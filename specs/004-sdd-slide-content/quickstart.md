# Quickstart: SDDスライドコンテンツ

## 前提条件

- Python 3.13+ がインストール済み
- uv がインストール済み
- hachimoku リポジトリが `../hachimoku/` に存在すること

## ビルド手順

```bash
# スライドのビルド
uv run make -C docs revealjs

# ブラウザでプレビュー（ビルド成功後）
# docs/_build/revealjs/index.html を開く
```

## 確認項目

1. **ビルド成功**: `uv run make -C docs revealjs` がエラーなく完了する
2. **スライド構成**: H1タイトル + H2セクション5つ + H3個別スライド
3. **natural-text準拠**: タイトル15文字以内、箇条書き25文字以内・6項目以内
4. **MyST記法準拠**: list-table、mermaid、literalinclude の使用
5. **出典リンク**: ハイパーリンクが機能すること
6. **literalinclude**: hachimoku 仕様書の抜粋が表示されること
7. **mermaid**: フローチャート・依存関係図が描画されること

## ファイル構成

```
docs/
└── index.md          # メインスライドファイル（編集対象）

specs/004-sdd-slide-content/
├── spec.md           # 仕様書
├── plan.md           # 実装計画（本ファイル群）
├── research.md       # リサーチ結果
├── data-model.md     # スライド構造定義
└── quickstart.md     # このファイル
```
