# Contributing to Suwen / 素問プロジェクトへの貢献

まずは本プロジェクトに興味を持ってくださり、ありがとうございます！  
このプロジェクトは、臨床家・学生・研究者が協働しながら、『黄帝内経・素問』の原文・歴代注釈・現代翻訳を整理・批判的に読解できるオープンな基盤を作ることを目的としています。

---

## 📌 プロジェクト概要 / Project Overview

- 原文・注釈・翻訳を構造化し、GitHub 上で共同編集  
- 臨床家による現代注を充実させ、学術的な読み解きの土台を形成  
- 自動スクリプトで index.md を生成して整合性を維持  
- 将来的には Web ビューワー、教育教材化も視野に入れています

---

## 🧭 貢献の方法 / How to Contribute

### 📝 1. Issue を立てる
誤字脱字、翻訳・注釈の改善提案、新機能やスクリプト改善などを歓迎します。  
[GitHub Issues](../../issues) にて以下を含めてください：

- 問題や提案の概要（タイトル）
- 背景・根拠・参照文献（必要に応じて）
- 再現手順や対象ファイル（翻訳対象行など）

**Issue タイプ例：**
- 🐛 Typo / Bug
- 💬 翻訳・注釈改善
- 📚 文献追加提案
- 🧰 スクリプト改善
- 💡 機能提案・議論

---

### 🔧 2. Pull Request（PR）の送信
翻訳・注釈・スクリプト・ドキュメントの改善は PR で行います。  
基本的な流れは以下の通りです👇

1. このリポジトリを Fork  
2. 新しいブランチを作成（例：`fix/typo-ch03`、`feature/add-modern-commentary`）  
3. 修正・追加を実施  
4. スクリプトで ID と統合ビューの整合性を確認
   ```bash
   python scripts/validate_ids.py
   python scripts/assemble.py content/chXX
````

5. PR を作成し、内容・根拠・対象行などを明記

**PR では以下を意識してください：**

* 1 つの PR に 1 つの目的
* 翻訳・注釈では対象となる行IDを明記（例：`[ch01-0042]`）
* 文献・典拠がある場合は脚注・参考を記載
* `index.md` の自動生成結果も含めること

---

## 📂 ディレクトリ構成 / Directory Structure

```
suwen/
├─ content/
│  ├─ ch01/
│  │  ├─ text.md          # 原文（行ID付き）
│  │  ├─ translation.md   # 現代語訳
│  │  ├─ notes.md         # 補足メモ
│  │  ├─ index.md         # 自動生成統合ビュー
│  │  └─ commentary/
│  │     ├─ wangbing.md   # 王冰注
│  │     └─ modern.md     # 現代注
├─ scripts/                # ID付与・統合など
├─ output/                 # PDF/EPUB などの生成物
└─ ...
```

---

## 🧪 ローカル環境の構築 / Local Development

```bash
git clone https://github.com/LuJialin12/suwen.git
cd suwen

# Python 仮想環境を作る（必要に応じて）
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # （必要であれば）

# 行IDの追加・チェック・統合
python scripts/add_ids.py content/ch01/text.md
python scripts/validate_ids.py
python scripts/assemble.py content/ch01
```

---

## 🧠 翻訳・注釈の編集ルール / Editorial Guidelines

* **翻訳**：忠実でありつつ、現代日本語として自然で臨床家が理解しやすい表現を心がける
* **注釈**：

  * 歴代注（王冰など）は元文を尊重し、出典を明記
  * 現代注は臨床的解釈や現代医学的比較を歓迎
* **行ID**：削除・変更は不可。新規追加時は `scripts/add_ids.py` を使用
* **Markdown 記法**：

  * 原文・翻訳・注釈すべて Markdown 形式で記述
  * 脚注・参考文献リンクを活用（例：`[^1]`）

---

## 🧭 コーディング規約 / Coding Style

* Python スクリプトは PEP8 準拠
* 自動整形には `black` の利用を推奨
* スクリプト追加時は簡単な docstring を書くこと

---

## 🧾 Pull Request チェックリスト / PR Checklist

* [ ] Issue と対応が明記されている
* [ ] 目的が明確で、変更内容が整理されている
* [ ] ID の整合性チェック済み (`validate_ids.py`)
* [ ] 統合ビュー生成済み (`assemble.py`)
* [ ] 翻訳・注釈には根拠や文献を明記（必要に応じて）

---

## 📜 ライセンス / License

このプロジェクトは [MIT License](./LICENSE) のもとで公開されています。
商用利用・改変・再配布は自由ですが、**著作権表示を保持**してください。

---

## 🌐 English Summary

This project welcomes contributions in translation, annotation, scripting, and documentation.
Please follow the workflow:

1. Open an Issue for proposals
2. Create a feature branch and make edits
3. Run scripts to validate and assemble
4. Submit a PR with clear explanations and references

License: MIT

---

## 🙏 謝辞 / Acknowledgements

翻訳・注釈・スクリプト改善に貢献してくださる皆さまに深く感謝いたします。
このプロジェクトは東洋医学を学ぶすべての人々のための共同作業場です。

