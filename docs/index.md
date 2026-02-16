# Spec Kitではじめる仕様駆動開発入門

みんなのPython勉強会#120

2026-02-12

## バイブコーディングガチャ

- AIが書くコードの品質にばらつき
- 余計な機能の追加
- 意図と異なる機能の実装
- 一見よさそうだが、微妙に異なる挙動

## 仕様駆動開発（SDD）とは

:::{list-table}
:header-rows: 1
:widths: auto

* - 従来の課題
  - SDD
* - - 仕様書を書いても、実装中に乖離が発生
    - コードが真実の源泉になる傾向
  - - 仕様書 ⇒ コード（仕様書からコードが生成される）
    - 仕様書を変更すればコードも更新
    - **「仕様書が真実の源泉」**
:::

## レシピと料理で例えると

:::{list-table}
:header-rows: 1
:widths: auto

* - 曖昧なレシピ
  - 詳細なレシピ
  - AIも同じ
* - - 「塩少々」「適量」「いい感じに」
    - → 作る人によって味にばらつき
  - - 分量・手順・火加減がすべて明確
    - → 誰が作っても同じ味を再現可能
  - - 明確な仕様 → 期待通りの実装
    - 曖昧な指示 → ガチャ結果
:::

## SDDの基本フロー

```
┌─────────┐
│ Specify │ ← 何を作るか明確化
└────┬────┘
     ↓
┌─────────┐
│  Plan   │ ← どう実装するか設計
└────┬────┘
     ↓
┌─────────┐
│  Tasks  │ ← 小さな実装単位に分解
└────┬────┘
     ↓
┌───────────┐
│ Implement │ ← AIエージェントが実装
└────┬──────┘
     ↓
┌─────────┐
│ Review  │ ← 仕様書と照合して確認
└─────────┘
```

## AIとの組み合わせの利点

:::{list-table}
:header-rows: 1
:widths: auto

* - 明確な仕様 → 推測を排除
  - 意図と実装の分離
  - 仕様変更時に再生成可能
* - - 「ログイン機能を作って」→ 曖昧な実装
    - 詳細仕様 → 正確な実装
  - - What（何を）: 仕様書に記述
    - How（どうやって）: AIが最適な実装を選択
  - - 生きたドキュメント
    - ドキュメントとコードの乖離を解消
:::

## GitHub Spec Kit紹介

:::{list-table}
:header-rows: 1
:widths: auto

* - GitHubが提供するSDDツールキット
  - AI Agent非依存
* - - 2025年9月リリース
    - オープンソース
  - - Claude Code
    - GitHub Copilot
    - Gemini CLI
    - Cursor / Windsurf
:::

https://github.com/github/spec-kit

## Spec Kitのワークフロー

```
Constitution（不変の原則）
      ↓
   Specify（仕様作成）
      ↓
    Plan（技術計画）
      ↓
   Tasks（タスク分割）
      ↓
  Implement（実装）
      ↓
     PR（プルリクエスト）
```

各ステップでチェックリスト・テンプレート・プロンプトを自動生成

## CLIコマンド例

```bash
# プロジェクト初期化
specify init

# 仕様作成
specify spec

# 技術計画生成
specify plan

# タスク分割
specify tasks
```

Markdown形式で仕様を管理し、Gitでバージョン管理

## 仕様書の例

```{literalinclude} ../specs/001-revealjs-slides-setup/spec.md
:language: markdown
```

## Non-Goals（非目標）の重要性

**AIは省略から推論できない**

- 書いていないことは「やっていい」と解釈
- スコープ境界の明示的な記述が必要

**例**

```markdown
## Non-Goals
- このフェーズではユーザー認証を実装しない
- モバイル対応は含まない
- 多言語対応は対象外
```

→ AIによる不要な実装の防止

## SDDの欠点・注意点

:::{list-table}
:header-rows: 1
:widths: auto

* - 初期コストがかかる
  - 仕様の品質が成功の鍵
  - 銀の弾丸ではない
* - - 仕様書作成に工数が必要
    - 小規模・試作には過剰
  - - 未熟な仕様 → 誤った実装の効率的な量産
    - レビューとイテレーションが必須
  - - プロジェクトの性質を考慮して選択
:::

## SDDが適している/いない場合

:::{list-table}
:header-rows: 1
:widths: auto

* - 適している
  - 適していない
* - - 中〜大規模プロジェクト
    - 複数人でのコラボレーション
    - AI活用を前提とした開発
    - 要件が比較的明確
  - - 極小規模（個人の小さなスクリプト）
    - 探索的プロトタイピング
    - 要件が極めて不明確な初期段階
:::

## 類似手法との比較

:::{list-table}
:header-rows: 1
:widths: auto

* - 手法
  - 開始点
  - 焦点
  - AI親和性
* - TDD
  - テスト
  - 品質検証
  - 中
* - BDD
  - 振る舞い記述
  - ユーザー視点
  - 中
* - SDD
  - 仕様書
  - AI自動化
  - 最高
:::

SDDはTDD/BDDと**対立しない**

- SDD: 「何を」「なぜ」を定義
- TDD: 「どのように」を検証

組み合わせて使える

## まとめ

:::{list-table}
:header-rows: 1
:widths: auto

* - バイブコーディングを卒業しよう
  - 仕様書が真実の源泉
  - Spec Kitで始めてみよう
* - - 明確な仕様でAIをコントロール
    - 「ガチャ」から「レシピ」へ
  - - What（何を）とHow（どうやって）の分離
    - 仕様変更→再生成で対応
  - - GitHubが提供するオープンソースツール
    - AI Agent非依存で始めやすい
:::

## 参考リンク

**GitHub Spec Kit**

https://github.com/github/spec-kit

**関連記事**

- [Spec-driven development with AI - GitHub Blog](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
- [Understanding SDD: Kiro, spec-kit, and Tessl - Martin Fowler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
