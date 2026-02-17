# Feature Specification: SDDスライドコンテンツ作成

**Feature Branch**: `004-sdd-slide-content`
**Created**: 2026-02-16
**Status**: Draft
**Input**: User description: "work/outline.txtの内容をもとにスライド内容docs/index.mdの仕様を策定"

## 背景と目的

「みんなのPython勉強会#120」で発表する「Spec Kitではじめる仕様駆動開発入門」のスライドコンテンツを `docs/index.md` に作成する。`work/outline.txt` で定義された構成案を正式なスライドとして仕上げる。

MyST記法のルールは `specs/003-myst-notation-rules` に準拠する。本仕様ではスライドの構成・内容・情報の正確性を定義する。

## Clarifications

### Session 2026-02-16

- Q: 既存の index.md を置き換えるか、ベースにして再構成するか？ → A: 既存ベースで再構成する
- Q: アウトラインにない既存スライドはどうするか？ → A: レシピの例え・SDDの基本フロー・SDDの欠点と注意点は残す。AIとの組み合わせの利点・類似手法との比較は削除。適している/いない場合は欠点と注意点に統合
- Q: SDDのツール紹介の粒度は？ → A: 簡単な特徴も記載する
- Q: Spec Kit実践例で何を見せるか？ → A: hachimokuリポジトリの仕様書をliteralincludeで表示
- Q: テーブルの列数上限は？ → A: 3列以内（003-myst-notation-rules FR-008a に反映済み）
- Q: SDDの定義の情報源は？ → A: GitHub Blog を一次情報として出典リンクを明記
- Q: 見出しレベルの仕様は？ → A: H1がタイトル、H2がセクション区切り（5つ）、H3が個別スライド
- Q: SDDの欠点にコンテキスト消費を含めるか？ → A: 含める
- Q: 人間の曖昧な思考の明確化をどこに入れるか？ → A: 「従来の開発 vs SDD」テーブルに追加

## User Scenarios & Testing *(mandatory)*

### User Story 1 - スライド構成と基本コンテンツ (Priority: P1)

発表者が `docs/index.md` を開くと、5セクション構成のスライドが完成しており、`uv run make -C docs revealjs` でビルドして Reveal.js スライドとして表示できる。各スライドの文言は natural-text ルールに準拠し、25分の発表に適した分量である。

**Why this priority**: スライドの構成とテキストコンテンツがなければ発表できない。最小限のMVPとしてテキストだけで発表可能。

**Independent Test**: `uv run make -C docs revealjs` でビルドが成功し、全スライドがブラウザで表示されることで検証可能。

**Acceptance Scenarios**:

1. **Given** `docs/index.md` が存在する状態, **When** ビルドを実行, **Then** H1タイトル + H2セクション5つ + H3個別スライドが表示される
2. **Given** 任意のスライドを表示した状態, **When** 文字数・項目数を確認, **Then** natural-text ルール（タイトル15文字以内、箇条書き6項目以内・25文字以内）に準拠している
3. **Given** スライド全体を通して確認した状態, **When** 発表時間を見積もる, **Then** 25分の発表に適した分量である（Constitution原則IV）

---

### User Story 2 - 信頼できる情報に基づく解説 (Priority: P1)

聴衆がスライドを見ると、解説が必要な用語や概念（SDD、Spec Kit、Kiro、cc-sdd、Non-Goals等）が一次情報またはそれに類する信頼できる情報に基づいて正確に説明されている。出典はハイパーリンクで確認可能であり、入門者にもわかりやすいたとえ話や対比で補強されている。

**Why this priority**: Constitution原則II「一次情報の尊重」の中核要件。新しい概念を紹介する発表において、情報の正確性は信頼の土台である。

**Independent Test**: スライド内の用語・概念の説明について、出典リンクをたどり原文と照合して正確性を検証可能。

**Acceptance Scenarios**:

1. **Given** 用語や概念を解説するスライドを表示した状態, **When** 内容を確認, **Then** 一次情報または信頼できる情報に基づく説明が記載され、出典ハイパーリンクが機能する
2. **Given** SDDの利点を説明するスライドを表示した状態, **When** 内容を確認, **Then** 「仕様を書く過程で曖昧な考えが明確化」の利点が従来の課題と対比して示されている
3. **Given** SDDの欠点・注意点スライドを表示した状態, **When** 内容を確認, **Then** Martin Fowler の批判的分析を参考に、欠点が公平に紹介されている
4. **Given** 専門用語が初出するスライドを確認した状態, **When** 説明を確認, **Then** 入門者向けの平易な説明が添えられている（Constitution原則I）

---

### User Story 3 - 実践例によるSDD体験 (Priority: P2)

聴衆が「実践例」セクションを見ると、hachimokuプロジェクトを通じてSDDの具体的な成果物（仕様書・依存関係図）が実物として提示され、「自分もやってみたい」と思える状態になる。

**Why this priority**: Constitution原則III「実践による実証」の中核。理論だけでは行動を促せない。

