# Spec Kitではじめる仕様駆動開発入門

みんなのPython勉強会#120

2026-02-12

## 仕様駆動開発(SDD)とは

### バイブコーディングの課題

- AIが書くコードの品質にばらつき
- 余計な機能の追加や意図と異なる実装
- 人間とAIでコンテキスト共有が不足
- 仕様書との「答え合わせ」手段の不在

### 仕様駆動開発(SDD)とは

コードより先に仕様書を書く開発手法

- 仕様書が唯一の情報源
- コードは仕様の表現にすぎない
- 仕様がコードに仕えるのでなく、コードが仕様に仕える

出典: [spec-driven.md - GitHub spec-kit](https://github.com/github/spec-kit/blob/main/spec-driven.md)

### 従来の開発 vs SDD

:::{list-table}
:header-rows: 1
:widths: auto

* - 従来の課題
  - SDD
* - 人間自身も要件の曖昧さに気づかない
  - 仕様を書く過程で曖昧な考えが明確化
* - 仕様書を書いても実装中に乖離が発生
  - 仕様書からコードを生成
* - コードが真実の源泉になりがち
  - 仕様変更でコードも更新
:::

### レシピと料理で例えると

:::{list-table}
:header-rows: 1
:widths: auto

* - 曖昧なレシピ
  - 詳細なレシピ
  - AIも同じ
* - 「塩少々」「適量」「いい感じに」
  - 分量・手順・火加減がすべて明確
  - 明確な仕様 → 期待通りの実装
* - → 作る人によって味にばらつき
  - → 誰が作っても同じ味を再現可能
  - 曖昧な指示 → ガチャ結果
:::

### SDDの欠点と注意点

:::{list-table}
:header-rows: 1
:widths: auto

* - 初期コスト
  - コンテキスト消費
  - 仕様の品質
* - - 仕様書作成に工数が必要
    - 小規模・試作には過剰
  - - 仕様・計画・タスクでトークンを消費
    - エージェントの作業領域が圧迫される
  - - 未熟な仕様で誤った実装を量産
    - レビューとイテレーションが必須
:::

中〜大規模や複数人開発に適し、探索的プロトタイピングには不向き

参考: [Understanding SDD - Birgitta Böckeler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)

### SDDの基本フロー

:::{mermaid}
flowchart TD
  A["Specify<br>何を作るか明確化"] --> B["Clarify<br>曖昧な箇所を洗い出す"]
  B --> C["Plan<br>どう作るか設計"]
  C --> D["Tasks<br>実装単位に分解"]
  D --> E["Implement<br>AIエージェントが実装"]
  E --> F["Review<br>受け入れ基準で検証"]
  F --> A
:::

## SDDのツール

### SDDのツール

- Spec Kit
- Kiro
- cc-sdd

### Spec Kit

GitHubが提供するオープンソースのSDDツールキット

- テンプレートとプロンプトで仕様管理
- clarify/analyzeで仕様の品質検証

<https://github.com/github/spec-kit>

### Kiro

AWS開発のエージェント型IDE

- Hooksでファイル保存時に自動実行
- 画像からの実装にも対応

<https://kiro.dev/>

### cc-sdd

コミュニティ製のSDDツール

- Kiro互換の仕様フォーマット
- 13言語のプロンプトに対応

<https://github.com/gotalab/cc-sdd>

## Spec Kit入門

### Spec Kitのワークフロー

:::{mermaid}
flowchart LR
  Z[Constitution]
  A[Specify] --> B[Clarify]
  B --> C[Plan]
  C --> D[Tasks]
  D --> E[Analyze]
  E --> F[Implement]
  E -.->|optional| G[Tasks to Issues]
:::

各ステップでテンプレートとプロンプトを自動生成

### Constitution

Constitution = プロジェクトの「憲法」

プロジェクトの不変の原則を定義する

- すべての仕様・コードの判断基準
- 例: DRY原則に従う

```bash
/speckit.constitution
```

### Specify

自然言語で機能仕様を記述する

- 漠然としたアイデアを自動的に明確化
- ユーザーストーリーと受け入れ基準
- 機能要件と主要エンティティ
- 測定可能な成功基準

```bash
/speckit.specify GitHub issueに自動応答するボットを作って
```

### spec.mdの構成

:::{list-table}
:header-rows: 1
:widths: auto

* - セクション
  - 内容
* - User Scenarios & Testing
  - ユーザー視点の利用シナリオと受け入れ基準
* - Functional Requirements
  - システムが満たすべき機能要件
* - Key Entities
  - 主要なデータ・概念の定義
* - Success Criteria
  - 測定可能な成功基準
:::

### Clarify

仕様の曖昧な箇所を質問形式で洗い出す

- 最大5つの質問を自動生成
- 見落としがちな仕様の矛盾も検出
- 回答を仕様書に反映

例: 「リトライする」という記述に対し
→ 「エクスポネンシャルバックオフ」などの選択肢を提供

```bash
/speckit.clarify
```

### Plan

技術計画を策定する

- データモデルとAPIコントラクトを設計
- リサーチで技術的な不明点を解消

```bash
/speckit.plan
```

### Tasks

計画を小さな実装タスクに分割する

- Setup→実装→Polishのフェーズ構成
- ユーザーストーリー単位で独立実行可能

```bash
/speckit.tasks
```

### Analyze

仕様・計画・タスクの整合性をチェックする

- 6カテゴリで矛盾や漏れを検出
- 読み取り専用で修正提案のみ出力

```bash
/speckit.analyze
```

### Implement

タスクに基づきAIエージェントが実装する

- テスト→実装の順序でコード生成
- タスク完了ごとに仕様と照合

```bash
/speckit.implement
```

### Tasks to Issues

タスクをGitHub Issueに変換する

- tasks.mdから依存関係順にissueを作成
- リモートがGitHubならMCP serverなどで投稿

```bash
/speckit.taskstoissues
```

### speckit-gates

各ステップに品質ゲートを自動追加するコミュニティ製スキル

- 計画・実装・ドキュメントを自動検証
- GREEN/YELLOW/REDで品質を可視化

```bash
npx skills add drillan/speckit-gates
```

<https://github.com/drillan/speckit-gates>

### speckit-gatesのスキル

:::{list-table}
:header-rows: 1
:widths: auto

* - スキル
  - トリガー
  - 内容
* - planning-validate
  - /speckit.plan後に自動
  - 計画成果物の整合性を検証
* - implementation-verify
  - /speckit.implement後に自動
  - 実装カバレッジを確認
* - docs-sync
  - /speckit.implement後に自動
  - ドキュメントの同期
* - progress-report
  - 手動実行
  - 進捗ダッシュボードを表示
* - release-check
  - 手動実行
  - リリース前の総合チェック
:::

## 実践例

### hachimokuプロジェクト

マルチエージェントコードレビューツール

- 6種のレビューエージェントを搭載
- diff・PR・ファイル単位でレビュー実行
- TOMLによるレビューエージェントのカスタマイズ
- Spec Kitで仕様を管理し段階的に開発

<https://github.com/drillan/hachimoku>

### hachimokuでセルフレビュー

このスライドも5種のカスタムエージェントで品質チェック

:::{literalinclude} ../.hachimoku/agents/natural-text-reviewer.toml
:language: toml
:end-before: system_prompt
:::

<https://github.com/drillan/stapy120/blob/main/.hachimoku/agents/natural-text-reviewer.toml>

### レビュー結果

5エージェントが指摘を自動検出

:::{literalinclude} _static/slides-review-sample.md
:language: text
:start-after: "## Issues"
:end-before: "```"
:::

<https://github.com/drillan/stapy120/blob/main/docs/_static/slides-review-sample.md>

### 仕様書の例: User Story

ユーザー視点の利用シナリオを優先度付きで記述

:::{rli} https://raw.githubusercontent.com/drillan/hachimoku/refs/heads/main/specs/001-architecture-spec/spec.md
:language: markdown
:start-after: "## User Scenarios & Testing *(mandatory)*"
:end-before: "**Acceptance Scenarios**:"
:::

出典: [hachimoku/specs/001-architecture-spec/spec.md](https://github.com/drillan/hachimoku/blob/main/specs/001-architecture-spec/spec.md)

### 仕様書の例: 受け入れ基準

Given/When/Then形式でテスト可能な基準を定義

:::{rli} https://raw.githubusercontent.com/drillan/hachimoku/refs/heads/main/specs/001-architecture-spec/spec.md
:language: markdown
:start-after: "Markdown 形式で stdout に表示される"
:end-before: "3. **Given** 変更差分にクラス定義"
:::

→ AIが「合格/不合格」を自動判定可能

出典: [hachimoku/specs/001-architecture-spec/spec.md](https://github.com/drillan/hachimoku/blob/main/specs/001-architecture-spec/spec.md)

### 仕様書の例: 機能要件

FR-XXX形式で機能要件を一意に識別

:::{rli} https://raw.githubusercontent.com/drillan/hachimoku/refs/heads/main/specs/001-architecture-spec/spec.md
:language: markdown
:start-after: "glob パターンをサポートする。Git リポジトリ外でも動作可能とする"
:end-before: "- **FR-006**:"
:::

→ 番号付きで要件の追跡と相互参照が可能

出典: [hachimoku/specs/001-architecture-spec/spec.md](https://github.com/drillan/hachimoku/blob/main/specs/001-architecture-spec/spec.md)

## Spec KitのTips

### 仕様作成前のブレインストーミング

`/speckit.specify` の前にアイデアを整理する

:::{list-table}
:header-rows: 1
:widths: auto

* - ツール
  - 特徴
* - [Feature Development](https://github.com/anthropics/claude-code/tree/main/plugins/feature-dev)
  - コードベース探索とアーキテクチャ設計
* - [Superpowers](https://github.com/obra/superpowers)
  - 対話型のアイデア深掘りと設計文書化
* - [Deep Trilogy](https://github.com/piercelamb/deep-plan)
  - 大規模アイデアのコンポーネント分解
:::

### 仕様の分割

:::::{list-table}
:header-rows: 0
:widths: 50 50

* - - 大規模プロジェクトは仕様を分割してスコープを小さくする
    - 例: 機能ごとに仕様を分割
  - :::{mermaid}
    graph TD
      002[002-domain-models] --> 003[003-agent-definition]
      002 --> 004[004-configuration]
      003 --> 005[005-review-engine]
      004 --> 005
      005 --> 006[006-cli-interface]
    :::
:::::

### 仕様書の文量が多い

`/speckit.specify` の直後にAIに質問する

- わからないこと
- 自分が気になるポイント

AIが説明し、不明確な点を明確化

### Tasks to Issuesの活用

そのままだと大量のissueが作られる

- 適切な粒度にまとめる
- 関連ドキュメントもissueに含める

```bash
/speckit.taskstoissues 適切な粒度に分類し、関連するドキュメントのリファレンスを必ずつけてください
```

## まとめ

### まとめ

:::{list-table}
:header-rows: 1
:widths: auto

* - バイブコーディングを卒業
  - 仕様書が真実の源泉
  - Spec Kitで始めよう
* - - 明確な仕様でAIをコントロール
    - 「ガチャ」から「レシピ」へ
  - - What（何を）とHow（どう）の分離
    - 仕様変更でコードも再生成
  - - GitHubのオープンソースツール
    - AI Agent非依存で始めやすい
:::

## おまけ

このスライド自体もSpec Kitで作成

### 4つの仕様で構築

:::::{list-table}
:header-rows: 0
:widths: 50 50

* - - 001: ビルド基盤の構築
    - 002: CSSテーマの設計
    - 003: MyST記法ルールの策定
    - 004: スライド内容の作成
  - :::{mermaid}
    graph TD
      001[001-slides-setup] --> 002[002-slide-css]
      001 --> 003[003-myst-rules]
      002 --> 004[004-slide-content]
      003 --> 004
    :::
:::::

### タイポグラフィ仕様

具体的な値で定義すればAIが同じCSSを再現

:::{literalinclude} ../specs/002-slide-css-spec/spec.md
:language: markdown
:start-after: "#### タイポグラフィ"
:end-before: "#### レイアウト"
:::

<https://github.com/drillan/stapy120/blob/main/specs/002-slide-css-spec/spec.md>

### テーブル記法の仕様

禁止パターンの明示でAIの記法選択を統一

:::{literalinclude} ../specs/003-myst-notation-rules/spec.md
:language: markdown
:start-after: "#### テーブル"
:end-before: "#### コード取り込み"
:::

<https://github.com/drillan/stapy120/blob/main/specs/003-myst-notation-rules/spec.md>
