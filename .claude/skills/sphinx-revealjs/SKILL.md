---
name: sphinx-revealjs
description: sphinx-revealjsの設定ルール。(1) Reveal.jsプラグインはUMDバンドル版を使用する。(2) ハイライトにはCSSテーマの読み込みが必須。(3) スライド幅はrevealjs_script_confで調整する。(4) Mermaidダイアグラムはサーバーサイドレンダリング（SVG）が必須。sphinx-revealjsのconf.pyを編集するときに適用する。
---

# sphinx-revealjs 設定ルール

## プラグイン設定 (`revealjs_script_plugins`)

- `src`パスに`_static/`プレフィックスは不要（ビルダーが自動付加する）
- Reveal.jsプラグインには2種類のファイルが存在する:
  - `plugin.js` — ESモジュール形式（`import`文を使用）。`<script>`タグでは動作しない
  - `highlight.js`等 — UMDバンドル形式。`<script>`タグで読み込み可能
- `src`には必ずUMDバンドル版を指定する
- `name`はReveal.jsが認識するグローバル名を指定する

### 利用可能なプラグイン

```python
# シンタックスハイライト
{"src": "revealjs/plugin/highlight/highlight.js", "name": "RevealHighlight"}
# スピーカーノート
{"src": "revealjs/plugin/notes/notes.js", "name": "RevealNotes"}
# 数式
{"src": "revealjs/plugin/math/math.js", "name": "RevealMath"}
# スライド内検索
{"src": "revealjs/plugin/search/search.js", "name": "RevealSearch"}
# ズーム
{"src": "revealjs/plugin/zoom/zoom.js", "name": "RevealZoom"}
```

## ハイライトCSSテーマ (`revealjs_css_files`)

highlight.jsはJS側でコード構造を解析するのみで、色付けはCSSテーマが担当する。CSSテーマを読み込まないとハイライトは視覚的に反映されない。

```python
revealjs_css_files = [
    "revealjs/plugin/highlight/monokai.css",  # ダーク背景
]
```

同梱テーマ: `monokai.css`（ダーク背景）、`zenburn.css`（ダーク背景・低コントラスト）

## 表示領域の最適化

### スライド幅の調整

Reveal.jsのデフォルトスライド幅は960pxで、ワイドスクリーンでは左右に余白が生まれる。`revealjs_script_conf`の`width`で調整する。

```python
revealjs_script_conf = {
    "width": 1200,   # デフォルト: 960
    "height": 700,   # デフォルト: 700
}
```

### コードブロックの幅最大化（SCSS）

Reveal.jsベーステーマの`pre`はデフォルトで`width: 90%`、`margin: auto`が設定されている。コンテンツ領域を最大化するには以下を上書きする:

```scss
.reveal {
  .slides section {
    padding: 10px;  // デフォルト: 20px程度
  }

  pre {
    width: 100%;
    margin-left: 0;
    margin-right: 0;
    box-sizing: border-box;
  }
}
```

## Mermaidダイアグラム（sphinxcontrib-mermaid）

### サーバーサイドレンダリング必須

`mermaid_output_format = "raw"`（クライアントサイドレンダリング）は使用禁止。Reveal.jsは非表示スライドのDOM要素を隠すため、Mermaidがテキスト寸法を測定できずレイアウト計算が失敗する。

必ず `mermaid_output_format = "svg"` でビルド時にSVGを事前生成する。

```python
# conf.py
mermaid_output_format = "svg"
mermaid_cmd = ["npx", "-y", "@mermaid-js/mermaid-cli@latest"]
mermaid_params = ["-b", "transparent"]
```

### object タグの CSS 制約

SVGモードでは `<object>` タグでSVGが埋め込まれる。サイズ制約用のCSSは**テーマSCSSとは別のCSSファイル**に記述し、`revealjs_css_files` で読み込む。テーマSCSS内の `object` セレクタはブラウザのCSSパーサーに無視される場合がある。

```css
/* _static/mermaid-fix.css */
.reveal .slides section > object {
  display: block;
  max-height: 500px;
  width: 100%;
  margin: 0 auto;
}
```

```python
# conf.py
revealjs_css_files = [
    "revealjs/plugin/highlight/monokai.css",
    "mermaid-fix.css",
]
```

## 設定例

```python
# conf.py — sphinx-revealjs + Mermaid 構成例
revealjs_script_conf = {
    "width": 1200,
    "height": 700,
}
revealjs_css_files = [
    "revealjs/plugin/highlight/monokai.css",
    "mermaid-fix.css",
]
revealjs_script_plugins = [
    {
        "src": "revealjs/plugin/highlight/highlight.js",
        "name": "RevealHighlight",
    },
]

# Mermaid: サーバーサイドSVG生成
mermaid_output_format = "svg"
mermaid_cmd = ["npx", "-y", "@mermaid-js/mermaid-cli@latest"]
mermaid_params = ["-b", "transparent"]
```
