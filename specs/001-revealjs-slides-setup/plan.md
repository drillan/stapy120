# Implementation Plan: Reveal.jsスライド生成・公開基盤

**Branch**: `001-revealjs-slides-setup` | **Date**: 2026-02-16 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-revealjs-slides-setup/spec.md`

## Summary

sphinx-revealjsとMyST記法を使用したスライドビルドパイプラインの整備と、GitHub Actionsを用いたGitHub Pagesへの自動デプロイを構築する。ローカルビルド環境はすでに動作しており、主要な新規作業はGitHub Actionsワークフローの作成である。

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Sphinx 9.1+, sphinx-revealjs 3.2+, myst-parser 5.0+, libsass 0.23+
**Storage**: N/A（静的サイト生成）
**Testing**: ローカルビルド確認 + GitHub Actionsワークフロー実行確認
**Target Platform**: GitHub Pages（静的ホスティング）
**Project Type**: Single（Sphinxドキュメントプロジェクト）
**Performance Goals**: デプロイ完了まで5分以内（SC-002）
**Constraints**: パブリックリポジトリ前提、uv使用必須
**Scale/Scope**: 単一スライドデッキ、1ファイル構成

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| 原則 | 適用範囲 | 判定 | 備考 |
|------|----------|------|------|
| I. 入門者ファースト | コンテンツ仕様の管轄 | N/A | インフラ仕様には直接適用されない |
| II. 一次情報の尊重 | コンテンツ仕様の管轄 | N/A | インフラ仕様には直接適用されない |
| III. 実践による実証 | コンテンツ仕様の管轄 | N/A | ただしビルド基盤がこの原則を支える |
| IV. 25分の構成規律 | コンテンツ仕様の管轄 | N/A | インフラ仕様には直接適用されない |
| V. 体験価値の最大化 | コンテンツ仕様の管轄 | N/A | インフラ仕様には直接適用されない |
| 品質基準: フォント・可読性 | テーマSCSS | PASS | 既存テーマが品質基準のCSS値を実装済み |
| 品質基準: コード例 | テーマSCSS | PASS | `pre { font-size: 0.5em }` 等が実装済み |
| ワークフロー: ビルドコマンド | FR-002 | PASS | `uv run make -C docs revealjs` と一致 |

**Constitution Check Result**: PASS（違反なし）

## Project Structure

### Documentation (this feature)

```text
specs/001-revealjs-slides-setup/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── quickstart.md        # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```text
docs/
├── conf.py              # Sphinx設定 [既存・変更不要]
├── index.md             # スライドソース [既存・コンテンツは別仕様]
├── Makefile             # ビルドコマンド [既存・変更不要]
├── make.bat             # Windows用ビルド [既存・変更不要]
├── _sass/
│   └── custom-solarized.scss  # カスタムテーマ [既存・変更不要]
└── _build/
    └── revealjs/        # ビルド成果物 [gitignore対象]

.github/
└── workflows/
    └── deploy.yml       # GitHub Pages自動デプロイ [新規作成]
```

**Structure Decision**: 既存のSphinxプロジェクト構成をそのまま活用する。新規作成が必要なのは `.github/workflows/deploy.yml` の1ファイルのみ。

## Implementation Design

### GitHub Actions ワークフロー設計

**ファイル**: `.github/workflows/deploy.yml`

**トリガー**:
- `push` to `main` ブランチ
- `workflow_dispatch`（手動実行）

**ジョブ構成**: 2ジョブ（build → deploy）

**buildジョブ**:
1. `actions/checkout@v6` でリポジトリをチェックアウト
2. `astral-sh/setup-uv@v7` でuvをセットアップ（キャッシュ有効）
3. `uv python install 3.13` でPythonをインストール
4. `uv sync --locked` で依存関係をインストール
5. `uv run make -C docs revealjs` でスライドをビルド
6. `actions/configure-pages@v5` でPages設定
7. `actions/upload-pages-artifact@v4` で `docs/_build/revealjs` をアップロード

**deployジョブ**:
1. `actions/deploy-pages@v4` でGitHub Pagesにデプロイ
2. 環境: `github-pages`

**権限**:
- `contents: read`
- `pages: write`
- `id-token: write`

**並行実行制御**:
- `concurrency: { group: "pages", cancel-in-progress: false }`

### 実装状況マッピング

| 要件 | 状況 | 必要な作業 |
|------|------|------------|
| FR-001: MyST → Reveal.js HTML生成 | 実装済み | なし |
| FR-002: ビルドコマンド | 実装済み | なし |
| FR-003: Sphinx拡張設定 | 実装済み | なし |
| FR-004: MyST拡張機能 | 実装済み | なし |
| FR-005: SCSSテーマコンパイル | 実装済み | なし |
| FR-006: GitHub Actions自動デプロイ | **未実装** | `deploy.yml` 新規作成 |
| FR-007: GitHub Pages公開 | **未実装** | `deploy.yml` + リポジトリ設定 |
| FR-008: uv依存関係管理 | 実装済み | なし |

## Complexity Tracking

Constitution Check に違反はないため、このセクションは空。