**Independent Test**: hachimokuの仕様書抜粋がスライドに正しく表示され、依存関係図が描画されていることを目視確認で検証可能。

**Acceptance Scenarios**:

1. **Given** 実践例セクションを表示した状態, **When** 内容を確認, **Then** hachimoku の仕様書から具体的な抜粋が表示される
2. **Given** 仕様間の依存関係を示すスライドを表示した状態, **When** 図を確認, **Then** 子仕様の依存関係がダイアグラムで描画される
3. **Given** 参考リンクスライドを表示した状態, **When** リンクを確認, **Then** 聴衆が即座に始められるツールのURLが掲載されている（Constitution原則V）

---

### Edge Cases

- hachimokuリポジトリがローカルに存在しない場合、ビルドエラーとなること（暗黙的にスキップしない）
- コードブロックが1スライドの許容行数を超える場合、スライドを分割すること
- 箇条書きの文言が25文字を超える場合、文言を短縮すること

## Requirements *(mandatory)*

### Functional Requirements

#### 全体構成

- **FR-001**: `docs/index.md` は H1 でタイトル「Spec Kitではじめる仕様駆動開発入門」を持つこと
- **FR-002**: H2 セクションは以下の5つとすること: 「仕様駆動開発(SDD)とは」「SDDのツール」「Spec Kit入門」「実践例」「まとめ」
- **FR-003**: 個別スライドは H3 で記述し、H4以下は使用しないこと
- **FR-004**: スライド総数は25分の発表に適した分量とすること。literalinclude等で内容を表示するだけのスライドはさらっと流す前提のため、枚数の厳密な上限は設けない

#### セクション別要件

- **FR-005**: 「仕様駆動開発(SDD)とは」（4〜6スライド程度）— バイブコーディングの課題を提示し、SDDの定義・利点を信頼できる一次情報に基づいて説明すること。従来の開発との対比や、入門者向けのたとえ話を含めること。用語・ツールの初出時には公式サイトやリポジトリ等のハイパーリンクを明記すること
- **FR-006**: 「SDDのツール」（1〜2スライド程度）— Spec Kit・Kiro・cc-sdd など主要なSDDツールの特徴と対応エージェントを紹介すること
- **FR-007**: 「Spec Kit入門」（8〜12スライド程度）— Spec Kitの概要と対応エージェントを紹介し、ワークフローの各ステップ（Constitution, Specify, Clarify, Plan, Tasks, Analyze, Implement, Tasks to Issues）をそれぞれ説明すること。各ステップには対応する `specify` コマンドを示すこと
- **FR-008**: 「実践例」（2〜4スライド程度）— hachimokuプロジェクトを紹介し、仕様書の実物を `literalinclude` で抜粋表示すること。仕様間の依存関係をダイアグラムで可視化すること
- **FR-009**: 「まとめ」（2〜4スライド程度）— SDDの欠点・注意点（初期コスト、コンテキスト消費、仕様の品質）を公平に提示し、発表の要点を要約すること。聴衆が始められるよう参考リンクを掲載すること

#### コンテンツ品質

- **FR-010**: MyST記法は `specs/003-myst-notation-rules` に準拠すること
- **FR-011**: 日本語テキストは `.claude/skills/natural-text/SKILL.md` に準拠すること
- **FR-012**: 解説が必要な用語・概念（SDD、Spec Kit、Kiro、cc-sdd等）は一次情報またはそれに類する信頼できる情報に基づいて説明し、出典を示せない主張を含まないこと
- **FR-013**: 専門用語は初出時に平易な説明を添えること
- **FR-014**: `literalinclude` で外部ファイルを埋め込む場合、全体をそのまま表示せず、もっとも重要な行を `:lines:` や `:start-after:` / `:end-before:` で抽出すること
- **FR-015**: スライドで利用・参照・参考にした情報（リンク等）を `README.md` にまとめること

## Non-Goals

- スライドのCSSテーマ変更（002-slide-css-spec で対応済み）
- MyST記法ルールの定義・変更（003-myst-notation-rules で対応済み）
- PDF出力対応
- スピーカーノートの追加
- アニメーション・トランジション効果の設定
- 自己紹介スライドの追加
- hachimoku リポジトリのクローンやサブモジュール化（ローカルに存在する前提）

## Assumptions

- hachimoku リポジトリが `../hachimoku/` の相対パスでアクセス可能
- `sphinxcontrib-mermaid` 拡張が `conf.py` で有効化済み
- Solarized カスタムテーマが適用済み

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `uv run make -C docs revealjs` がエラーなく完了する
- **SC-002**: スライド総数が25分の発表に適した分量である
- **SC-003**: natural-text ルールに全スライドが準拠している
- **SC-004**: SDD定義の出典としてハイパーリンクが機能する
- **SC-005**: hachimoku の仕様書抜粋がスライドに正しく表示される
- **SC-006**: Constitution の5原則に適合している
