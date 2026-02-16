# Feature Specification: スライドCSS仕様

**Feature Branch**: `002-slide-css-spec`
**Created**: 2026-02-16
**Status**: Draft
**Input**: User description: "SKILL.md / docs/**/*.css / docs/conf.py をもとにスライドCSSの仕様を策定"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - SCSSソースを編集してスライドのデザインを変更する (Priority: P1)

発表者がスライドの見た目を調整したいとき、SCSSソースファイルを編集してビルドすると、変更がスライドに反映される。どのSCSS変数・セレクタを変更すればどの要素に影響するかが仕様として明確になっている。

**Why this priority**: スライドCSS仕様の中核。発表者が安全にデザインをカスタマイズするための前提条件となる。

**Independent Test**: SCSSの任意の変数を変更し、`uv run make -C docs revealjs` でビルドして、出力CSSに変更が反映されることを確認する。

**Acceptance Scenarios**:

1. **Given** SCSS変数 `$mainColor` を変更した状態, **When** ビルドを実行する, **Then** 出力CSSの `--r-main-color` が変更後の値になる
2. **Given** 存在しないSCSS変数を参照した状態, **When** ビルドを実行する, **Then** ビルドエラーが発生し、エラー箇所が報告される
3. **Given** SCSSファイルに構文エラーがある状態, **When** ビルドを実行する, **Then** ビルドエラーが発生し、エラー箇所と行番号が報告される

---

### User Story 2 - タイポグラフィ設定を把握する (Priority: P2)

発表者がフォントサイズや行間を調整したいとき、仕様書のタイポグラフィ定義を参照することで、各要素のフォント設定と推奨値を把握できる。

**Why this priority**: 日本語スライドではフォントと行間の選択が可読性に大きく影響する。

**Independent Test**: 仕様書のタイポグラフィ定義と実際のSCSS設定を照合し、全要素の設定が記載されていることを確認する。

**Acceptance Scenarios**:

1. **Given** 仕様書のタイポグラフィ定義, **When** 見出し・本文・コード・リストの各設定を確認する, **Then** フォントファミリ・サイズ・行間・字間がすべて記載されている
2. **Given** 日本語テキストを含むスライド, **When** ブラウザで表示する, **Then** `word-break: auto-phrase` により自然な位置で改行される

---

### User Story 3 - コードブロックの表示仕様を確認する (Priority: P2)

発表者がコードを含むスライドを作成するとき、コードブロックの表示領域・フォントサイズ・最大高さなどの仕様を参照して、スライドに収まるコード量を事前に見積もれる。

**Why this priority**: 技術系プレゼンではコードブロックの見やすさが情報伝達の鍵。

**Independent Test**: コードブロックを含むスライドをビルドし、仕様書の表示設定どおりにレンダリングされることを確認する。

**Acceptance Scenarios**:

1. **Given** コードブロックを含むスライド, **When** ビルドして表示する, **Then** コードブロックが幅100%で表示され、左右マージンが0である
2. **Given** 長いコードブロックを含むスライド, **When** ビルドして表示する, **Then** 最大高さ560pxでスクロール可能になる

---

### Edge Cases

- SCSSテンプレート (`template/mixins`, `template/settings`, `template/theme`) のバージョンが変わった場合、カスタムSCSSとの互換性に影響がある
- Google Fontsの読み込みに失敗した場合、フォントはフォントスタック内の次候補（Hiragino Kaku Gothic ProN → Noto Sans JP → sans-serif）に遷移する
- 印刷時 (`@media print`) のスタイルが画面表示と異なる場合がある

## Requirements *(mandatory)*

### Functional Requirements

#### タイポグラフィ

- **FR-001**: スライドの本文フォントは `Zen Kaku Gothic New` を第一候補とし、`Hiragino Kaku Gothic ProN`・`Noto Sans JP` を次候補とすること
- **FR-002**: コード表示フォントは `Source Code Pro` を使用すること
- **FR-003**: 各要素のフォントサイズは以下のとおりとすること: h1（2.0em）、h2（1.6em）、h3（1.3em）、本文（36px）、コードブロック（0.5em）、インラインコード（0.85em）
- **FR-004**: 行間は以下のとおりとすること: 本文（1.6）、リスト（1.8）、コードブロック（1.4em）
- **FR-005**: 日本語テキストは `word-break: auto-phrase` で自然な位置で改行し、字間は本文 `0.04em`・見出し `0.06em` とすること

