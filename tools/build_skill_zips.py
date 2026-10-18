#!/usr/bin/env python3
"""Собирает каждый навык из plugins/ в отдельный zip для загрузки в Claude (Настройки → Возможности → Навыки).

Использование: python3 tools/build_skill_zips.py [папка_вывода]   (по умолчанию skills-zip/)
"""
import glob, re, yaml, os, json, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(ROOT, "plugins")
D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "skills-zip")
os.makedirs(D, exist_ok=True)
RENAME = {("data", "analyze"): "data-analyze", ("productivity", "update"): "productivity-update",
          ("extract-alpha", "prompt"): "extract-alpha-prompt", ("design", "design-critique"): "design-critique-brief"}
SKIP_DIRS = {".github", "demos", "gallery", "workbench", "node_modules", "__pycache__", ".claude-plugin"}
SKIP_FILES = {"README_CN.md", "README_JA.md", "package-lock.json", ".DS_Store"}
ALLOWED = {"name", "description", "license", "allowed-tools", "compatibility", "metadata"}


def s(v):
    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)


out = []
for sk in sorted(glob.glob(R + "/*/**/SKILL.md", recursive=True)):
    rel = os.path.relpath(sk, R)
    plug = rel.split("/")[0]
    d = os.path.dirname(sk)
    t = open(sk, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    fm = yaml.safe_load(m.group(1))
    body = t[m.end():]
    name = RENAME.get((plug, fm["name"]), fm["name"])
    meta = {k: s(v) for k, v in (fm.get("metadata") or {}).items()} if isinstance(fm.get("metadata"), dict) else {}
    meta.update({k: s(v) for k, v in fm.items() if k not in ALLOWED})
    meta.setdefault("plugin", plug)
    nfm = {"name": name, "description": fm["description"]}
    lic = fm.get("license") or json.load(open(f"{R}/{plug}/.claude-plugin/plugin.json", encoding="utf-8")).get("license")
    if lic:
        nfm["license"] = lic
    for k in ("allowed-tools", "compatibility"):
        if fm.get(k):
            nfm[k] = " ".join(fm[k]) if isinstance(fm[k], list) else str(fm[k])
    nfm["metadata"] = meta
    text = "---\n" + yaml.safe_dump(nfm, allow_unicode=True, sort_keys=False, width=100000) + "---\n" + body
    zp = os.path.join(D, name + ".zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{name}/SKILL.md", text)
        for root, dirs, files in os.walk(d):
            dirs[:] = [x for x in dirs if x not in SKIP_DIRS
                       and not glob.glob(os.path.join(root, x, "**", "SKILL.md"), recursive=True)]
            for f in files:
                fp = os.path.join(root, f)
                if fp == sk or f in SKIP_FILES:
                    continue
                z.write(fp, f"{name}/" + os.path.relpath(fp, d))
        names = set(z.namelist())
        lf = glob.glob(f"{R}/{plug}/LICENSE*")
        if lf and not any(n.split("/")[-1].startswith("LICENSE") for n in names):
            z.write(lf[0], f"{name}/LICENSE.txt")
    out.append({"name": name, "plugin": plug, "size_kb": os.path.getsize(zp) // 1024})
json.dump(out, open(os.path.join(D, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"Собрано навыков: {len(out)} → {D}")
