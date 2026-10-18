#!/usr/bin/env python3
"""Монтаж короткого вертикального видео по плану (JSON) с помощью ffmpeg.

Подкоманды:
  analyze  ВИДЕО                 — длительность, размер, паузы и смены сцен (JSON)
  render   ПЛАН.json             — смонтировать ролик по плану
  example                        — вывести пример плана

Что умеет render:
  * склеить выбранные отрезки (segments) в нужном порядке;
  * вырезать паузы в речи (remove_silence);
  * перевести в 9:16 / 1:1 / 4:5 / 16:9 с размытым фоном или кадрированием;
  * наложить субтитры из SRT (с пересчётом времени после вырезок),
    короткими фразами по N слов, своим шрифтом и цветом;
  * хук-текст на экране в первые секунды;
  * логотип, музыка с приглушением под голос, финальная заставка с призывом;
  * ускорение, нормализация громкости под соцсети (-14 LUFS), обложка PNG.

Нужны только ffmpeg и ffprobe. Сторонние Python-библиотеки не нужны.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap

FORMATS = {"9:16": (1080, 1920), "1:1": (1080, 1080), "4:5": (1080, 1350), "16:9": (1920, 1080)}
FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]

EXAMPLE = {
    "input": "исходник.mp4",
    "output": "reels.mp4",
    "format": "9:16",
    "reframe": "blur",
    "segments": [{"start": "00:00:12.0", "end": "00:00:31.5"}, {"start": "00:01:05", "end": "00:01:20"}],
    "remove_silence": {"enabled": True, "threshold_db": -35, "min_silence": 0.5, "keep_padding": 0.12},
    "speed": 1.0,
    "subtitles": {"file": "исходник.srt", "words_per_chunk": 3, "uppercase": False,
                  "font": None, "size": 72, "color": "#FFFFFF", "highlight": "#FFE14D",
                  "outline_color": "#000000", "outline": 5, "position": "center"},
    "hook": {"text": "3 ошибки, из-за которых тебя не берут на работу", "duration": 3.0, "size": 64},
    "logo": {"file": "logo.png", "position": "top-right", "scale": 0.16, "opacity": 0.9},
    "music": {"file": "music.mp3", "volume": 0.18, "duck": True},
    "end_card": {"text": "Подпишись — дальше больше", "duration": 2.0},
    "loudnorm": True,
    "cover": {"at": 1.0, "file": "обложка.png"},
}


# ---------- утилиты ----------

def die(msg):
    print(json.dumps({"status": "error", "message": msg}, ensure_ascii=False))
    sys.exit(1)


def need(tool):
    if not shutil.which(tool):
        die(f"Не найден {tool}. Установите ffmpeg (в нём есть ffmpeg и ffprobe).")


def t2s(v):
    """'1:05.5', '00:01:05,5', '65.5' или число -> секунды."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    v = str(v).strip().replace(",", ".")
    parts = v.split(":")
    try:
        sec = 0.0
        for p in parts:
            sec = sec * 60 + float(p)
        return sec
    except ValueError:
        die(f"Не понимаю время: {v!r}. Пишите как 75.5, 1:15.5 или 00:01:15.5")


def s2srt(s):
    ms = int(round(s * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    sec, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{sec:02},{ms:03}"


def s2ass(s):
    cs = int(round(s * 100))
    h, cs = divmod(cs, 360000)
    m, cs = divmod(cs, 6000)
    sec, cs = divmod(cs, 100)
    return f"{h}:{m:02}:{sec:02}.{cs:02}"


def run(cmd, capture=True):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        tail = "\n".join(p.stderr.strip().splitlines()[-15:])
        die("ffmpeg завершился с ошибкой:\n" + tail)
    return p


def probe(path):
    if not os.path.isfile(path):
        die(f"Файл не найден: {path}")
    p = run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path])
    info = json.loads(p.stdout)
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    if v is None:
        die("В файле нет видеодорожки.")
    num, den = (v.get("avg_frame_rate") or "30/1").split("/")
    fps = float(num) / float(den) if float(den) else 30.0
    rot = 0
    for sd in v.get("side_data_list", []) or []:
        if "rotation" in sd:
            rot = int(sd["rotation"])
    w, h = int(v["width"]), int(v["height"])
    if abs(rot) in (90, 270):
        w, h = h, w
    return {"duration": float(info["format"].get("duration", 0)), "width": w, "height": h,
            "fps": round(fps, 3), "has_audio": a is not None}


