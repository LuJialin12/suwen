from pathlib import Path

base = Path("suwen/content")

#ch04~ch81を作る
for i in range(4, 82):
    new_ch = base / f"ch{i:02d}"
    files = [
        new_ch /"text.md",
        new_ch /"translation.md",
        new_ch /"commentary/modern.md",
        new_ch /"commentary/wangbing.md",
        new_ch /"notes.md",
        new_ch /"index.md",
    ]
    for f in files:
        f.parent.mkdir(parents=True, exist_ok=True) #ディレクトリ生成
        f.write_text("") #空ファイル