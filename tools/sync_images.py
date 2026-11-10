#!/usr/bin/env python3
"""Link photos in images/elements/ to data/elements.json.

Name each photo after its element symbol, for example Cu.jpg or Au.png.
Run from anywhere:  python3 tools/sync_images.py
Then fill in the "credit" field for each photo in data/elements.json.
"""
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
path = root / "data" / "elements.json"
data = json.loads(path.read_text(encoding="utf-8"))
exts = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
linked = 0

for f in sorted((root / "images" / "elements").iterdir()):
    if f.suffix.lower() not in exts:
        continue
    if f.stem not in data:
        print("Skipped (file name must be an element symbol such as Cu):", f.name)
        continue
    rel = f"images/elements/{f.name}"
    if data[f.stem].get("image") != rel:
        data[f.stem]["image"] = rel
        linked += 1

path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Linked {linked} new image(s).")