#### レイアウト

- **FR-006**: スライドの表示領域は幅1200px、高さ700pxとすること
- **FR-007**: スライドのパディングは10pxとすること（Reveal.jsデフォルトの20pxから縮小）
- **FR-008**: コードブロックは幅100%・左右マージン0・`box-sizing: border-box`・角丸6px・最大高さ560pxとすること
- **FR-009**: インラインコードは背景色 `rgba($base01, 0.08)`・パディング `0.1em 0.3em`・角丸3pxとすること
- **FR-010**: 引用ブロックは左ボーダー4px（cyan色）・背景色 `rgba($base2, 0.5)`・角丸 `0 6px 6px 0` とすること
- **FR-011**: テーブルはフォントサイズ・セル余白・ボーダー色をカスタム定義すること（list-tableディレクティブで生成されるテーブルに適用）

#### ビルドパイプライン

- **FR-012**: SCSSソースファイルは `docs/_sass/` に配置すること
- **FR-013**: ビルド後のCSSは `docs/_static/` に出力されること
- **FR-014**: ビルドは `uv run make -C docs revealjs` で実行できること
- **FR-015**: sphinx-revealjsのSASS自動ビルド設定（`revealjs_sass_auto_targets = True`）により、SCSSファイルの追加時に手動設定が不要であること

#### SCSS構造

- **FR-016**: SCSSファイルは以下の順序で構成すること: (1) Sassモジュールインポート、(2) テンプレートインポート、(3) Google Fontsインポート、(4) カラー変数定義、(5) テーマ変数オーバーライド、(6) テーマテンプレート適用、(7) カスタムオーバーライド
- **FR-017**: カスタムスタイルはテーマテンプレート適用後に配置し、CSS詳細度（specificity）でベーステーマを上書きすること

### Key Entities

- **テーマ変数**: Reveal.jsテーマテンプレートが認識するSCSS変数群（$mainFont, $mainColor, $backgroundColor等）。テンプレートがCSS変数 (`--r-*`) に変換する。カラーパレットの定義はテーマに委譲する
- **カスタムオーバーライド**: テーマテンプレート適用後に追加するCSS。日本語最適化やコードブロック調整など、ベーステーマでは対応できないスタイルを定義する
- **SCSSビルドパイプライン**: `docs/_sass/*.scss` → sphinx-revealjs SASS拡張 → `docs/_static/*.css` → スライドHTML

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: ビルドされたスライドのフォント・サイズ・行間が仕様のタイポグラフィ定義と一致する（DevToolsのComputed Stylesで検証可能）
- **SC-002**: ビルドされたスライドのレイアウト（表示領域・パディング・コードブロック幅等）が仕様どおりにレンダリングされる（目視およびCSS値の検証で確認可能）
- **SC-003**: SKILL.mdを参照することで、SCSS変数やカスタムスタイルの追加箇所を5分以内に特定できる

## Clarifications

### Session 2026-02-16

- Q: この仕様の成果物は何か → A: ビルドされたスライド（`docs/_build/revealjs`）が最終成果物。SKILL.mdはそれを実現するための補助的な位置づけ
- Q: テーブルのスタイルは仕様に含めるか → A: 含める（フォントサイズ・余白・ボーダー色を定義）
- Q: FR-001「全16色を使用」の精度 → A: 色設定の仕様は不要。カラーパレットはテーマに委譲する

## Assumptions

- Solarized Lightカラーパレットは変更されない前提で仕様を定義する
- フォントの読み込みにはGoogle Fonts CDNを使用する。オフライン環境ではフォントファイルをローカルに配置する運用が別途必要
- Reveal.jsのバージョンはsphinx-revealjs 3.2+に同梱されるものを使用する
- SCSSテンプレート (`template/mixins`, `template/settings`, `template/theme`) はReveal.jsの公式テンプレートを使用する
