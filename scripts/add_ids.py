#!/usr/bin/env python3
from pathlib import Path
import re
import sys

# 使い方: python scripts/add_ids.py content/ch01/text.md
p = Path(sys.argv[1])
lines = p.read_text(encoding="utf-8").splitlines()

# ファイルパスから章番号を抽出 (例: ch01 → 01)
chapter_match = re.search(r"ch(\d+)", str(p))
if chapter_match:
    chapter_num = int(chapter_match.group(1))
else:
    print("ファイル名から章番号を取得できませんでした。")
    sys.exit(1)

# IDパターンを chXX-YYYY 形式に変更
id_pat = re.compile(r'^\[(ch\d{2}-\d{4}[a-z]?)\]\s')
next_num = 1

# 既存IDの最大値を探す
for ln in lines:
    m = id_pat.match(ln)
    if m and re.match(r'^ch\d{2}-(\d{4})$', m.group(1)):
        next_num = max(next_num, int(m.group(1).split("-")[1]) + 1)

out = []
for ln in lines:
    if not ln.strip():  # 空行はそのまま
        out.append(ln)
        continue
    if id_pat.match(ln):  # すでにIDあり
        out.append(ln)
        continue
    # 新しいIDを付与
    new_id = f"ch{chapter_num:02d}-{next_num:04d}"
    out.append(f"[{new_id}] {ln}")
    next_num += 1

p.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"IDs added in {p}")
