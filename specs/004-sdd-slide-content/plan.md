# Implementation Plan: SDDスライドコンテンツ作成

**Branch**: `004-sdd-slide-content` | **Date**: 2026-02-16 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/004-sdd-slide-content/spec.md`

## Summary

「みんなのPython勉強会#120」で発表する「Spec Kitではじめる仕様駆動開発入門」のスライドコンテンツを `docs/index.md` に作成する。既存の `docs/index.md` をベースに、`work/outline.txt` の構成案と仕様に基づいて5セクション構成（SDD概要・SDDのツール・Spec Kit入門・実践例・まとめ）のスライドに再構成する。

一次情報（GitHub spec-kit、Wikipedia、Birgitta Böckeler の分析記事）に基づく正確なコンテンツ作成と、MyST記法ルール（list-table、mermaid、literalinclude）への準拠が技術的な要点である。

## Technical Context

**Language/Version**: MyST Markdown（myst-parser 5.0+）
**Primary Dependencies**: Sphinx 9.1+, sphinx-revealjs 3.2+, sphinxcontrib-mermaid 2.0.0
**Storage**: N/A（静的サイト生成）
**Testing**: `uv run make -C docs revealjs`（ビルド成功を検証）
**Target Platform**: Reveal.js スライド（ブラウザ表示、フルHD想定）
**Project Type**: ドキュメント生成（Sphinxプロジェクト）
**Performance Goals**: N/A
**Constraints**: 25分の発表に適した分量（20〜30枚目安）、natural-textルール準拠
**Scale/Scope**: スライド22枚 + セクション区切り5枚 = 計27枚

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-Research Check

| 原則 | 状態 | 確認内容 |
|---|---|---|
| I. 入門者ファースト | ✅ PASS | 専門用語の平易な説明、レシピのたとえ話、1スライド1メッセージを計画に含む |
| II. 一次情報の尊重 | ✅ PASS | GitHub spec-kit、Wikipedia、Birgitta Böckeler 記事の3ソースを特定済み。Research で全ソースの正確性を検証済み |
| III. 実践による実証 | ✅ PASS | hachimoku プロジェクトの仕様書を literalinclude で実物表示。このプレゼン自体が Spec Kit で制作されたメタ実践例 |
| IV. 25分の構成規律 | ✅ PASS | 22スライド、時間配分合計21〜27分（目標25分） |
| V. 体験価値の最大化 | ✅ PASS | 参考リンクスライドに Spec Kit / Kiro / cc-sdd のURLを掲載 |

### Post-Design Check

| 原則 | 状態 | 確認内容 |
|---|---|---|
| I. 入門者ファースト | ✅ PASS | 全スライドで専門用語の初出時に平易な説明を計画。SDD定義、パワーインバージョン、Non-Goals 等すべてに説明を配置 |
| II. 一次情報の尊重 | ✅ PASS | Research（R-001〜R-009）で全ソースを検証。Kiroの「独自AIエンジン」を「Anthropic Claude搭載」に修正。Martin Fowler記事の著者をBirgitta Böckelerに修正 |
| III. 実践による実証 | ✅ PASS | hachimoku仕様書のliteralinclude（User Story 1 + Acceptance Scenarios）、依存関係のmermaidダイアグラムを設計済み |
| IV. 25分の構成規律 | ✅ PASS | data-model.md でセクション別時間配分を設計。literalincludeスライドは「さらっと流す」前提で時間超過リスクを管理 |
| V. 体験価値の最大化 | ✅ PASS | 参考リンクに Spec Kit、Kiro、cc-sdd、GitHub Blog、Martin Fowler記事を掲載。聴衆が即座に始められる状態 |

## Project Structure

### Documentation (this feature)

```text
specs/004-sdd-slide-content/
├── spec.md              # 仕様書
├── plan.md              # このファイル
├── research.md          # Phase 0: 一次情報の調査結果
├── data-model.md        # Phase 1: スライド構造定義（22枚の詳細）
├── quickstart.md        # Phase 1: ビルド・確認手順
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### 成果物（リポジトリルート）

```text
docs/
└── index.md              # メインスライドファイル（編集対象）
```

**Structure Decision**: 本フィーチャーの成果物は `docs/index.md` の1ファイルのみ。既存ファイルをベースに再構成する。ソースコードの新規作成は不要。外部依存として `../hachimoku/specs/001-architecture-spec/spec.md`（literalinclude対象）が必要。

## 実装方針

### 既存スライドの再構成

Research R-007 で定義した再構成ルールに従い、既存 `docs/index.md` のスライドを以下のように処理する:

| 操作 | 対象スライド |
|---|---|
| **移動** | バイブコーディングガチャ → SDD配下、Spec Kit紹介 → 入門配下、仕様書の例 → 実践例 |
| **残す** | レシピと料理、SDDの基本フロー、Non-Goals、SDDの欠点・注意点、まとめ、参考リンク |
| **削除** | AIとの組み合わせの利点、類似手法との比較 |
| **統合** | 適している/いない場合 → 欠点と注意点に統合 |
| **新規** | SDD定義、各ワークフローステップ（8枚）、hachimoku紹介、依存関係図 |

### MyST記法の適用

| 要素 | 変換方針 |
|---|---|
| ASCII artフロー図 | mermaid ディレクティブに変換 |
| テーブル | list-table ディレクティブを維持/適用 |
| 外部コード | literalinclude で取り込み（:lines: で抜粋） |
| コマンド例 | 5行以下のインラインコードブロック（許容） |

### コンテンツ品質

| 制約 | 基準 |
|---|---|
| スライドタイトル | 15文字以内 |
| 箇条書き1項目 | 25文字以内（全角換算） |
| 箇条書き項目数 | 6項目以内/スライド |
| テーブル列数 | 3列以内 |
| コード行数 | 10行以下/スライド |
| 出典 | 用語・概念の解説にはハイパーリンク必須 |

### 一次情報と出典

| 情報 | 出典 | 用途 |
|---|---|---|
| SDDの定義・パワーインバージョン | GitHub spec-kit `spec-driven.md` | SDD定義スライド |
| SDDの学術的起源（2004年） | Wikipedia SDD記事 | SDD定義スライドの補足 |
| SDDの批判的分析 | Birgitta Böckeler（martinfowler.com） | 欠点・注意点スライド |
| Spec Kitのワークフロー | GitHub spec-kit README.md | ワークフロースライド |
| Kiroの特徴 | kiro.dev | ツール紹介スライド |
| cc-sddの特徴 | github.com/gotalab/cc-sdd | ツール紹介スライド |
| GitHub Blog記事 | github.blog | SDD定義・参考リンク |

## Complexity Tracking

> Constitution Check で違反なし。Complexity Tracking は不要。
