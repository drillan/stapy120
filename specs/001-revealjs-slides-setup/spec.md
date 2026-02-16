# Feature Specification: Reveal.jsスライド生成・公開基盤

**Feature Branch**: `001-revealjs-slides-setup`
**Created**: 2026-02-16
**Status**: Draft
**Input**: User description: "docsのドキュメントをもとにsphinx-revealjsでスライド生成し、MyST記法で記述、GitHub Pagesにホストする"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - ローカルでスライドをビルドする (Priority: P1)

発表者がMyST記法で書いたMarkdownファイルからReveal.jsスライドをローカルでビルドし、プレビューできる。

**Why this priority**: スライド作成の基本操作であり、他のすべての機能の前提となる

**Independent Test**: ビルドコマンドを実行し、生成されたHTMLファイルをブラウザで開いてスライドとして表示されることを確認できる

**Acceptance Scenarios**:

1. **Given** MyST記法で記述されたMarkdownファイルが`docs/`配下に存在する, **When** ビルドコマンドを実行する, **Then** `docs/_build/revealjs/`にReveal.jsスライドのHTMLが生成される
2. **Given** ビルドが完了した状態, **When** 生成されたHTMLをブラウザで開く, **Then** スライドが正しく表示され、ページ送りで遷移できる
3. **Given** MyST記法のMarkdownでコードブロックを含むスライド, **When** ビルドを実行する, **Then** シンタックスハイライトが適用されたコードブロックが表示される

---

### User Story 2 - GitHub Pagesでスライドを公開する (Priority: P2)

発表者がmainブランチにプッシュすると、自動でスライドがビルドされGitHub Pagesに公開される。聴衆はURLにアクセスするだけでスライドを閲覧できる。

**Why this priority**: スライドの共有・公開はプレゼンテーションの主要な目的であり、ローカルビルドの次に重要

**Independent Test**: mainブランチへのプッシュ後、GitHub PagesのURLにアクセスしてスライドが表示されることを確認できる

**Acceptance Scenarios**:

1. **Given** mainブランチに変更がプッシュされた, **When** CIパイプラインが実行される, **Then** スライドが自動でビルドされGitHub Pagesにデプロイされる
2. **Given** デプロイが完了した, **When** 聴衆がGitHub PagesのURLにアクセスする, **Then** 最新のスライドが表示される
3. **Given** スライドの内容を更新してプッシュした, **When** デプロイが完了する, **Then** GitHub Pages上のスライドが更新された内容に反映される

---

### User Story 3 - カスタムテーマでスライドを表示する (Priority: P3)

日本語に最適化されたカスタムテーマ（Solarizedベース）が適用された状態でスライドが表示される。フォント、行間、文字間隔が日本語の可読性に配慮されている。

**Why this priority**: 視覚的な品質はプレゼンテーションの伝達力に直結するが、機能面が先に整っている必要がある

**Independent Test**: ビルドしたスライドでカスタムテーマが適用され、日本語テキストが読みやすく表示されることを視覚的に確認できる

**Acceptance Scenarios**:

1. **Given** カスタムSCSSテーマファイルが存在する, **When** スライドをビルドする, **Then** テーマがCSSにコンパイルされスライドに適用される
2. **Given** 日本語テキストを含むスライド, **When** ブラウザで表示する, **Then** 日本語フォント（ゴシック体）が適用され、適切な行間・文字間隔で表示される

---

### Edge Cases

- ビルドコマンド実行時にMyST記法の構文エラーがある場合、エラーメッセージが表示されビルドが失敗する
- SCSSファイルに構文エラーがある場合、テーマのコンパイルが失敗しビルドエラーとなる
- GitHub Actionsのワークフローが失敗した場合、前回の正常なデプロイが維持される
- `docs/_build/`が存在しない初回ビルドでも正常にビルドが完了する

## Scope

### In Scope

- sphinx-revealjsによるスライドビルドパイプライン
- MyST記法によるスライド記述基盤
- `docs/conf.py`のSphinx設定
- カスタムSCSSテーマのビルド
- GitHub Actionsによる自動ビルド・デプロイ
- GitHub Pagesでのホスティング

### Out of Scope（Non-Goals）

- スライドのコンテンツ（内容）は別仕様で管理する
- PDF出力やスライドのエクスポート機能
- カスタムドメインの設定
- アクセス制限や認証
- スライドのバージョニングや複数スライドの管理

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: ビルドシステムは、`docs/`配下のMyST記法MarkdownファイルからReveal.jsスライドHTMLを生成できなければならない
- **FR-002**: ビルドコマンド `uv run make -C docs revealjs` で一貫してスライドをビルドできなければならない
- **FR-003**: Sphinx設定ファイル（`docs/conf.py`）でsphinx-revealjs、MyST Parser、SCSSコンパイラの拡張機能が有効でなければならない
- **FR-004**: MyST Parserの拡張機能（colon_fence、deflist、tasklist）が利用可能でなければならない
- **FR-005**: カスタムSCSSテーマファイルがビルド時にCSSにコンパイルされ、スライドに適用されなければならない
- **FR-006**: mainブランチへのプッシュをトリガーに、GitHub Actionsワークフローが自動でスライドをビルド・デプロイしなければならない
- **FR-007**: ビルド成果物（`docs/_build/revealjs/`の内容）がGitHub Pagesに公開されなければならない
- **FR-008**: プロジェクトの依存関係は`pyproject.toml`で管理され、`uv`で解決されなければならない

### Key Entities

- **スライドソース**: MyST記法で記述されたMarkdownファイル。`docs/`配下に配置される
- **Sphinx設定**: `docs/conf.py`。ビルドに必要な拡張機能やテーマの設定を保持する
- **カスタムテーマ**: `docs/_sass/`配下のSCSSファイル。日本語最適化されたスタイルを定義する
- **ビルド成果物**: `docs/_build/revealjs/`に生成されるHTML・CSS・JSファイル群
- **デプロイパイプライン**: GitHub Actionsワークフロー。ビルドからGitHub Pagesへのデプロイを自動化する

## Assumptions

- GitHubリポジトリのSettings > PagesでGitHub Actionsからのデプロイが有効化されている（または有効化する）
- `uv`がCI環境で利用可能である（GitHub Actionsでセットアップする）
- Python 3.13以上がCI環境で利用可能である
- リポジトリはパブリックである（GitHub Pages無料利用の前提）

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: ビルドコマンド1回の実行で、MyST記法のMarkdownからReveal.jsスライドHTMLが生成される
- **SC-002**: mainブランチへのプッシュから5分以内にGitHub Pagesにスライドが公開される
- **SC-003**: GitHub PagesのURLにアクセスした聴衆が、追加のソフトウェアなしにスライドを閲覧できる
- **SC-004**: カスタムテーマが適用され、日本語テキストが適切なフォントと行間で表示される
