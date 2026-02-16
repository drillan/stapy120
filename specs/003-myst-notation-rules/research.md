# Research: MyST記法ルール拡充

## Decision 1: Mermaid用Sphinx拡張

- **Decision**: `sphinxcontrib-mermaid` (v2.0.0) を使用する
- **Rationale**:
  - sphinx-revealjsと完全互換（HTMLビルダーベース）
  - MyST colon fence構文（`:::{mermaid}`）をそのまま使用可能
  - デフォルト設定（`mermaid_output_format = 'raw'`）でJS自動注入・クライアント側レンダリング
  - conf.pyに `'sphinxcontrib.mermaid'` を追加するのみで動作
- **Alternatives considered**:
  - `myst_fence_as_directive = ["mermaid"]`: GitHub互換のコードブロック形式だが、コロンフェンス統一ルール（FR-016）と矛盾する
  - 画像として事前生成（`mermaid_output_format = 'svg'`）: mermaid-cli依存が増える。スライド用途ではJS動的レンダリングで十分

## Decision 2: Admonition対応

- **Decision**: 追加設定不要。myst-parserのcolon_fence拡張で対応済み
- **Rationale**:
  - `myst_enable_extensions = ["colon_fence"]` が有効化済み
  - `:::{note}`, `:::{warning}`, `:::{tip}`, `:::{important}`, `:::{seealso}` がそのまま使える
  - カスタムタイトルは `:::{admonition} タイトル` + `:class: tip` で対応
- **Alternatives considered**: なし（標準機能のため）

## Decision 3: 定義リスト対応

- **Decision**: 追加設定不要。myst-parserのdeflist拡張で対応済み
- **Rationale**:
  - `myst_enable_extensions = ["deflist"]` が有効化済み
  - `用語\n: 定義` 構文がそのまま使える
- **Alternatives considered**: なし（標準機能のため）

## Decision 4: SKILL.mdファイル分割の要否

- **Decision**: 分割しない。1ファイルに統合する
- **Rationale**:
  - 現在140行 + 新規約120行 = 約260行。他のスキルファイル（natural-text: 49行、sphinx-revealjs: 93行）より大きいが、ルールブックとして1ファイルで参照できる利便性が高い
  - Claude Codeのスキルシステムは1スキル=1 SKILL.mdファイル。分割するとスキル記述が複数になり、適用条件が分散する
  - 各セクションはh2見出しで明確に区切られており、ナビゲーションに問題はない
  - 分割の閾値目安: 400行を超えた時点で再検討する
- **Alternatives considered**:
  - カテゴリ別スキル分割（myst-tables, myst-mermaid等）: スキル適用条件が分散し、一部ルールが適用されないリスク
  - メインSKILL.md + 参照ファイル: Claude Codeのスキルシステムがincludeに対応していない
