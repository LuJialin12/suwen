# 黄帝内経 注釈・翻訳プロジェクト

**Huangdi Neijing Annotation & Translation Project**

---

## 📖 プロジェクト概要 / Project Overview

本プロジェクトは、**臨床家の視点**から中国医学古典（特に *黄帝内経*）を整理し、

* 歴代注釈と現代翻訳をオープンに公開
* 臨床に役立つ現代医学的な考察も交えて批判的に吟味
* 東洋医学を学ぶすべての人の「ベースアップ」を目指す

This project organizes the classical Chinese medical text *Huangdi Neijing* from the **perspective of clinicians**:

* Open publication of historical annotations and modern translations
* Critical review with perspectives from contemporary medicine
* Building a foundation for raising the baseline knowledge of all students of East Asian medicine

---

## 🚀 目的 / Goals

* 臨床家の経験を反映した注釈・翻訳を誰でも読める形にする

* 古典を**現代医学と比較・吟味**できる土台を作る

* 学生・臨床家・研究者が共に議論できる環境を育てる

* Make clinician-informed annotations and translations freely accessible

* Provide a basis for **critical evaluation through comparison with modern medicine**

* Foster an environment where students, clinicians, and researchers can discuss together

---

## 🔧 使い方 / Usage

1. リポジトリをクローン

   ```bash
   git clone https://github.com/<your-org>/<repo-name>.git
   cd <repo-name>
   ```

2. 原文・注釈・翻訳は `content/` ディレクトリに整理済み

   * `text.md` … 原文 / Original text
   * `translation.md` … 翻訳 / Translation
   * `commentary/` … 歴代注・現代注 / Historical & modern commentaries

3. 統合ビューを生成

   ```bash
   python scripts/assemble.py content/ch01
   ```

---

## 📂 ディレクトリ構成 / Directory Structure

```
content/
 ├── ch01/
 │   ├── text.md
 │   ├── translation.md
 │   └── commentary/
 │       ├── wangbing.md
 │       └── modern.md
 └── ch02/ ...
```

---

## 🤝 貢献方法 / Contributing

* **Issue**: 誤字脱字・改善案・議論提案などを歓迎します

* **Pull Request**: 翻訳修正・注釈追加・スクリプト改善を受け付けます

* 詳細ルールは [`CONTRIBUTING.md`](./CONTRIBUTING.md) を参照してください

* **Issues**: Report typos, propose improvements, or start discussions

* **Pull Requests**: Submit translation edits, add annotations, or improve scripts

* See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for detailed guidelines

---

## 🗺️ ロードマップ / Roadmap

* [ ] 全章の原文・翻訳・注釈を収録 / Collect all chapters with translations & commentaries
* [ ] 臨床家による現代注の拡充 / Expand clinician-based modern commentary
* [ ] Webビューワー公開（注釈切替機能）/ Publish a web viewer with toggleable commentaries
* [ ] 教育資料としての活用 / Utilize as teaching material

---

## 📜 ライセンス / License

本プロジェクトは **MITライセンス** の下で公開しています。
商用利用・改変・再配布は自由ですが、著作権表示を保持してください。

This project is released under the **MIT License**.
Commercial use, modification, and redistribution are permitted with attribution.

---

## 🌐 コミュニティ / Community

* 議論や情報交換は [GitHub Issues](./issues) にて
* Discussions and knowledge sharing via [GitHub Issues](./issues) or Discord/Slack (coming soon)
