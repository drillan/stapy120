# CLAUDE.md

## 日本語テキストルール

日本語のスライドを書く際は `.claude/skills/natural-text/SKILL.md` のルールに従うこと。

## MyST 記法ルール

MyST記法を書く際は `.claude/skills/myst/SKILL.md` のルールに従うこと。

## sphinx-revealjs 設定ルール

sphinx-revealjsのconf.pyを編集する際は `.claude/skills/sphinx-revealjs/SKILL.md` のルールに従うこと。

## ビルドコマンド

### スライド（Reveal.js）

```sh
uv run make -C docs revealjs
```

## Active Technologies
- Python 3.13+ + Sphinx 9.1+, sphinx-revealjs 3.2+, myst-parser 5.0+, libsass 0.23+ (001-revealjs-slides-setup)
- N/A（静的サイト生成） (001-revealjs-slides-setup)
- N/A（Markdownルール文書の更新） + sphinxcontrib-mermaid 2.0.0（新規追加） (003-myst-notation-rules)
- MyST Markdown（myst-parser 5.0+） + Sphinx 9.1+, sphinx-revealjs 3.2+, sphinxcontrib-mermaid 2.0.0 (004-sdd-slide-content)

## Recent Changes
- 001-revealjs-slides-setup: Added Python 3.13+ + Sphinx 9.1+, sphinx-revealjs 3.2+, myst-parser 5.0+, libsass 0.23+
