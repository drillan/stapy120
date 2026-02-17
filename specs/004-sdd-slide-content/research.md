# Research: SDDスライドコンテンツ

## 調査項目一覧

### R-001: SDD の定義と「パワーインバージョン」概念

- **Decision**: GitHub spec-kit リポジトリの `spec-driven.md` を正式な定義元として採用
- **Rationale**: Constitution 原則II で指定された一次情報源であり、GitHub 公式の定義文書である
- **Alternatives considered**: GitHub Blog 記事（二次的な紹介記事）、Wikipedia（歴史的概要）

**確認済み定義**:

> "Spec-Driven Development (SDD) inverts this power structure. Specifications don't serve code -- code serves specifications." — spec-driven.md

> "The specification becomes the primary artifact. Code becomes its expression in a particular language and framework."

スライドでは「仕様書がコードに仕えるのではなく、コードが仕様書に仕える」（パワーインバージョン）として紹介する。

### R-002: SDD の学術的起源

- **Decision**: 2004年の学術論文を起源として引用する
- **Rationale**: Wikipedia の Spec-driven development 記事に基づく（Constitution 原則IIの一次情報リスト）
- **Alternatives considered**: 起源に触れない（歴史的文脈が失われる）

**確認済み情報**:

- 原論文: Ostroff, J.S., Makalsky, D., and Paige, R.F. (2004) "Agile Specification-Driven Development", XP 2004
- TDD（テスト駆動開発）と DbC（契約による設計）の融合として学術的に定式化
- 2020年代にLLMエージェントの台頭で「ルネサンス」を迎えた

**スライドでの扱い**: SDD定義スライドの補足として「2004年にTDDとDbCの融合として学術的に定式化」と記載。スライド上では論文詳細までは不要（時間制約）。

### R-003: Martin Fowler サイトの批判的分析

- **Decision**: 著者を正確に「Birgitta Böckeler（Thoughtworks）」として引用する
- **Rationale**: 記事はMartinFowler.comに掲載されているが、著者はBirgitta Böckeler（Distinguished Engineer at Thoughtworks）。正確な帰属が必要
- **Alternatives considered**: 「Martin Fowler」と簡略化する（不正確になる）

**確認済み批判ポイント**:

1. **問題規模への不適合**: 小さなバグ修正に「4つのユーザーストーリーと16の受け入れ基準」が生成される過剰さ
2. **ドキュメント負担**: Markdownファイルの大量生成は冗長になりうる
3. **エージェントの制御限界**: 精巧なワークフローにもかかわらず、エージェントが指示を無視するケースあり

**スライドでの扱い**: 「まとめ」セクションのSDDの欠点・注意点で参考情報として活用。出典リンクを明記。

### R-004: GitHub spec-kit のワークフローと対応エージェント

- **Decision**: 8ステップのワークフローと代表的な対応エージェントを紹介する
- **Rationale**: spec-kit README.md のAvailable Slash Commandsセクションで確認済み
- **Alternatives considered**: 全17エージェントを列挙する（スライド分量超過）

**確認済みワークフロー（9ステップ）**:

1. Constitution — プロジェクトの基本原則を定義
2. Specify — 要件とユーザーストーリーを定義
3. Clarify — 曖昧な箇所を質問形式で洗い出し
4. Plan — 技術実装計画を策定
5. Tasks — タスクリストを生成
6. Analyze — 成果物間の整合性チェック
7. Implement — タスクに基づき実装を実行
8. Checklist — 品質チェックリストを生成
9. Tasks to Issues — タスクをGitHub Issueに変換

**注意**: spec-kit README の slash command テーブルには Checklist / Tasks to Issues の記載がないが、`.claude/commands/` に `speckit.checklist.md` と `speckit.taskstoissues.md` が存在する。スライドでは仕様（FR-007）に記載の8ステップ（Constitution〜Tasks to Issues、Checklist を除く）を採用する。

**対応エージェント**: 17種類以上（Claude Code, GitHub Copilot, Gemini CLI, Cursor, Windsurf 等）。スライドでは代表的なものを紹介し「他多数」と記載。

**リリース時期**: リポジトリ作成 2025年8月21日、v0.0.1 リリース 2025年8月22日、GitHub Blog 発表 2025年9月2日。スライドでは「2025年8月公開」とする。

### R-005: Kiro の特徴

- **Decision**: 「AWS開発のエージェント型IDE、Anthropic Claude搭載」として紹介する
- **Rationale**: Kiro は独自AIエンジンではなく Anthropic Claude モデルを使用している。Agent Hooks が差別化機能
- **Alternatives considered**: 「独自AIエンジン搭載」（不正確）

**確認済み情報**:

