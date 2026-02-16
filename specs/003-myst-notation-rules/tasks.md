# Tasks: MyST記法ルールの拡充

**Input**: Design documents from `/specs/003-myst-notation-rules/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md

**Tests**: テスト不要（ルール文書の更新のため）。ビルド検証でSC-003を確認する。

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup

**Purpose**: Mermaidダイアグラム対応に必要な依存追加とSphinx拡張設定

- [x] T001 [P] Add `sphinxcontrib-mermaid>=2.0.0` to dependencies in pyproject.toml
- [x] T002 [P] Add `sphinxcontrib.mermaid` to extensions list in docs/conf.py

---

## Phase 2: Foundational

**Purpose**: 全ユーザーストーリーに共通する前提変更

**⚠️ CRITICAL**: SKILL.mdのfrontmatterと一般ルールは全セクションに影響するため、ストーリー実装前に完了すること

- [x] T003 Update frontmatter `description` field to include Mermaid・Admonition・定義リスト in .claude/skills/myst/SKILL.md
- [x] T004 Add colon fence統一ルール（FR-016: `:::`をディレクティブ囲みに使用）to 構文の注意点 section in .claude/skills/myst/SKILL.md

**Checkpoint**: frontmatterとcolon fenceルールが反映され、各ストーリーのセクション追加準備完了

---

## Phase 3: User Story 1 - ダイアグラム（Mermaid） (Priority: P1) 🎯 MVP

**Goal**: `:::{mermaid}` ディレクティブのルールをSKILL.mdに定義し、ASCIIアートフローチャートの禁止パターンを明示する

**Independent Test**: SKILL.mdのダイアグラムセクションのみを参照して `:::{mermaid}` でflowchartを記述し、`uv run make -C docs revealjs` でビルドが通ることを確認

### Implementation for User Story 1

- [x] T005 [US1] Add ## ダイアグラム section with basic `:::{mermaid}` syntax and flowchart example in .claude/skills/myst/SKILL.md
- [x] T006 [US1] Add 推奨ダイアグラムタイプ一覧（flowchart, sequenceDiagram, stateDiagram-v2, gantt, classDiagram）and note that other types are also allowed in .claude/skills/myst/SKILL.md
- [x] T007 [US1] Add オプション subsection（name for cross-reference, caption, align）with FR-004 clarification（label optional unless cross-referencing）in .claude/skills/myst/SKILL.md
- [x] T008 [US1] Add 禁止パターン subsection with ASCIIアート flowchart example（罫線文字 `┌─┐→↓`）in .claude/skills/myst/SKILL.md
- [x] T009 [US1] Run build verification: `uv run make -C docs revealjs` to confirm mermaid directive works

**Checkpoint**: Mermaidダイアグラムルールが完成。SKILL.mdを参照してMermaid記法で図を作成できる状態

---

## Phase 4: User Story 2 - テーブルとコード取り込み (Priority: P2)

**Goal**: コードの取り込みセクションにFR-009 clarification（5行以下のインライン許容）を反映する。テーブルセクションは変更なし

**Independent Test**: SKILL.mdのコード取り込みセクションを参照して、5行以下と6行以上のコードを正しく判別できることを確認

### Implementation for User Story 2

- [x] T010 [US2] Update 禁止パターン subsection in コードの取り込み section to add 5行閾値ルール and 許容パターン example in .claude/skills/myst/SKILL.md

**Checkpoint**: テーブル・コード取り込みルールが最新仕様を反映

---

## Phase 5: User Story 3 - Admonition (Priority: P3)

**Goal**: Admonitionディレクティブ（note, tip, warning, important, seealso）のルールをSKILL.mdに定義する

**Independent Test**: SKILL.mdのAdmonitionセクションを参照して `:::{note}` を記述し、ビルドでスタイル付きボックスとして表示されることを確認

### Implementation for User Story 3

- [x] T011 [US3] Add ## Admonition section with basic `:::{note}` syntax and custom title syntax（`:::{admonition} タイトル` + `:class:`）in .claude/skills/myst/SKILL.md
- [x] T012 [US3] Add 使用可能なタイプ subsection listing note, tip, warning, important, seealso with usage guidance in .claude/skills/myst/SKILL.md
- [x] T013 [US3] Add 禁止パターン subsection（plain text「注意:」「ヒント:」）and コンテンツ量ガイドライン（1〜3行）in .claude/skills/myst/SKILL.md

**Checkpoint**: Admonitionルールが完成。5種のタイプを使い分けてコンテンツを強調できる状態

---

## Phase 6: User Story 4 - 定義リスト (Priority: P3)

**Goal**: 定義リスト（deflist）構文のルールをSKILL.mdに定義する

**Independent Test**: SKILL.mdの定義リストセクションを参照して `用語\n: 定義` 構文で記述し、ビルドで `<dl>` 要素としてレンダリングされることを確認

### Implementation for User Story 4

- [x] T014 [US4] Add ## 定義リスト section with basic syntax（`用語\n: 定義`）and multiple definitions example in .claude/skills/myst/SKILL.md
- [x] T015 [US4] Add 禁止パターン subsection（箇条書きで定義リストを代用するパターン）in .claude/skills/myst/SKILL.md

**Checkpoint**: 定義リストルールが完成。用語説明を構造化された形式で記述できる状態

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: 全体整合性の確認とビルド検証

- [x] T016 Run full build verification: `uv run make -C docs revealjs` to confirm all directives work (SC-003)
- [x] T017 Verify SKILL.md line count is under 400 lines (plan constraint) — 321 lines
- [x] T018 Verify all rule categories covered (SC-001): テーブル, コード取り込み, ダイアグラム, Admonition, 定義リスト, 一般
- [x] T019 Verify each rule has both 正しい記法 and 禁止パターン examples (SC-002)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion (T001, T002 must complete before T003, T004)
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories are sequential (all edit the same file: SKILL.md)
  - Priority order: US1 → US2 → US3 → US4
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2). Requires sphinxcontrib-mermaid from Setup
- **User Story 2 (P2)**: Can start after US1 (same file, sequential edits)
- **User Story 3 (P3)**: Can start after US2 (same file, sequential edits)
- **User Story 4 (P3)**: Can start after US3 (same file, sequential edits)

### Parallel Opportunities

- T001 and T002 can run in parallel (different files: pyproject.toml, conf.py)
- Story phases are sequential due to single-file constraint (SKILL.md)
- Polish tasks T016-T019 are sequential (validation must be ordered)

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001, T002)
2. Complete Phase 2: Foundational (T003, T004)
3. Complete Phase 3: User Story 1 - Mermaid (T005-T009)
4. **STOP and VALIDATE**: Mermaidルールが動作し、ASCIIアートの代替として使用可能か確認
5. この時点でMermaid対応という最大価値が実現

### Incremental Delivery

1. Setup + Foundational → 基盤準備完了
2. US1（Mermaid） → ビルド検証 → MVP完了
3. US2（コード取り込み更新） → 既存ルールが最新化
4. US3（Admonition） → 情報強調手段が追加
5. US4（定義リスト） → 用語構造化手段が追加
6. Polish → 全体検証完了

---

## Notes

- 全ストーリーが同一ファイル（SKILL.md）を編集するため、並列実行は不可
- 各ストーリーのCheckpointでビルド検証を推奨（問題の早期発見）
- T009のビルド検証はMermaid固有の問題を検出するため、MVP段階で必須
- 各セクションはplan.mdのSKILL.mdセクション構成に従うこと
