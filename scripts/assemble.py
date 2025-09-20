#!/usr/bin/env python3
from pathlib import Path
import re, sys, collections

# 使い方: python scripts/assemble.py content/ch01
ch = Path(sys.argv[1])

# ID形式を chXX-YYYY に変更
id_pat = re.compile(r'^\[(ch\d{2}-\d{4}[a-z]?)\]\s(.*)$')

def load_idmap(mdpath):
    m = collections.OrderedDict()
    if not mdpath.exists():
        return m
    for ln in mdpath.read_text(encoding="utf-8").splitlines():
        mo = id_pat.match(ln)
        if mo:
            m[mo.group(1)] = mo.group(2)
    return m

# 各種ファイルを読み込み
text_map = load_idmap(ch/"text.md")
trans_map = load_idmap(ch/"trans.md")  # 翻訳ファイル追加
wb_map   = load_idmap(ch/"commentary"/"wangbing.md")
md_map   = load_idmap(ch/"commentary"/"modern.md")

# 出力組み立て
out = []
out.append(f"# 統合ビュー {ch.name}\n")
for _id, src in text_map.items():
    out.append(f"## {_id}\n")
    out.append(f"**原文**：{src}  <a id=\"{_id}\"></a>\n")
    if _id in trans_map:
        out.append(f"**翻訳**：{trans_map[_id]}\n")
    if _id in wb_map:
        out.append(f"**王冰注**：{wb_map[_id]}\n")
    if _id in md_map:
        out.append(f"**現代注**：{md_map[_id]}\n")
    out.append("\n---\n")

(ch/"index.md").write_text("\n".join(out), encoding="utf-8")
print(f"wrote {ch/'index.md'}")
