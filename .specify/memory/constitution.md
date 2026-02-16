<!--
Sync Impact Report
===================
- Version change: 0.0.0 → 1.0.0 (initial ratification)
- Added principles:
  - I. 入門者ファースト (Beginner-First)
  - II. 一次情報の尊重 (Primary Source Authority)
  - III. 実践による実証 (Proof by Practice)
  - IV. 25分の構成規律 (25-Minute Structure Discipline)
  - V. 体験価値の最大化 (Maximize Experience Value)
- Added sections:
  - プレゼンテーション品質基準
  - コンテンツ制作ワークフロー
  - Governance
- Templates requiring updates:
  - .specify/templates/plan-template.md ✅ no update needed
    (Constitution Check section is generic; principles auto-apply)
  - .specify/templates/spec-template.md ✅ no update needed
    (User story structure compatible with presentation scenarios)
  - .specify/templates/tasks-template.md ✅ no update needed
    (Phase structure compatible with presentation workflow)
- Follow-up TODOs: none

- Version change: 1.0.0 → 1.1.0 (MINOR: 品質基準に具体的数値制約を追加)
- Changed sections:
  - プレゼンテーション品質基準: フォントと可読性の項目を更新
    - 「会場後方からも読める」→ オンライン開催前提に修正
    - フルHDレイアウト制約を追加（h2: 15文字、箇条書き: 25文字/6項目）
    - CSS実測値の根拠を注記として記載（960×700px、36px基準）
    - コード例の行数制約にCSS根拠を注記として追加
- Templates requiring updates: none
  (品質基準はテンプレートから参照されない)
-->

# STA.py #120 プレゼンテーション Constitution

## Core Principles

### I. 入門者ファースト (Beginner-First)

すべてのスライドコンテンツはプログラミング入門者が理解できる水準で
記述しなければならない。

- 専門用語を初出時に**必ず**平易な言葉で説明すること
- 抽象概念は具体的なたとえ話（アナロジー）で補強すること
- 1枚のスライドに盛り込む概念は1つに限定すること
- コード例を示す場合は、最小限の行数で要点を伝えること
- 「知っていて当然」という前提を置かないこと

**根拠**: 聴衆にはプログラミング歴の浅い参加者が含まれる。
入門者が置いてけぼりにならないことが、発表全体の伝達力を決める。

### II. 一次情報の尊重 (Primary Source Authority)

SDD（仕様書駆動開発）やSpec Kitなどの専門用語・概念を説明する際は、
もっとも信頼性が高い一次情報を参照しなければならない。

- **SDD の定義**: GitHub spec-kit リポジトリ (`spec-driven.md`) を
  正式な定義元とする。「仕様がコードに仕えるのではなく、
  コードが仕様に仕える」（パワーインバージョン）が核心概念
- **学術的起源**: 2004年にTDD（テスト駆動開発）と
  DbC（契約による設計）の融合として学術的に定式化された事実を
  Wikipedia の Spec-driven development 記事に基づき引用すること
- **批判的視点**: Martin Fowler の記事による客観的分析（レビュー負荷、
  問題サイズの適合性）も公平に紹介すること
- 二次情報・ブログ記事のみに依拠した説明は禁止する
- 出典を示せない主張をスライドに含めないこと

**一次情報リスト**:

| 情報源 | URL | 用途 |
|--------|-----|------|
| GitHub spec-kit | github.com/github/spec-kit | SDDの定義・ワークフロー |
| Wikipedia | en.wikipedia.org/wiki/Spec-driven_development | 学術的起源・歴史 |
| Martin Fowler | martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html | 客観的ツール比較・批判的分析 |

**根拠**: 新しい概念を紹介する発表において、情報の正確性は
信頼性の土台である。一次情報に基づかない説明は誤解を生む。

### III. 実践による実証 (Proof by Practice)

SDDとSpec Kitの有効性は、理論の説明だけでなく
具体的な実践例を通じて実感させなければならない。

- このプレゼンテーション自体がSpec Kitで作られた
  **メタ実践例**であることを示すこと
- Spec Kit のワークフロー（specify → plan → tasks → implement）を
  実際の成果物を見せながら解説すること
- 「従来のやり方」と「SDDのやり方」の対比を
  具体的な時間・成果物で示すこと
- 聴衆が「自分もやってみたい」と思える手順を提示すること

