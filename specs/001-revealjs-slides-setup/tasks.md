# Tasks: Reveal.jsスライド生成・公開基盤

**Input**: Design documents from `/specs/001-revealjs-slides-setup/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, quickstart.md

**Tests**: テスト未要求のため、テストタスクは含めない

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

**Note**: US1（ローカルビルド）とUS3（カスタムテーマ）は既に実装済み。検証タスクのみ含む。US2（GitHub Pagesデプロイ）が主要な新規実装作業。

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: 既存インフラの健全性確認

- [x] T001 既存のビルド環境が動作することを確認する: `uv run make -C docs revealjs` を実行し、`docs/_build/revealjs/index.html` が生成されることを検証する

**Checkpoint**: ビルド環境が正常に動作する状態

---

## Phase 2: User Story 1 - ローカルでスライドをビルドする (Priority: P1) — 実装済み・検証のみ

**Goal**: MyST記法のMarkdownからReveal.jsスライドをローカルでビルドし、プレビューできる

**Independent Test**: `uv run make -C docs revealjs` を実行し、生成されたHTMLをブラウザで開いてスライドとして表示されることを確認する

**Status**: FR-001〜FR-005, FR-008はすべて実装済み。以下の検証で完了を確認する。

### 検証 for User Story 1

- [x] T002 [US1] `docs/conf.py` でsphinx-revealjs、myst_parser、sphinx_revealjs.ext.sass拡張が有効であることを確認する
- [x] T003 [US1] `docs/conf.py` でMyST Parser拡張機能（colon_fence、deflist、tasklist）が設定されていることを確認する
- [x] T004 [US1] `pyproject.toml` でsphinx、sphinx-revealjs、myst-parser、libsassの依存関係が定義されていることを確認する
- [ ] T005 [US1] ビルド成果物 `docs/_build/revealjs/index.html` をブラウザで開き、スライドが表示されページ送りで遷移できることを確認する

**Checkpoint**: User Story 1 の全受け入れシナリオが満たされている

---

## Phase 3: User Story 2 - GitHub Pagesでスライドを公開する (Priority: P2) — 新規実装

**Goal**: mainブランチへのプッシュで自動的にスライドがビルドされ、GitHub Pagesに公開される

**Independent Test**: mainブランチへのプッシュ後、GitHub PagesのURLにアクセスしてスライドが表示されることを確認する

### Implementation for User Story 2

- [x] T006 [US2] `.github/workflows/deploy.yml` を新規作成する: トリガー（push to main, workflow_dispatch）、権限（contents: read, pages: write, id-token: write）、並行実行制御（concurrency group: pages）を設定する
- [x] T007 [US2] `.github/workflows/deploy.yml` のbuildジョブを実装する: actions/checkout@v6、astral-sh/setup-uv@v7（enable-cache: true）、uv python install 3.13、uv sync --locked、uv run make -C docs revealjs、actions/configure-pages@v5、actions/upload-pages-artifact@v4（path: docs/_build/revealjs）
- [x] T008 [US2] `.github/workflows/deploy.yml` のdeployジョブを実装する: actions/deploy-pages@v4、environment: github-pages、needs: build
- [ ] T009 [US2] GitHubリポジトリのSettings > Pages > SourceをGitHub Actionsに設定する（手動操作）
- [ ] T010 [US2] mainブランチにプッシュし、GitHub Actionsワークフローが正常に実行されることを確認する
- [ ] T011 [US2] GitHub PagesのURL（`https://drillan.github.io/stapy120/`）にアクセスし、スライドが表示されることを確認する

**Checkpoint**: User Story 2 の全受け入れシナリオが満たされている

---

## Phase 4: User Story 3 - カスタムテーマでスライドを表示する (Priority: P3) — 実装済み・検証のみ

**Goal**: 日本語最適化されたカスタムSolarizedテーマがスライドに適用される

**Independent Test**: ビルドしたスライドでカスタムテーマが適用され、日本語テキストが読みやすく表示されることを視覚的に確認する

**Status**: FR-005は実装済み。`docs/_sass/custom-solarized.scss` が既に存在し、日本語フォント・行間・文字間隔が設定済み。

### 検証 for User Story 3

- [x] T012 [US3] `docs/_sass/custom-solarized.scss` が存在し、Zen Kaku Gothic Newフォント、行間1.6、文字間隔0.04emが設定されていることを確認する
- [x] T013 [US3] ビルド成果物にカスタムテーマCSS（`docs/_build/revealjs/_static/custom-solarized.css`）が生成されていることを確認する
- [ ] T014 [US3] ブラウザでスライドを表示し、日本語フォントが適用され適切な行間・文字間隔で表示されることを視覚的に確認する

**Checkpoint**: User Story 3 の全受け入れシナリオが満たされている

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: 全体の整合性確認

- [ ] T015 GitHub Pages上のスライドでカスタムテーマが正しく適用されていることを確認する（US2 + US3の統合検証）
- [ ] T016 `specs/001-revealjs-slides-setup/quickstart.md` の手順に従い、ゼロからビルド・デプロイできることを検証する

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: 依存なし — 即座に開始可能
- **US1 検証 (Phase 2)**: Phase 1完了後 — 既存実装の検証のみ
- **US2 実装 (Phase 3)**: Phase 1完了後 — 新規実装。US1検証と並行可能
- **US3 検証 (Phase 4)**: Phase 1完了後 — US1検証と並行可能
- **Polish (Phase 5)**: Phase 2, 3, 4すべて完了後

### User Story Dependencies

- **User Story 1 (P1)**: 実装済み。検証のみ。他ストーリーに依存しない
- **User Story 2 (P2)**: 新規実装。ローカルビルド（US1）が動作する前提だが、US1は実装済みのため即座に着手可能
- **User Story 3 (P3)**: 実装済み。検証のみ。他ストーリーに依存しない

### Parallel Opportunities

- T002, T003, T004 は異なるファイルの確認のため並行実行可能
- T012, T013 は異なるファイルの確認のため並行実行可能
- Phase 2（US1検証）とPhase 4（US3検証）は並行実行可能
- Phase 3（US2実装）のT006, T007, T008は同一ファイルのため順次実行

---

## Implementation Strategy

### MVP First (User Story 2 のみ)

1. Phase 1完了: ビルド環境確認
2. Phase 3完了: `.github/workflows/deploy.yml` を作成しデプロイ確認
3. **STOP and VALIDATE**: GitHub PagesでスライドがHTMLとして表示されることを確認
4. 残りのPhase（検証タスク）を実施

### 推奨実行順序

1. T001（ビルド確認）
2. T006 → T007 → T008（deploy.yml作成 — 同一ファイルのため順次）
3. T009（GitHub Pages設定 — 手動）
4. T010 → T011（デプロイ検証 — 順次）
5. T002〜T005, T012〜T014（既存実装の検証 — 並行可能）
6. T015 → T016（統合検証）

---

## Notes

- 全16タスク中、新規実装は3タスク（T006, T007, T008 = deploy.yml作成）のみ
- 残りは検証タスク（既存実装の確認）と手動操作（T009）
- T009はGitHubの管理画面での手動操作が必要
- テストタスクは仕様で未要求のため含めない
