---
name: sphinx-revealjs
description: sphinx-revealjsの設定ルール。(1) Reveal.jsプラグインはUMDバンドル版を使用する。(2) ハイライトにはCSSテーマの読み込みが必須。(3) スライド幅はrevealjs_script_confで調整する。(4) Mermaidダイアグラムはsphinx-oceanidによるクライアントサイド遅延レンダリング。(5) スライドの左右分割にはlist-tableを使用する。sphinx-revealjsのconf.pyやスライドを編集するときに適用する。
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

## Mermaidダイアグラム（sphinx-oceanid）

### クライアントサイド遅延レンダリング

sphinx-oceanid は beautiful-mermaid（ELK.js ベースレイアウト）によるクライアントサイドレンダリングを使用する。Reveal.js の非表示スライド問題は IntersectionObserver と `slidechanged` イベントによる遅延レンダリングで自動的に解決される。

conf.py に `"sphinx_oceanid"` を追加するだけで動作し、追加設定は不要。

```python
# conf.py
extensions = [
    "sphinx_oceanid",
    "sphinx_revealjs",
    # ...
]
```

### サーバーサイドレンダリング関連の設定は不要

sphinx-oceanid では以下の設定・ファイルは不要:

- `mermaid_output_format`, `mermaid_cmd`, `mermaid_params` 等の `mermaid_*` 設定
- `puppeteer-config.json`（Puppeteer は使用しない）
- `mermaid-config.json`（beautiful-mermaid がテーマを内包）
- `mermaid-fix.css`（`<object>` タグは使用しない）
- CIでの日本語フォントインストール（クライアントサイドレンダリングのため閲覧者のブラウザ環境に依存）

### SVGの高さ制約

sphinx-oceanid のSVGはデフォルトで `height: auto` のため、縦方向に長いダイアグラム（`flowchart TD` 等）がスライドからはみ出す。`_static/oceanid-revealjs.css` で `max-height` を設定し、`revealjs_css_files` で読み込む。

```css
/* _static/oceanid-revealjs.css */
.reveal .slides .oceanid-diagram .oceanid-svg-container svg {
  max-height: 500px;
}
```

```python
# conf.py
revealjs_css_files = [
    "revealjs/plugin/highlight/monokai.css",
    "oceanid-revealjs.css",
]
```

## スライドの左右分割レイアウト

1スライドに収まりきらない場合、`list-table` で左右に分割する。

### 用途

- ページに収まりきらない場合
- 説明と図を並べたい場合
- 複数のトピックを比較したい場合

### 書式

コロンフェンスの数を変えてディレクティブをネストする（外側`:::::`、内側`:::`）。

```
:::::{list-table}
:header-rows: 0
:widths: 50 50

* - 左カラムの内容
  - :::{mermaid}
    flowchart LR
      A --> B
    :::
:::::
```

`:widths:` で左右の比率を調整する（例: `60 40` で左を広く）。

### 左カラムに箇条書きを配置する場合

セルの先頭を箇条書きにする場合、`* - -` の3段ネスト構文を使う。

```
:::::{list-table}
:header-rows: 0
:widths: 50 50

* - - 箇条書き項目1
    - 箇条書き項目2
  - :::{mermaid}
    flowchart LR
      A --> B
    :::
:::::
```

## 設定例

```python
# conf.py — sphinx-revealjs + sphinx-oceanid 構成例
extensions = [
    "myst_parser",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.sass",
    "sphinx_oceanid",
]

revealjs_script_conf = {
    "width": 1200,
    "height": 700,
}
revealjs_css_files = [
    "revealjs/plugin/highlight/monokai.css",
]
revealjs_script_plugins = [
    {
        "src": "revealjs/plugin/highlight/highlight.js",
        "name": "RevealHighlight",
    },
]
# sphinx-oceanid は追加設定不要（Reveal.jsビルダーを自動検出）
```
