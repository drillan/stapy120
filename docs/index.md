# Spec Kitではじめる仕様駆動開発入門

みんなのPython勉強会#120

2026-02-12

## バイブコーディングガチャ

- AIが書くコードの品質にばらつき
- 余計な機能の追加
- 意図と異なる機能の実装
- 一見よさそうだが、微妙に異なる挙動

## 仕様駆動開発（SDD）とは

**従来の課題**

- 仕様書を書いても、実装中に乖離が発生
- コードが真実の源泉になる傾向

**SDD: Specification-Driven Development**

- 仕様書 ⇒ コード（仕様書からコードが生成される）
- 仕様書を変更すればコードも更新
- **「仕様書が真実の源泉」**

## レシピと料理で例えると

**曖昧なレシピ**

- 「塩少々」「適量」「いい感じに」
- → 作る人によって味にばらつき

**詳細なレシピ**

- 分量・手順・火加減がすべて明確
- → 誰が作っても同じ味を再現可能

**AIも同じ**

- 明確な仕様 → 期待通りの実装
- 曖昧な指示 → ガチャ結果

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

**明確な仕様 → AIの推測や曖昧さを排除**

- 「ログイン機能を作って」→ 曖昧な実装
- 詳細仕様 → 正確な実装

**意図と実装の分離**

- What（何を）: 仕様書に記述
- How（どうやって）: AIが最適な実装を選択

**仕様変更時に再生成可能**

- 生きたドキュメント
- ドキュメントとコードの乖離を解消

## GitHub Spec Kit紹介

**GitHubが提供するSDDツールキット**

- 2025年9月リリース
- オープンソース

**AI Agent非依存**

- Claude Code
- GitHub Copilot
- Gemini CLI
- Cursor / Windsurf

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

## 仕様書の例（Taskify）

```markdown
# Taskify Specification

## 1. Product Overview
チーム生産性プラットフォーム

## 2. Core Features
- プロジェクト管理
- チームコラボレーション
- カンバンボード

## 3. Technical Specifications
- API Endpoints
- Data Model（TypeScript型定義）

## 4. Non-Goals ← 重要！
- モバイルアプリは現フェーズでは対象外
- リアルタイム通知は後フェーズ
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

**初期コストがかかる**

- 仕様書作成に工数が必要
- 小規模・試作には過剰

**仕様の品質が成功の鍵**

- 未熟な仕様 → 誤った実装の効率的な量産
- レビューとイテレーションが必須

**銀の弾丸ではない**

- プロジェクトの性質を考慮して選択

## SDDが適している/いない場合

**適している**

- 中〜大規模プロジェクト
- 複数人でのコラボレーション
- AI活用を前提とした開発
- 要件が比較的明確

**適していない**

- 極小規模（個人の小さなスクリプト）
- 探索的プロトタイピング
- 要件が極めて不明確な初期段階

## 類似手法との比較

| 手法 | 開始点 | 焦点 | AI親和性 |
|------|--------|------|---------|
| TDD | テスト | 品質検証 | 中 |
| BDD | 振る舞い記述 | ユーザー視点 | 中 |
| SDD | 仕様書 | AI自動化 | 最高 |

SDDはTDD/BDDと**対立しない**

- SDD: 「何を」「なぜ」を定義
- TDD: 「どのように」を検証

組み合わせて使える

## まとめ

**バイブコーディングを卒業しよう**

- 明確な仕様でAIをコントロール
- 「ガチャ」から「レシピ」へ

**仕様書が真実の源泉**

- What（何を）とHow（どうやって）の分離
- 仕様変更→再生成で対応

**Spec Kitで始めてみよう**

- GitHubが提供するオープンソースツール
- AI Agent非依存で始めやすい

## 参考リンク

**GitHub Spec Kit**

https://github.com/github/spec-kit

**関連記事**

- [Spec-driven development with AI - GitHub Blog](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
- [Understanding SDD: Kiro, spec-kit, and Tessl - Martin Fowler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
