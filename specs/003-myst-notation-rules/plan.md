# Implementation Plan: MyST記法ルールの拡充

**Branch**: `003-myst-notation-rules` | **Date**: 2026-02-16 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/003-myst-notation-rules/spec.md`

## Summary

`.claude/skills/myst/SKILL.md` を拡充し、Mermaidダイアグラム・Admonition・定義リスト・一般ルールを追加する。ファイルは分割せず1ファイルに統合する（約260行見込み）。Mermaid対応の前提として `sphinxcontrib-mermaid` の依存追加とconf.py設定が必要。

## Technical Context

**Language/Version**: N/A（Markdownルール文書の更新）
**Primary Dependencies**: sphinxcontrib-mermaid 2.0.0（新規追加）
**Storage**: N/A
**Testing**: `uv run make -C docs revealjs` でビルド確認
**Target Platform**: Sphinx + sphinx-revealjs（Reveal.jsスライド出力）
**Project Type**: single
**Performance Goals**: N/A
**Constraints**: SKILL.mdは400行以下を維持する
**Scale/Scope**: 1ファイル（SKILL.md）の更新 + 前提設定2ファイル

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| 原則 | 適用 | 状態 |
|------|------|------|
| I. 入門者ファースト | SKILL.mdはコンテンツ作成者向けルールブック。各ルールに正しい記法と禁止パターンの具体例を示し、初見でも理解可能にする | PASS |
| II. 一次情報の尊重 | Mermaid構文はmermaid-js公式、MyST構文はmyst-parser公式ドキュメントに基づく | PASS |
| III. 実践による実証 | 各ルールに動作する具体例を含める | PASS |
| IV. 25分の構成規律 | SKILL.mdはスライド本文ではないため直接適用なし | N/A |
| V. 体験価値の最大化 | ルールブックを参照するだけで正しいMyST記法が書けることを目指す | PASS |

## Project Structure

### Documentation (this feature)

```text
specs/003-myst-notation-rules/
├── plan.md              # This file
├── research.md          # Phase 0 output (complete)
├── spec.md              # Feature specification
├── checklists/
│   └── requirements.md  # Specification quality checklist
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
.claude/skills/myst/
└── SKILL.md             # 更新対象（唯一の成果物）

# 前提設定（SKILL.mdの検証に必要）
pyproject.toml           # sphinxcontrib-mermaid 依存追加
docs/conf.py             # sphinxcontrib.mermaid 拡張追加
```

**Structure Decision**: 成果物は `.claude/skills/myst/SKILL.md` の1ファイル。前提設定として `pyproject.toml` と `docs/conf.py` に最小限の変更を加える。

## Implementation Design

### SKILL.md セクション構成

現在のSKILL.mdの構成を維持しつつ、新しいセクションを追加する。セクション順序はディレクティブの使用頻度に基づく。

```text
SKILL.md
├── frontmatter (name, description)  ← description更新
├── ## テーブル                       ← 維持
│   ├── ### list-table の書式
│   ├── ### 必須オプション
│   ├── ### 利用可能なオプション
│   └── ### 禁止パターン（箇条書きグループの表化を統合）
├── ## コードの取り込み               ← 維持 + 5行閾値ルール追加
│   ├── ### 基本書式
│   ├── ### 主要オプション
│   └── ### 禁止パターン / 許容パターン
├── ## ダイアグラム                   ← 新規
│   ├── ### 基本書式
│   ├── ### 推奨ダイアグラムタイプ
│   ├── ### オプション
│   └── ### 禁止パターン
├── ## Admonition                    ← 新規
│   ├── ### 基本書式
│   ├── ### 使用可能なタイプ
│   └── ### 禁止パターン
├── ## 定義リスト                    ← 新規
│   ├── ### 基本書式
│   └── ### 禁止パターン
└── ## 構文の注意点                   ← 維持 + コロンフェンスルール追加
```

### 前提設定

#### pyproject.toml

```toml
dependencies = [
    ...
    "sphinxcontrib-mermaid>=2.0.0",
]
```

#### docs/conf.py

```python
extensions = [
    "myst_parser",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.sass",
    "sphinxcontrib.mermaid",  # 追加
]
```

### 各セクションの設計方針

#### テーブル（維持）

変更なし。現在のルール（list-table必須、パイプテーブル禁止、箇条書きグループの表化）をそのまま維持。

#### コードの取り込み（小修正）

- FR-009のclarification結果を反映: 「5行以下のコード片はインラインコードブロックを許容」を禁止パターンセクションに明記
- 許容パターンの具体例を追加

#### ダイアグラム（新規）

- `:::{mermaid}` ディレクティブの基本構文
- 推奨タイプ一覧（flowchart, sequenceDiagram, stateDiagram-v2, gantt, classDiagram）+ それ以外も使用可の注記
- `name`オプションは相互参照時のみ必須（FR-004 clarification）
- 禁止パターン: ASCIIアートフローチャート（罫線文字`┌─┐→↓`による図）
- 正しい記法: flowchartの具体例

#### Admonition（新規）

- `:::{note}` 等の基本構文
- 使用可能タイプ5種（note, tip, warning, important, seealso）
- カスタムタイトル構文（`:::{admonition} タイトル` + `:class: tip`）
- コンテンツは1〜3行に簡潔にまとめるガイドライン
- 禁止パターン: プレーンテキストで「注意:」「ヒント:」と書く

#### 定義リスト（新規）

- `用語\n: 定義` の基本構文
- 複数定義の構文
- 禁止パターン: 箇条書きで定義リストを代用

#### 構文の注意点（追記）

- コロンフェンス（`:::`）統一ルールを追加（FR-016）
- 既存の list-table 構文注意点は維持

## Build Sequence

```text
1. sphinxcontrib-mermaid 依存追加 (pyproject.toml)
   ↓
2. conf.py に sphinxcontrib.mermaid 拡張追加
   ↓
3. SKILL.md 更新（全セクション）
   ↓
4. ビルド検証 (uv run make -C docs revealjs)
```

ステップ1-2はSKILL.mdルールの検証に必要な前提設定。ステップ3が本feature の主成果物。

## Complexity Tracking

特筆すべき違反なし。