**根拠**: 「百聞は一見に如かず」。抽象的なメソドロジーの説明よりも、
目の前で動く実例のほうが聴衆の記憶に残り、行動を促す。

### IV. 25分の構成規律 (25-Minute Structure Discipline)

発表内容は25分で話し終えられる分量に厳密に収めなければならない。

- スライド総数の目安: 20〜30枚（1枚あたり約1分）
- 各セクションに時間配分を設定し、合計が25分を超えないこと
- 推奨構成:
  - 導入・自己紹介: 2〜3分
  - 課題提起（なぜSDDが必要か）: 4〜5分
  - SDDの解説: 5〜6分
  - Spec Kit のデモ・実践例: 8〜10分
  - まとめ・次のステップ: 2〜3分
- 「あれもこれも」と詰め込まず、核心メッセージに集中すること
- 削るべきか迷ったら、削ること

**根拠**: 時間超過は聴衆の集中力を損ない、
核心メッセージの伝達力を低下させる。制約が明確さを生む。

### V. 体験価値の最大化 (Maximize Experience Value)

聴衆が発表後に「SDDを自分で試せる」状態で帰れることを
ゴールとしなければならない。

- 発表の最後に、聴衆が即座に始められる具体的な手順を示すこと
- Spec Kit のインストール・初期設定の手順を含めること
- 「明日から使える」レベルの実用性を優先すること
- 完璧な理解よりも「まず動かしてみる」体験を重視すること
- 参考リンク・リソース集をスライド最終ページに掲載すること

**根拠**: 知識の伝達だけでは行動は変わらない。
聴衆が次の一歩を踏み出せる状態にすることが発表の価値を最大化する。

## プレゼンテーション品質基準

スライドの品質を一定水準に保つための基準。

- **日本語テキスト**: `.claude/skills/natural-text/SKILL.md` の
  ルールに従うこと
- **フォントと可読性**: 本イベントはオンライン開催であり、
  フルHD（1920×1080）画面での視認性を基準とする。
  カスタムSolarizedテーマの日本語最適化を活用し、
  以下のレイアウト制約を遵守すること:
  - **h2タイトル**: 15文字以内
  - **箇条書き1項目**: 25文字以内（半角文字混在を考慮）
  - **箇条書き項目数**: 1スライドあたり6項目以内
  - 注: Reveal.jsスライド領域 960×700px、本文 `font-size: 36px` 基準。
    左右padding各40pxを除いた有効幅880pxに対し、
    全角36px換算で約24文字が1行上限となる。
    折り返しによる可読性低下を防ぐため25文字を目安とする
- **コード例**: シンタックスハイライトを適用し、
  1スライドあたりのコード行数は10行以下とすること。
  注: `pre { font-size: 0.5em }` = 18px、`line-height: 1.4em` = 25.2px。
  コンテンツ領域約550pxに対し物理上限は約21行だが、
  可読性を考慮して10行以内とする
- **図解**: 概念の説明には文章よりも図解を優先すること
- **スライドタイトル**: 各スライドのタイトルは内容を端的に要約し、
  タイトルだけ読んでも発表の流れが追えること

## コンテンツ制作ワークフロー

このプレゼンテーション自体をSpec Kit のワークフローで制作する。

1. **仕様作成** (`/speckit.specify`): 発表内容の仕様をspecに記述
2. **計画策定** (`/speckit.plan`): スライド構成とセクション設計を計画
3. **タスク生成** (`/speckit.tasks`): 各スライドの制作タスクを生成
4. **実装** (`/speckit.implement`): MyST記法でスライドを記述、
   `uv run make -C docs revealjs` でビルド確認
5. **検証**: ビルド成功・スライド表示確認・時間配分の検証

このワークフロー自体が原則III（実践による実証）の実例となる。

## Governance

この憲法はプレゼンテーションコンテンツ制作における
最上位の指針として機能する。

- すべてのスライドコンテンツは本憲法の原則に適合しなければならない
- 原則の追加・変更には、変更理由の文書化と
  影響範囲の確認が必要である
- バージョニングはセマンティックバージョニングに従う:
  - MAJOR: 原則の削除・根本的な再定義
  - MINOR: 原則の追加・大幅な拡充
  - PATCH: 表現の修正・誤字修正・非意味的な調整
- 各仕様・計画の作成時に Constitution Check を実施すること

**Version**: 1.1.0 | **Ratified**: 2026-02-16 | **Last Amended**: 2026-02-16
