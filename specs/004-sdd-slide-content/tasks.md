# Tasks: SDDスライドコンテンツ作成

**Input**: Design documents from `/specs/004-sdd-slide-content/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

**Tests**: テスト不要（プレゼンテーション制作プロジェクト。検証は `uv run make -C docs revealjs` ビルド成功で行う）

**Organization**: US1（構成と基本コンテンツ）→ US2（情報の正確性）→ US3（実践例）の順で実装。全タスクは `docs/index.md` への編集が中心のため、同一ファイルへの並列編集は行わない。

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup

**Purpose**: 前提条件の確認

- [x] T001 hachimoku リポジトリが `../hachimoku/specs/001-architecture-spec/spec.md` に存在することを確認する
- [x] T002 `uv run make -C docs revealjs` で現在の docs/index.md がビルド成功することを確認する

---

## Phase 2: Foundational (スライド骨格の再構成)

**Purpose**: 既存 docs/index.md を5セクション構成の H1/H2/H3 階層に再構成する。削除・移動・統合の処理を行い、新規スライドのプレースホルダを配置する

**⚠️ CRITICAL**: この骨格が完成するまで個別スライドのコンテンツ作成に進まないこと

- [x] T003 docs/index.md の H1 タイトルを維持し、H2 セクション5つ（「仕様駆動開発(SDD)とは」「SDDのツール」「Spec Kit入門」「実践例」「まとめ」）の骨格を作成する。既存の H2 スライド（セクション区切りなし）を新しい H2 配下の H3 に移動する
- [x] T004 削除対象スライドを docs/index.md から除去する: 「AIとの組み合わせの利点」テーブル、「類似手法との比較」テーブル、「SDDが適している/いない場合」テーブル（内容は T013 で欠点スライドに統合）
- [x] T005 既存スライドを正しいセクションに配置する: 「バイブコーディングガチャ」→ SDD配下 H3、「GitHub Spec Kit紹介」→ Spec Kit入門配下 H3、「Non-Goals」→ Spec Kit入門配下 H3。新規スライドの H3 見出しをプレースホルダとして追加する（data-model.md の全体構造に従う）
- [x] T006 `uv run make -C docs revealjs` でビルドが成功することを確認する

**Checkpoint**: H1/H2/H3 の骨格が完成。全スライドの見出しが配置済み。ビルド成功

---

## Phase 3: User Story 1 - スライド構成と基本コンテンツ (Priority: P1) 🎯 MVP

**Goal**: 5セクション・22枚のスライドに natural-text ルール準拠のコンテンツを記述し、25分の発表に適した分量にする

**Independent Test**: `uv run make -C docs revealjs` でビルドが成功し、全スライドがブラウザで表示される。各スライドのタイトルが15文字以内、箇条書きが25文字以内・6項目以内

### セクション1: 仕様駆動開発(SDD)とは（S-02〜S-06）

- [x] T007 [US1] docs/index.md の「バイブコーディングの課題」スライド（S-02）を H3 で記述する。既存コンテンツをベースに、箇条書き4〜5項目で AIコーディングの課題を提示する。項目に「人間の期待値との共有不足」を含める（outline.txt 参照）
- [x] T008 [US1] docs/index.md に「仕様駆動開発(SDD)とは」スライド（S-03）を H3 で新規作成する。箇条書き3〜4項目で SDD の定義を記述する。出典リンク（GitHub spec-kit spec-driven.md、GitHub Blog）を含める。「コードが仕様に仕える」パワーインバージョン概念を反映する（research.md R-001）
- [x] T009 [US1] docs/index.md の「従来の開発 vs SDD」スライド（S-04）を list-table（2列）で書き直す。Clarification に基づき「仕様を書く過程で曖昧な考えが明確化」「人間自身も要件の曖昧さに気づかない」を従来の課題側に追加する
- [x] T010 [US1] docs/index.md の「レシピと料理で例えると」スライド（S-05）の list-table を確認・調整する。既存コンテンツを維持し、natural-text ルール（25文字以内）への準拠を確認する
- [x] T011 [US1] docs/index.md の「SDDの基本フロー」スライド（S-06）の ASCII art フローチャートを mermaid flowchart TD ディレクティブに変換する。5ステップ（Specify→Plan→Tasks→Implement→Review）にラベルを付ける

### セクション2: SDDのツール（S-07）

- [x] T012 [US1] docs/index.md に「SDDのツール紹介」スライド（S-07）を list-table（3列: ツール名、特徴、対応エージェント）で新規作成する。Spec Kit・Kiro・cc-sdd の3ツールを記載する。Kiro は「Anthropic Claude搭載」とする（research.md R-005）。各ツールに公式サイトリンクを付ける

### セクション3: Spec Kit入門（S-08〜S-17）

- [x] T013 [US1] docs/index.md の「GitHub Spec Kit紹介」スライド（S-08）を list-table（2列）で書き直す。リリース時期を「2025年8月公開」とし（research.md R-004）、リポジトリ URL を記載する。対応エージェントは代表的なものを列挙する
- [x] T014 [US1] docs/index.md の「Spec Kitのワークフロー」スライド（S-09）の ASCII art を mermaid flowchart で書き直す。8ステップ（Constitution→Specify→Clarify→Plan→Tasks→Analyze→Implement→Tasks to Issues）を表示する。「各ステップでテンプレートを自動生成」の説明テキストを付ける
- [x] T015 [US1] docs/index.md に Spec Kit 各ステップのスライド（S-10〜S-16）を H3 で新規作成する。Constitution・Specify・Clarify・Plan・Tasks・Analyze・Implement の7枚を、各スライド箇条書き2〜3項目 + `specify <command>` コードブロック（5行以下）で記述する。outline.txt の各ステップの説明を参考にする
- [x] T016 [US1] docs/index.md の「Non-Goalsの重要性」スライド（S-17）を確認・調整する。「AIは省略から推論できない」の説明と Markdown コードブロック例（5行以下のためインライン許容）を維持する

### セクション5: まとめ（S-21〜S-23）

- [x] T017 [US1] docs/index.md の「SDDの欠点と注意点」スライド（S-21）を list-table（3列: 初期コスト、コンテキスト消費、仕様の品質）で書き直す。Clarification に基づき「コンテキスト消費」列を新規追加する。削除した「適している/いない場合」の要点（中〜大規模に適し、探索的プロトタイピングには不向き）をテーブル下の1行テキストとして統合する
- [x] T018 [US1] docs/index.md の「まとめ」スライド（S-22）の list-table を確認・調整する。natural-text ルール（25文字以内）への準拠を確認する
- [x] T019 [US1] docs/index.md の「参考リンク」スライド（S-23）を更新する。Spec Kit・Kiro・cc-sdd のツールリンクと、GitHub Blog・Birgitta Böckeler 記事のリンクを掲載する
- [x] T020 [US1] `uv run make -C docs revealjs` でビルドが成功することを確認する。ブラウザで全スライドが表示されることを検証する

**Checkpoint**: 全22枚のスライドにコンテンツが記述済み。ビルド成功。mermaid ダイアグラムと list-table が正しく描画される

---

## Phase 4: User Story 2 - 信頼できる情報に基づく解説 (Priority: P1)

**Goal**: 用語・概念の解説が一次情報に基づき正確であること。出典ハイパーリンクが機能すること。専門用語に入門者向けの平易な説明が添えられていること

**Independent Test**: スライド内の出典リンクをたどり、原文と照合して正確性を検証可能

- [x] T021 [US2] docs/index.md の SDD 定義スライド（S-03）の説明が GitHub spec-kit `spec-driven.md` の原文と整合していることを確認する。パワーインバージョン概念の記述を原文と照合し、必要に応じて修正する
- [x] T022 [US2] docs/index.md の「従来の開発 vs SDD」スライド（S-04）に「仕様を書く過程で曖昧な考えが明確化」が含まれていることを確認する（Acceptance Scenario US2-2）
- [x] T023 [US2] docs/index.md のツール紹介スライド（S-07）の各ツール情報が公式サイトと整合していることを確認する。Kiro の説明が「Anthropic Claude搭載」であること、cc-sdd の対応エージェント数（8種）が正確であることを検証する
- [x] T024 [US2] docs/index.md の「SDDの欠点と注意点」スライド（S-21）が Birgitta Böckeler の批判的分析を参考にしていることを確認する（Acceptance Scenario US2-3）。出典リンク（martinfowler.com）が機能することを検証する
- [x] T025 [US2] docs/index.md の全スライドを通読し、専門用語（SDD、パワーインバージョン、Constitution、Non-Goals 等）の初出時に入門者向けの平易な説明が添えられていることを確認する（Constitution 原則I、Acceptance Scenario US2-4）。不足している場合は補足を追加する
- [x] T026 [US2] docs/index.md の全出典ハイパーリンクが正しい URL であることを確認する。リンク先の情報と記述内容が整合していることを検証する
- [x] T027 [US2] `uv run make -C docs revealjs` でビルドが成功することを確認する

**Checkpoint**: 全出典リンクが正確。専門用語に平易な説明が付与済み。一次情報との整合性を検証済み

---

## Phase 5: User Story 3 - 実践例によるSDD体験 (Priority: P2)

**Goal**: hachimoku プロジェクトの仕様書を literalinclude で表示し、仕様間の依存関係を mermaid ダイアグラムで可視化する

**Independent Test**: hachimoku の仕様書抜粋がスライドに正しく表示され、依存関係図が描画されていることを目視確認で検証可能

- [x] T028 [US3] docs/index.md の「hachimokuプロジェクト」スライド（S-18）を H3 で新規作成する。箇条書き3〜4項目でプロジェクト概要を記述し、リポジトリ URL（github.com/drillan/hachimoku）を記載する
- [x] T029 [US3] docs/index.md の「仕様書の例」スライド（S-19）に literalinclude ディレクティブで `../../hachimoku/specs/001-architecture-spec/spec.md` から User Story 1 + Acceptance Scenarios を抜粋表示する。`:language: markdown` と `:lines:` または `:start-after:` / `:end-before:` オプションで表示範囲を限定する（FR-014）
- [x] T030 [US3] docs/index.md の「仕様間の依存関係」スライド（S-20）に mermaid graph TD ディレクティブで hachimoku の仕様間依存関係図を作成する。hachimoku/specs/README.md の依存関係（002→003, 002→004, 003→005, 004→005, 005→006）を簡略化して表示する。「6つの子仕様が親仕様を分担」の説明テキストを付ける
- [x] T031 [US3] `uv run make -C docs revealjs` でビルドが成功することを確認する。literalinclude の抜粋が正しく表示され、mermaid ダイアグラムが描画されることを検証する

**Checkpoint**: hachimoku 仕様書の抜粋が表示される。依存関係ダイアグラムが描画される。ビルド成功

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: natural-text ルール準拠の最終確認、README.md 作成、最終ビルド検証

- [x] T032 docs/index.md の全スライドを通読し、natural-text ルール準拠を最終確認する。タイトル15文字以内、箇条書き25文字以内・6項目以内、テーブル3列以内、コード10行以下。違反箇所があれば修正する
- [x] T033 [P] README.md にスライドで利用・参照・参考にした情報（リンク等）をまとめる（FR-015）。一次情報（spec-kit、Wikipedia、Birgitta Böckeler 記事、GitHub Blog）、ツール（Spec Kit、Kiro、cc-sdd）、実践例（hachimoku）のリンクを含める
- [x] T034 `uv run make -C docs revealjs` で最終ビルドを実行し、全スライドがブラウザで正しく表示されることを確認する

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **US1 (Phase 3)**: Depends on Foundational completion
- **US2 (Phase 4)**: Depends on US1 completion（コンテンツが存在しないと検証できない）
- **US3 (Phase 5)**: Depends on Foundational completion（US1 とは独立だが、同一ファイル編集のため US1 完了後に実施）
- **Polish (Phase 6)**: Depends on US1, US2, US3 all complete

### User Story Dependencies

- **US1 (P1)**: Foundational 完了後に開始。他の US に依存しない
- **US2 (P1)**: US1 完了後に開始（コンテンツの正確性を検証するため、コンテンツが先に必要）
- **US3 (P2)**: US1 完了後に開始（同一ファイル編集の競合を避けるため）

### Within Each User Story

- セクション順に記述（セクション1→2→3→5 for US1, セクション4 for US3）
- 各セクション内は data-model.md のスライド順（S-02→S-03→...）
- ビルド確認はフェーズ末に1回

### Parallel Opportunities

- T001 と T002 は並列実行可能（異なるチェック対象）
- T033（README.md）は T032（natural-text チェック）と並列実行可能（異なるファイル）
- 同一ファイル（docs/index.md）への編集タスクは並列化不可

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup（前提確認）
2. Complete Phase 2: Foundational（骨格再構成）
3. Complete Phase 3: User Story 1（全セクションのコンテンツ）
4. **STOP and VALIDATE**: ビルド成功、全スライド表示、natural-text 準拠
5. この時点でテキストのみの発表が可能（MVP）

### Incremental Delivery

1. Setup + Foundational → 骨格完成
2. US1 → 全スライドにコンテンツ → ビルド成功（MVP）
3. US2 → 出典の正確性を検証・強化 → 信頼性向上
4. US3 → hachimoku 実践例を追加 → 実物表示
5. Polish → natural-text 最終チェック、README.md → 完成

---

## Notes

- 全タスクの主要編集対象は `docs/index.md`（単一ファイル）
- ビルド確認コマンド: `uv run make -C docs revealjs`
- MyST 記法ルール: `.claude/skills/myst/SKILL.md` に準拠
- natural-text ルール: `.claude/skills/natural-text/SKILL.md` に準拠
- 一次情報: research.md の R-001〜R-010 を参照
- スライド構造: data-model.md を参照
- hachimoku 仕様書パス: `../../hachimoku/specs/001-architecture-spec/spec.md`（docs/ からの相対パス）
