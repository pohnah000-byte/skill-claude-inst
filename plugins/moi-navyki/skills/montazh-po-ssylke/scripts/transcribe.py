#!/usr/bin/env python3
"""Расшифровка речи из видео/аудио в субтитры SRT и текст с таймкодами (faster-whisper).

Использование:
  python3 transcribe.py ВИДЕО [--model small] [--lang ru] [--out имя]

На выходе:
  имя.srt   — субтитры по фразам (для montage.py)
  имя.json  — фразы со временем начала и конца (чтобы выбрать лучшие моменты)
  имя.txt   — сплошной текст с таймкодами [мм:сс]

Модели: tiny / base / small / medium (чем больше, тем точнее и медленнее).
Для русского по умолчанию small. Первый запуск скачивает модель (~500 МБ для small).
Нужно: pip install faster-whisper   (+ ffmpeg)
"""
import argparse
import json
import os
import sys


def srt_time(s):
    ms = int(round(s * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    sec, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{sec:02},{ms:03}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("media")
    ap.add_argument("--model", default="small")
    ap.add_argument("--lang", default="ru", help="код языка или auto")
    ap.add_argument("--out", default=None)
    ap.add_argument("--max-chars", type=int, default=42, help="макс. длина одной фразы субтитров")
    args = ap.parse_args()

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print(json.dumps({"status": "error", "message": "Нет faster-whisper. Выполните: pip install faster-whisper"},
                         ensure_ascii=False))
        sys.exit(1)
    if not os.path.isfile(args.media):
        print(json.dumps({"status": "error", "message": f"Файл не найден: {args.media}"}, ensure_ascii=False))
        sys.exit(1)

    out = args.out or os.path.splitext(args.media)[0]
    # звук декодируем через ffmpeg сами: так не зависим от версии библиотеки av
    import subprocess
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", args.media, "-vn", "-ac", "1",
                          "-ar", "16000", "-f", "f32le", "-"], stdout=subprocess.PIPE).stdout
    if not raw:
        print(json.dumps({"status": "error", "message": "В файле нет звука или его не удалось прочитать"},
                         ensure_ascii=False))
        sys.exit(1)
    audio = np.frombuffer(raw, dtype=np.float32)
    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    segments, info = model.transcribe(audio, language=None if args.lang == "auto" else args.lang,
                                      word_timestamps=True, vad_filter=True)

    # режем на короткие фразы по словам, чтобы субтитры не были простынёй
    phrases = []
    for seg in segments:
        words = seg.words or []
        if not words:
            phrases.append({"start": seg.start, "end": seg.end, "text": seg.text.strip()})
            continue
        cur, start = "", None
        for w in words:
            token = w.word.strip()
            if start is None:
                start = w.start
            if cur and len(cur) + 1 + len(token) > args.max_chars:
                phrases.append({"start": start, "end": prev_end, "text": cur})
                cur, start = token, w.start
            else:
                cur = (cur + " " + token).strip()
            prev_end = w.end
            if token.endswith((".", "!", "?", "…")) and len(cur) > 12:
                phrases.append({"start": start, "end": w.end, "text": cur})
                cur, start = "", None
        if cur:
            phrases.append({"start": start, "end": prev_end, "text": cur})

    # приклеиваем короткие «хвосты» (2–3 слова) к предыдущей фразе
    merged = []
    for p in phrases:
        if (merged and len(p["text"]) < 14 and p["start"] - merged[-1]["end"] < 0.3
                and not merged[-1]["text"].endswith((".", "!", "?", "…"))
                and len(merged[-1]["text"]) + len(p["text"]) <= args.max_chars + 16):
            merged[-1] = {"start": merged[-1]["start"], "end": p["end"], "text": merged[-1]["text"] + " " + p["text"]}
        else:
            merged.append(p)
    phrases = merged

    with open(out + ".srt", "w", encoding="utf-8") as f:
        for i, p in enumerate(phrases, 1):
            f.write(f"{i}\n{srt_time(p['start'])} --> {srt_time(p['end'])}\n{p['text']}\n\n")
    with open(out + ".json", "w", encoding="utf-8") as f:
        json.dump([{"start": round(p["start"], 2), "end": round(p["end"], 2), "text": p["text"]} for p in phrases],
                  f, ensure_ascii=False, indent=1)
    with open(out + ".txt", "w", encoding="utf-8") as f:
        for p in phrases:
            m, s = divmod(int(p["start"]), 60)
            f.write(f"[{m:02}:{s:02}] {p['text']}\n")
    print(json.dumps({"status": "ok", "language": info.language, "duration": round(info.duration, 1),
                      "phrases": len(phrases), "srt": out + ".srt", "json": out + ".json", "txt": out + ".txt"},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
