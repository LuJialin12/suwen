#!/usr/bin/env python3
from pathlib import Path
import re
import sys

# 使い方: python scripts/add_ids.py content/ch01/text.md
p = Path(sys.argv[1])
lines = p.read_text(encoding="utf-8").splitlines()

id_pat = re.compile(r'^\[(L\d{4}[a-z]?)\]\s')
next_num = 1

# 既存IDの最大値を探す
for ln in lines:
    m = id_pat.match(ln)
    if m and re.match(r'^L(\d{4})$', m.group(1)):
        next_num = max(next_num, int(m.group(1)[1:]) + 1)

out = []
for ln in lines:
    if not ln.strip():  # 空行はそのまま
        out.append(ln)
        continue
    if id_pat.match(ln):  # すでにIDあり
        out.append(ln)
        continue
    # 新しいIDを付与
    new_id = f"L{next_num:04d}"
    out.append(f"[{new_id}] {ln}")
    next_num += 1

p.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"IDs added in {p}")
