# Research: Reveal.jsスライド生成・公開基盤

**Date**: 2026-02-16
**Feature**: 001-revealjs-slides-setup

## 1. GitHub Pagesデプロイ方式

**Decision**: `actions/deploy-pages` アクション（モダン方式）を採用

**Rationale**:
- `gh-pages`ブランチへのプッシュ方式と比較して、OIDC認証によりセキュア
- GitHub公式の推奨アプローチ（2024年以降の標準）
- デプロイ履歴がGitHub UIのEnvironmentsで確認可能
- ブランチ管理の煩雑さを回避

**Alternatives considered**:
- `gh-pages`ブランチ方式: 古い方式。ブランチの管理が必要で、force pushが発生する
- サードパーティアクション（`peaceiris/actions-gh-pages`等）: 公式アクションで十分な機能がある

## 2. CI環境でのPython/uvセットアップ

**Decision**: `astral-sh/setup-uv` アクションでuvをインストールし、`uv python install`でPython 3.13をセットアップ

**Rationale**:
- `actions/setup-python`より高速
- `enable-cache: true`でキャッシュが自動的に最適化される
- プロジェクトの`pyproject.toml`と一貫した依存関係解決

**Alternatives considered**:
- `actions/setup-python` + pip: 従来のアプローチだが、uvより低速

## 3. ワークフロートリガー

**Decision**: `push`（mainブランチ）+ `workflow_dispatch`（手動実行）

**Rationale**:
- mainブランチへのプッシュで自動デプロイ（FR-006準拠）
- `workflow_dispatch`で手動再デプロイも可能（トラブルシューティング用）

**Alternatives considered**:
- PRマージ時のみ: プッシュ時と実質同じ（mainへのマージ = mainへのプッシュ）
- スケジュール実行: 静的サイトには不要

## 4. 必要な権限設定

**Decision**: `contents: read`, `pages: write`, `id-token: write`

**Rationale**:
- `contents: read`: リポジトリのチェックアウトに必要
- `pages: write`: Pages APIへのデプロイに必要
- `id-token: write`: OIDC JWTトークンのリクエストに必要（deploy-pagesの認証）

## 5. 並行実行制御

**Decision**: `concurrency: { group: "pages", cancel-in-progress: false }`

**Rationale**:
- 同時に複数のデプロイが走ることを防止
- 進行中のデプロイはキャンセルしない（中途半端な状態を回避）

## 6. 既存リソースの状況

### 実装済み（変更不要）
- `docs/conf.py`: sphinx-revealjs、MyST Parser、SCSS拡張が設定済み
- `docs/_sass/custom-solarized.scss`: 日本語最適化テーマが実装済み
- `docs/index.md`: スライドソースが存在（コンテンツは別仕様）
- `pyproject.toml`: 依存関係が定義済み（sphinx, sphinx-revealjs, myst-parser, libsass）
- `docs/Makefile`: Sphinxビルド用Makefile
- `.gitignore`: `docs/_build/` が除外済み

### 新規作成が必要
- `.github/workflows/deploy.yml`: GitHub Actionsデプロイワークフロー
