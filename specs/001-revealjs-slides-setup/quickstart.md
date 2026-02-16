# Quickstart: Reveal.jsスライド生成・公開基盤

## 前提条件

- Python 3.13以上
- uv（Pythonパッケージマネージャー）
- Git

## ローカルビルド

```bash
# 依存関係のインストール
uv sync

# スライドのビルド
uv run make -C docs revealjs

# ビルド成果物の確認
open docs/_build/revealjs/index.html
```

## GitHub Pagesへのデプロイ

1. GitHubリポジトリの **Settings** > **Pages** を開く
2. **Source** を **GitHub Actions** に設定する
3. mainブランチにプッシュすると自動でデプロイされる

```bash
git add .
git commit -m "Update slides"
git push origin main
```

デプロイ完了後、`https://<username>.github.io/<repo>/` でスライドが公開される。

## プロジェクト構造

```
docs/
├── conf.py              # Sphinx設定（sphinx-revealjs, MyST, SCSS）
├── index.md             # スライドソース（MyST記法）
├── Makefile             # ビルドコマンド
├── _sass/
│   └── custom-solarized.scss  # カスタムテーマ
└── _build/
    └── revealjs/        # ビルド成果物（gitignore対象）

.github/
└── workflows/
    └── deploy.yml       # GitHub Pagesデプロイワークフロー
```

## ビルドコマンド一覧

| コマンド | 説明 |
|----------|------|
| `uv run make -C docs revealjs` | Reveal.jsスライドをビルド |
| `uv run make -C docs clean` | ビルド成果物を削除 |