- 開発元: AWS
- 使用モデル: Anthropic Claude Sonnet 3.7 / Claude 4.0
- パブリックプレビュー: 2025年7月14日
- GA（一般提供）: 2025年11月17日
- 主要機能: EARS記法による要件定義、Agent Hooks（ファイル保存時等の自動タスク実行）、Steering Files
- 3ドキュメント構造: `requirements.md`, `design.md`, `tasks.md`

**アウトラインからの修正**: 「独自AIエンジン搭載」→「Anthropic Claude搭載」に修正。差別化ポイントは「エージェント型IDE」「Agent Hooks自動化」。

### R-006: cc-sdd の特徴

- **Decision**: 「Kiro互換のコミュニティ製SDDツール、8エージェント対応」として紹介する
- **Rationale**: cc-sdd README.md で確認済み
- **Alternatives considered**: 詳細機能を列挙する（スライド時間制約）

**確認済み情報**:

- 開発元: gotalab（日本のコミュニティ）
- Kiroスタイルのワークフロー互換実装
- 対応エージェント（8種）: Claude Code, Cursor, Gemini CLI, Codex CLI, GitHub Copilot, Qwen Code, OpenCode, Windsurf
- ワークフロー: `spec-init` → `spec-requirements` → `spec-design` → `spec-tasks` → `spec-impl`
- 13言語対応（日本語含む）

### R-010: Tessl のスコープ判定

- **Decision**: スライドに含めない（スコープ外）
- **Rationale**: Tessl はエージェント向けスキル・コンテキストのレジストリ管理プラットフォームであり、「仕様を書いてコーディングエージェントに実装させる」SDDワークフローとは焦点が異なる。入門者向け25分発表では Spec Kit・Kiro・cc-sdd の3ツールに絞る
- **Alternatives considered**: ツール紹介テーブルに4行目として追加（情報密度が上がり入門者には過剰）、参考リンクにのみ記載（発表テーマとの関連性が薄い）

### R-007: 既存スライドの再構成方針

- **Decision**: 仕様書のClarificationsに基づき、既存スライドを再構成する
- **Rationale**: spec.md のQ&Aで明確化済み
- **Alternatives considered**: 全面書き直し（既存の有用なコンテンツが失われる）

**再構成ルール**:

| 既存スライド | 判定 | 理由 |
|---|---|---|
| バイブコーディングガチャ | 移動 | H2「仕様駆動開発(SDD)とは」配下のH3に移動 |
| 仕様駆動開発（SDD）とは | 再構成 | 従来 vs SDD テーブルに「曖昧な思考の明確化」を追加 |
| レシピと料理で例えると | 残す | そのまま（入門者向けたとえ話） |
| SDDの基本フロー | 残す | ASCII art → mermaid に変換 |
| AIとの組み合わせの利点 | **削除** | Clarification で削除指示 |
| GitHub Spec Kit紹介 | 移動 | H2「Spec Kit入門」配下に移動 |
| Spec Kitのワークフロー | 再構成 | 8ステップに拡充、ASCII art → mermaid |
| CLIコマンド例 | 統合 | 各ステップの説明スライドにコマンドを組み込む |
| 仕様書の例 | 移動 | H2「実践例」に移動、hachimoku仕様書に差し替え |
| Non-Goals | 残す | H2「Spec Kit入門」配下に移動 |
| SDDの欠点・注意点 | 再構成 | コンテキスト消費を追加、適している/いない場合を統合 |
| SDDが適している/いない場合 | **統合** | 欠点・注意点スライドに統合 |
| 類似手法との比較 | **削除** | Clarification で削除指示 |
| まとめ | 残す | 微修正 |
| 参考リンク | 再構成 | Kiro, cc-sdd を追加 |

### R-008: hachimoku リポジトリの literalinclude 対象

- **Decision**: `001-architecture-spec/spec.md` の User Story 1 + Acceptance Scenarios を抜粋表示する
- **Rationale**: User Story + Given/When/Then 形式が SDD の具体的な成果物として最もわかりやすい
- **Alternatives considered**: Feature Specification タイトル部分（情報量が少ない）、Requirements セクション（長すぎる）

**表示対象行**: spec.md の行35〜50付近（User Story 1 の定義から Acceptance Scenarios まで）
**パス**: `../../hachimoku/specs/001-architecture-spec/spec.md`（docs/ からの相対パス）

### R-009: 仕様間依存関係のダイアグラム

- **Decision**: hachimoku/specs/README.md の mermaid 図を参考に、簡略化したダイアグラムをスライド用に作成する
- **Rationale**: README.md に graph TD 形式の依存関係図が既に存在する
- **Alternatives considered**: literalinclude で README.md の mermaid 部分を取り込む（Sphinx での mermaid in literalinclude は非対応）

**元の依存関係**: 002→003, 002→004, 002→005, 003→005, 004→005, 005→006, 005→008（8仕様、007 含む）

**スライド用の簡略化**: 6つの子仕様が親仕様のユーザーストーリーを分担する構造を、主要な依存フローとして表示する。
