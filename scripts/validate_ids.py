#!/usr/bin/env python3
from pathlib import Path
import re, sys

# 使い方: python scripts/validate_ids.py content/ch01/text.md
p = Path(sys.argv[1])

# chXX-YYYY の形式 (末尾に a,b など1文字つく可能性も許容)
id_pat = re.compile(r'^\[(ch\d{2}-\d{4}[a-z]?)\]\s')

seen = set()
ok = True

for i, ln in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
    if not ln.strip():  # 空行は無視
        continue
    m = id_pat.match(ln)
    if not m:
        print(f"{p}:{i}: 行頭にIDなし -> {ln[:30]}")
        ok = False
        continue
    _id = m.group(1)
    if _id in seen:
        print(f"{p}:{i}: 重複ID {_id}")
        ok = False
    seen.add(_id)

if ok:
    print("ok: ID検証通過")
sys.exit(0 if ok else 1)
