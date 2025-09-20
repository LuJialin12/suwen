#!/usr/bin/env python3
"""text/translation/commentary の各ファイルを統合して index.md を生成するスクリプト."""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path
from typing import Iterable, Iterator, List, Tuple

ID_PATTERN = re.compile(r"^\[(ch\d{2}-\d{4}[a-z]?)\]\s*(.*)$", re.MULTILINE)
COMMENTARY_LABELS = {
    "wangbing": "王冰注",
    "modern": "現代注",
}


def load_entries(md_path: Path) -> "collections.OrderedDict[str, str]":
    """Return an ordered mapping of ID -> text for the given markdown file."""

    entries: "collections.OrderedDict[str, str]" = collections.OrderedDict()
    if not md_path.exists():
        return entries

    text = md_path.read_text(encoding="utf-8")
    matches = list(ID_PATTERN.finditer(text))
    if not matches:
        return entries

    for idx, match in enumerate(matches):
        _id = match.group(1)
        first_line = match.group(2).rstrip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        block = text[start:end]
        block = block.rstrip("\n")
        if block.startswith("\n"):
            block = block[1:]

        if first_line and block:
            content = f"{first_line}\n{block}"
        elif first_line:
            content = first_line
        else:
            content = block.lstrip("\n")

        entries[_id] = content

    return entries


def collect_commentaries(commentary_dir: Path) -> List[Tuple[str, "collections.OrderedDict[str, str]"]]:
    commentaries: List[Tuple[str, "collections.OrderedDict[str, str]"]] = []
    if not commentary_dir.exists():
        return commentaries

    for md_path in sorted(commentary_dir.glob("*.md")):
        label_key = md_path.stem
        label = COMMENTARY_LABELS.get(label_key, label_key)
        mapping = load_entries(md_path)
        if mapping:
            commentaries.append((label, mapping))

    return commentaries


def iter_chapters(paths: Iterable[Path]) -> Iterator[Path]:
    for path in paths:
        if (path / "text.md").exists():
            yield path
            continue
        if path.is_dir():
            for child in sorted(path.iterdir()):
                if (child / "text.md").exists():
                    yield child


def assemble(chapter_dir: Path) -> None:
    text_map = load_entries(chapter_dir / "text.md")
    if not text_map:
        raise SystemExit(f"text.md に ID 形式のエントリが見つかりません: {chapter_dir}")

    translation_path = chapter_dir / "translation.md"
    if not translation_path.exists():
        translation_path = chapter_dir / "trans.md"
    trans_map = load_entries(translation_path)

    commentaries = collect_commentaries(chapter_dir / "commentary")

    out_lines: List[str] = [f"# 統合ビュー {chapter_dir.name}", ""]

    for _id, src in text_map.items():
        out_lines.append(f"## {_id}")
        out_lines.append("")
        out_lines.append(f"**原文**：{src}  <a id=\"{_id}\"></a>")
        if _id in trans_map:
            out_lines.append(f"**翻訳**：{trans_map[_id]}")
        for label, mapping in commentaries:
            if _id in mapping:
                out_lines.append(f"**{label}**：{mapping[_id]}")
        out_lines.append("")
        out_lines.append("---")
        out_lines.append("")

    index_path = chapter_dir / "index.md"
    index_path.write_text("\n".join(out_lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {index_path}")


def main(argv: List[str]) -> None:
    if len(argv) < 2:
        print("使い方: python scripts/assemble.py <chapter dir> [<chapter dir> ...]")
        raise SystemExit(1)

    paths = [Path(arg) for arg in argv[1:]]
    chapters = list(iter_chapters(paths))
    if not chapters:
        raise SystemExit("text.md を含むディレクトリが見つかりませんでした。")

    for chapter in chapters:
        assemble(chapter)


if __name__ == "__main__":
    main(sys.argv)