def find_font(custom=None):
    if custom and os.path.isfile(custom):
        return custom
    for f in FONT_CANDIDATES:
        if os.path.isfile(f):
            return f
    if shutil.which("fc-match"):
        p = subprocess.run(["fc-match", "-f", "%{file}", "sans:bold:lang=ru"], stdout=subprocess.PIPE, text=True)
        if p.stdout and os.path.isfile(p.stdout):
            return p.stdout
    die("Не нашёл шрифт с кириллицей. Укажите путь к .ttf/.otf в поле font.")


def font_family(path):
    if shutil.which("fc-scan"):
        p = subprocess.run(["fc-scan", "--format", "%{family[0]}", path], stdout=subprocess.PIPE, text=True)
        if p.stdout.strip():
            return p.stdout.strip()
    return os.path.splitext(os.path.basename(path))[0]


def esc_filter_path(p):
    return p.replace("\\", "/").replace(":", r"\:").replace("'", r"\'")


def ass_color(hex_color, alpha=0):
    h = hex_color.lstrip("#")
    r, g, b = h[0:2], h[2:4], h[4:6]
    return f"&H{alpha:02X}{b}{g}{r}".upper()


# ---------- анализ ----------

def detect_silences(path, start, end, thresh_db, min_sil):
    cmd = ["ffmpeg", "-hide_banner", "-nostats", "-ss", str(start), "-to", str(end), "-i", path,
           "-vn", "-af", f"silencedetect=n={thresh_db}dB:d={min_sil}", "-f", "null", "-"]
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    sil, cur = [], None
    for line in p.stderr.splitlines():
        m = re.search(r"silence_start: ([\d.]+)", line)
        if m:
            cur = float(m.group(1)) + start
        m = re.search(r"silence_end: ([\d.]+)", line)
        if m and cur is not None:
            sil.append((cur, float(m.group(1)) + start))
            cur = None
    if cur is not None:
        sil.append((cur, end))
    return sil


def detect_scenes(path, threshold=0.35):
    cmd = ["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-an",
           "-vf", f"select='gt(scene,{threshold})',showinfo", "-f", "null", "-"]
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return [round(float(m), 2) for m in re.findall(r"pts_time:([\d.]+)", p.stderr)]


def cmd_analyze(path):
    info = probe(path)
    out = dict(info)
    if info["has_audio"]:
        sil = detect_silences(path, 0, info["duration"], -35, 0.5)
        out["silences"] = [[round(a, 2), round(b, 2)] for a, b in sil]
        out["silence_total"] = round(sum(b - a for a, b in sil), 2)
    out["scene_changes"] = detect_scenes(path)
    print(json.dumps(out, ensure_ascii=False, indent=1))


# ---------- план монтажа ----------

def keep_intervals(plan, info):
    dur = info["duration"]
    segs = plan.get("segments") or [{"start": 0, "end": dur}]
    base = []
    for s in segs:
        a, b = max(0.0, t2s(s.get("start", 0))), min(dur, t2s(s.get("end", dur)))
        if b - a < 0.2:
            die(f"Отрезок {s} слишком короткий или выходит за длину видео ({dur:.1f} с).")
        base.append((a, b))
    rs = plan.get("remove_silence") or {}
    if not (rs.get("enabled") and info["has_audio"]):
        return base
    pad = float(rs.get("keep_padding", 0.12))
    out = []
    for a, b in base:
        sil = detect_silences(plan["input"], a, b, rs.get("threshold_db", -35), rs.get("min_silence", 0.5))
        cur = a
        for s0, s1 in sil:
            s0p, s1p = s0 + pad, s1 - pad
            if s1p - s0p <= 0.05:
                continue
            if s0p - cur >= 0.25:
                out.append((cur, s0p))
            cur = max(cur, s1p)
        if b - cur >= 0.25:
            out.append((cur, b))
    if not out:
        die("После удаления пауз ничего не осталось — уменьшите threshold_db (например, -45).")
    return out


