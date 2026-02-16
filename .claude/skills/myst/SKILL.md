---
name: myst
description: MyST記法のルール。(1) パイプテーブルではなくlist-tableディレクティブを使用する。(2) 太字見出し＋箇条書きの複数グループはlist-tableに変換する。(3) コードブロックは外部ファイルからliteralincludeで取り込む。MyST/Sphinxのマークダウンを生成するときに適用する。
---

# MyST 記法ルール

## テーブル

- パイプテーブル（`| col1 | col2 |` 形式）は使用禁止
- テーブルは必ず `:::{list-table}` ディレクティブで記述する

### list-table の書式

```
:::{list-table}
:header-rows: 1
:widths: auto

* - ヘッダ1
  - ヘッダ2
* - データ1
  - データ2
:::
```

### 必須オプション

- `:header-rows:` を必ず指定する（ヘッダ行がない場合は `0`）
- `:widths: auto` を基本とする（明示的な幅指定が必要な場合のみ整数列を使用）

### 利用可能なオプション

- `:align:` — `left` / `center` / `right`
- `:header-rows:` — ヘッダ行数（デフォルト: 0）
- `:stub-columns:` — スタブ列数（デフォルト: 0）
- `:width:` — テーブル全体の幅（長さまたはパーセント）
- `:widths:` — 列幅の比率（整数列または `auto`）
- `:class:` — CSSクラス
- `:name:` — 参照用ターゲット名

## 箇条書きグループの表化

太字見出し＋箇条書きのグループが複数並ぶパターンは `list-table` に変換する。各グループの見出しをヘッダ行、箇条書きをセル内の箇条書きとして配置する。

### 禁止パターン

```
**カテゴリA**

- 項目1
- 項目2

**カテゴリB**

- 項目3
- 項目4
```

### 正しい記法

```
:::{list-table}
:header-rows: 1
:widths: auto

* - カテゴリA
  - カテゴリB
* - - 項目1
    - 項目2
  - - 項目3
    - 項目4
:::
```

### セル内箇条書きの構文

- `* - - item` は「行開始 → セル開始 → 箇条書き項目」の3段ネスト
- 同一セル内の後続項目は `    - item`（4スペースインデント）

## コードの取り込み

外部ファイルとして存在するコードはインラインコードブロックではなく `literalinclude` で取り込む。

### 基本書式

```
:::{literalinclude} path/to/file.py
:language: python
:::
```

パスはドキュメントファイルからの相対パス。`/` 始まりはソースディレクトリのルートからの相対パス。

### 主要オプション

- `:language:` — シンタックスハイライトの言語
- `:lines:` — 行範囲の指定（例: `1-5`, `1,3,5-10`）
- `:start-after:` — 指定テキストの後から取り込み開始
- `:end-before:` — 指定テキストの前で取り込み終了
- `:emphasize-lines:` — 強調表示する行（例: `3,5-7`）
- `:linenos:` — 行番号を表示
- `:caption:` — キャプション
- `:pyobject:` — 特定のPythonオブジェクトを抽出
- `:dedent:` — インデントを除去する文字数

### 禁止パターン

ファイルとして存在するコードをインラインで記述してはならない:

````
```python
def hello():
    print("Hello")
```
````

### 正しい記法

```
:::{literalinclude} examples/hello.py
:language: python
:::
```

部分的に取り込む場合:

```
:::{literalinclude} examples/hello.py
:language: python
:start-after: # start example
:end-before: # end example
:::
```

## 構文の注意点

- `* -` は新しい行（row）の開始
- `  -`（インデント付きハイフン）は列（column）の値
- セル内に複数行のコンテンツを含める場合はインデントを揃える