def parse_srt(path):
    raw = open(path, encoding="utf-8-sig").read().replace("\r", "")
    cues = []
    for block in re.split(r"\n\s*\n", raw.strip()):
        lines = block.split("\n")
        for i, ln in enumerate(lines):
            m = re.match(r"(\S+)\s*-->\s*(\S+)", ln)
            if m:
                text = " ".join(x.strip() for x in lines[i + 1:] if x.strip())
                text = re.sub(r"<[^>]+>", "", text)
                if text:
                    cues.append((t2s(m.group(1)), t2s(m.group(2)), text))
                break
    return cues


def remap_cues(cues, keeps, speed):
    """Переносит время субтитров из исходника на смонтированную шкалу."""
    out, offset = [], 0.0
    for ka, kb in keeps:
        for ca, cb, text in cues:
            a, b = max(ca, ka), min(cb, kb)
            if b - a > 0.15:
                out.append(((a - ka + offset) / speed, (b - ka + offset) / speed, text))
        offset += kb - ka
    merged = []
    for c in sorted(out):
        if merged and merged[-1][2] == c[2] and c[0] - merged[-1][1] < 0.05:
            merged[-1] = (merged[-1][0], c[1], c[2])
        else:
            merged.append(c)
    return merged


def chunk_cues(cues, n):
    if not n or n <= 0:
        return cues
    out = []
    for a, b, text in cues:
        words = text.split()
        if len(words) <= n:
            out.append((a, b, text))
            continue
        groups = [words[i:i + n] for i in range(0, len(words), n)]
        total = sum(len(" ".join(g)) for g in groups)
        t = a
        for g in groups:
            d = (b - a) * len(" ".join(g)) / total
            out.append((t, t + d, " ".join(g)))
            t += d
    return out


def write_ass(cues, st, W, H, font_path, path):
    fam = font_family(font_path)
    size = int(st.get("size", 72) * W / 1080)
    outline = st.get("outline", 5)
    pos = st.get("position", "center")
    align = {"bottom": 2, "center": 5, "top": 8}.get(pos, 5)
    margin_v = int(H * (0.18 if pos == "bottom" else 0.12 if pos == "top" else 0))
    if pos == "center":
        align, margin_v = 2, int(H * 0.30)
    primary = ass_color(st.get("color", "#FFFFFF"))
    outc = ass_color(st.get("outline_color", "#000000"))
    hl = st.get("highlight")
    lines = [
        "[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 0", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
        "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
        f"Style: Main,{fam},{size},{primary},{primary},{outc},&H80000000,-1,0,0,0,100,100,0,0,1,{outline},2,{align},{int(W*0.08)},{int(W*0.08)},{margin_v},1",
        "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    for i, (a, b, text) in enumerate(cues):
        if st.get("uppercase"):
            text = text.upper()
        text = text.replace("{", "(").replace("}", ")")
        if hl:
            words = text.split()
            if words:
                k = max(range(len(words)), key=lambda j: len(words[j].strip(".,!?…:;—-«»")))
                words[k] = "{\\c" + ass_color(hl) + "}" + words[k] + "{\\c" + primary + "}"
                text = " ".join(words)
        lines.append(f"Dialogue: 0,{s2ass(a)},{s2ass(b)},Main,,0,0,0,,{text}")
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")


def wrap_text(text, width):
    return "\n".join(textwrap.wrap(text, width=width)) or text


def cmd_render(plan_path):
    plan = json.load(open(plan_path, encoding="utf-8"))
    base_dir = os.path.dirname(os.path.abspath(plan_path))

    def P(x):
        return x if os.path.isabs(x) else os.path.join(base_dir, x)

    plan["input"] = P(plan["input"])
    info = probe(plan["input"])
    out_path = P(plan.get("output", "result.mp4"))
    fmt = plan.get("format", "9:16")
    if fmt == "original":
        W, H = info["width"] - info["width"] % 2, info["height"] - info["height"] % 2
    elif fmt in FORMATS:
        W, H = FORMATS[fmt]
    else:
        die(f"Неизвестный формат {fmt}. Варианты: {', '.join(FORMATS)}, original")
    speed = float(plan.get("speed", 1.0))
    if not 0.5 <= speed <= 2.0:
        die("speed должен быть от 0.5 до 2.0")
    font = find_font((plan.get("subtitles") or {}).get("font") or plan.get("font"))
    keeps = keep_intervals(plan, info)
    body = sum(b - a for a, b in keeps) / speed
    tmp = tempfile.mkdtemp(prefix="montage-")

    inputs = ["-i", plan["input"]]
    fc = []
    n = len(keeps)
    for i, (a, b) in enumerate(keeps):
        fc.append(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS[v{i}]")
        if info["has_audio"]:
            fc.append(f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS[a{i}]")
    if info["has_audio"]:
        fc.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[vc][ac]")
    else:
        fc.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[vc]")
        fc.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{body:.3f}[ac]")
    v, a = "vc", "ac"
    if speed != 1.0:
        fc.append(f"[{v}]setpts=PTS/{speed}[vs]")
        fc.append(f"[{a}]atempo={speed}[as]")
        v, a = "vs", "as"

    # формат кадра
    mode = plan.get("reframe", "blur")
    if fmt == "original":
        fc.append(f"[{v}]scale={W}:{H}[vf]")
    elif mode == "crop":
        fc.append(f"[{v}]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}[vf]")
    else:
        fc.append(f"[{v}]split[bg0][fg0]")
        fc.append(f"[bg0]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:6,eq=brightness=-0.08[bg]")
        fc.append(f"[fg0]scale={W}:{H}:force_original_aspect_ratio=decrease[fg]")
        fc.append("[bg][fg]overlay=(W-w)/2:(H-h)/2[vf]")
    fc.append("[vf]fps=30,setsar=1,format=yuv420p[vr]")
    v = "vr"

    # субтитры
    st = plan.get("subtitles")
    if st and st.get("file"):
        cues = remap_cues(parse_srt(P(st["file"])), keeps, speed)
        cues = chunk_cues(cues, int(st.get("words_per_chunk", 0) or 0))
        ass = os.path.join(tmp, "subs.ass")
        write_ass(cues, st, W, H, font, ass)
        fontsdir = os.path.dirname(font)
        fc.append(f"[{v}]subtitles='{esc_filter_path(ass)}':fontsdir='{esc_filter_path(fontsdir)}'[vsub]")
        v = "vsub"

    # хук
    hook = plan.get("hook")
    if hook and hook.get("text"):
        size = int(hook.get("size", 64) * W / 1080)
        chars = max(10, int(W * 0.84 / (size * 0.56)))
        tf = os.path.join(tmp, "hook.txt")
        open(tf, "w", encoding="utf-8").write(wrap_text(hook["text"], chars))
        d = float(hook.get("duration", 3.0))
        fc.append(f"[{v}]drawtext=fontfile='{esc_filter_path(font)}':textfile='{esc_filter_path(tf)}':"
                  f"fontsize={size}:fontcolor={hook.get('color', 'white')}:line_spacing={int(size*0.25)}:"
                  f"box=1:boxcolor={hook.get('box_color', 'black@0.6')}:boxborderw={int(size*0.45)}:"
                  f"x=(w-text_w)/2:y=h*0.14:enable='lt(t,{d})'[vh]")
        v = "vh"

    # логотип
    logo = plan.get("logo")
    if logo and logo.get("file"):
        inputs += ["-i", P(logo["file"])]
        li = inputs.count("-i") - 1
        lw = int(W * float(logo.get("scale", 0.16)))
        m = int(W * 0.04)
        pos = {"top-right": f"W-w-{m}:{m}", "top-left": f"{m}:{m}",
               "bottom-right": f"W-w-{m}:H-h-{m}", "bottom-left": f"{m}:H-h-{m}"}.get(logo.get("position", "top-right"))
        fc.append(f"[{li}:v]scale={lw}:-1,format=rgba,colorchannelmixer=aa={logo.get('opacity', 0.9)}[lg]")
        fc.append(f"[{v}][lg]overlay={pos}[vl]")
        v = "vl"

    # финальная заставка
    end = plan.get("end_card")
    total = body
    if end and end.get("text"):
        d = float(end.get("duration", 2.0))
        size = int(end.get("size", 72) * W / 1080)
        chars = max(10, int(W * 0.8 / (size * 0.56)))
        tf = os.path.join(tmp, "end.txt")
        open(tf, "w", encoding="utf-8").write(wrap_text(end["text"], chars))
        fc.append(f"[{v}]tpad=stop_mode=clone:stop_duration={d},"
                  f"drawbox=color=black@0.65:t=fill:enable='gte(t,{body:.3f})',"
                  f"drawtext=fontfile='{esc_filter_path(font)}':textfile='{esc_filter_path(tf)}':fontsize={size}:"
                  f"fontcolor=white:line_spacing={int(size*0.25)}:x=(w-text_w)/2:y=(h-text_h)/2:enable='gte(t,{body:.3f})'[ve]")
        fc.append(f"[{a}]apad=pad_dur={d}[ap]")
        v, a = "ve", "ap"
        total = body + d

    # музыка
    mus = plan.get("music")
    if mus and mus.get("file"):
        inputs += ["-stream_loop", "-1", "-i", P(mus["file"])]
        mi = inputs.count("-i") - 1
        fade = max(0.0, total - 1.5)
        fc.append(f"[{mi}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={mus.get('volume', 0.18)},"
                  f"atrim=0:{total:.3f},afade=t=out:st={fade:.3f}:d=1.5[m0]")
        fc.append(f"[{a}]aformat=sample_rates=48000:channel_layouts=stereo[vo]")
        if mus.get("duck", True) and info["has_audio"]:
            fc.append("[vo]asplit[vo1][sc]")
            fc.append("[m0][sc]sidechaincompress=threshold=0.04:ratio=8:attack=20:release=400[md]")
            fc.append("[vo1][md]amix=inputs=2:duration=first:normalize=0[am]")
        else:
            fc.append("[vo][m0]amix=inputs=2:duration=first:normalize=0[am]")
        a = "am"

    if plan.get("loudnorm", True):
        fc.append(f"[{a}]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")
    else:
        fc.append(f"[{a}]aresample=48000[aout]")
    a = "aout"

    script = os.path.join(tmp, "graph.txt")
    open(script, "w", encoding="utf-8").write(";\n".join(fc))
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *inputs,
           "-filter_complex_script", script, "-map", f"[{v}]", "-map", f"[{a}]",
           "-t", f"{total:.3f}", "-c:v", "libx264", "-preset", plan.get("preset", "medium"), "-crf", str(plan.get("crf", 20)),
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out_path]
    run(cmd)

    result = {"status": "ok", "output": out_path, "duration": round(probe(out_path)["duration"], 2),
              "size": f"{W}x{H}", "pieces": len(keeps),
              "removed_seconds": round(sum(t2s(s.get("end", info["duration"])) - t2s(s.get("start", 0))
                                           for s in (plan.get("segments") or [{"start": 0, "end": info["duration"]}]))
                                       - sum(b - a for a, b in keeps), 2)}
    cov = plan.get("cover")
    if cov:
        cp = P(cov.get("file", os.path.splitext(out_path)[0] + "_cover.png"))
        run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", str(t2s(cov.get("at", 1.0))),
             "-i", out_path, "-frames:v", "1", cp])
        result["cover"] = cp
    shutil.rmtree(tmp, ignore_errors=True)
    print(json.dumps(result, ensure_ascii=False, indent=1))


def main():
    need("ffmpeg")
    need("ffprobe")
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return
    cmd = sys.argv[1]
    if cmd == "example":
        print(json.dumps(EXAMPLE, ensure_ascii=False, indent=1))
    elif cmd == "analyze" and len(sys.argv) == 3:
        cmd_analyze(sys.argv[2])
    elif cmd == "render" and len(sys.argv) == 3:
        cmd_render(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
