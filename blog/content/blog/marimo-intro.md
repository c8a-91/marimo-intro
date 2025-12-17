+++
title = "marimo というノートブックの紹介"
date = 2025-12-18
description = "Python の新しいリアクティブノートブック環境 marimo を紹介します"
+++

この記事は [RWPL Advent Calendar 2025](https://adventar.org/calendars/11609) の 18 日目の記事です。

本記事では、Python の新しいノートブック環境「[marimo](https://marimo.io/)」を紹介します。今年見つけた面白いツールなので、この機会に共有したいと思います。

## 目次

1. [Notebook とは？](#notebook)
2. [marimo のメリット](#compare)
3. [まとめ](#summary)
4. [参考文献](#references)

## 1. Notebook とは？ {#notebook}

**ノートブック**は、コード、テキスト、可視化を1つのドキュメントにまとめられる対話型の開発環境です。

### 主な用途

- **データサイエンス**: データの探索、クリーニング、分析
- **機械学習**: モデルの構築、実験、評価
- **教育**: プログラミングの学習、チュートリアル作成
- **レポート作成**: 分析結果の共有、ドキュメンテーション

代表的なノートブック環境として **[Jupyter Notebook](https://jupyter.org/)** が広く使われていますが、本記事では比較的最近注目されている marimo を紹介します。

## 2. marimo のメリット {#compare}

### 実行モデル・再現性

Jupyter ではセルを任意の順序で実行できるため、実行順序によって結果が変わる「隠れた状態」問題が発生することがあります。

marimo は**リアクティブ実行**を採用しています。あるセルで変数を更新すると、その変数に依存するセルが自動的に再実行されます。これにより、常にコードと出力が一致し、再現性が保証されます。

```python
# セル1: スライダーを定義
age_min = mo.ui.slider(start=0, stop=80, value=0, label="年齢（下限）")
age_max = mo.ui.slider(start=0, stop=80, value=80, label="年齢（上限）")

# セル2: スライダーに依存（値を変えると自動で再実行される）
filtered = titanic_data[(titanic_data["age"] >= age_min.value) & (titanic_data["age"] < age_max.value)]
```

**実際に試してみてください：** 下のスライダーを動かすと、グラフがリアルタイムで更新されます。Jupyter でも同様のことは可能らしいですが、marimo ではコールバック関数を書かずに、変数を参照するだけで実現できます。

<iframe src="/notebooks/demo.html" width="100%" height="500" frameborder="0" style="border: 1px solid #e5e7eb; border-radius: 8px;"></iframe>

### 保存形式・Git

Jupyter は JSON 形式（.ipynb）で保存されるため、Git での差分確認が困難です。

marimo は Pure Python（.py）で保存されるため、通常の Python ファイルと同様に Git で管理できます。

**Jupyter (.ipynb) - JSON 形式:**
```json
{
  "cells": [
    {
      "cell_type": "code",
      "source": ["print('Hello, World!')"]
    }
  ]
}
```

**marimo (.py) - Pure Python:**
```python
import marimo
app = marimo.App()

@app.cell
def _():
    print('Hello, World!')
    return
```

### ACP（AI エージェント連携）

marimo は **[Agent Client Protocol（ACP）](https://agentclientprotocol.com/)** をサポートしています。ACP は AI エージェントとエディタを連携させるためのオープンプロトコルです。

**ACP でできること：**
- AI エージェントが marimo ノートブックを直接読み書き
- チャットパネルからコーディング支援を受ける
- セルの自動生成・修正

**対応エージェント：** Claude Code、Google Gemini

詳細は公式ドキュメントを参照してください：[Agents - marimo](https://docs.marimo.io/guides/editor_features/agents/)

## 3. まとめ {#summary}

### こんな人に marimo がおすすめ

- **再現性を重視する人**: リアクティブ実行で常に一貫した結果
- **Git でノートブックを管理したい人**: Pure Python で差分が見やすい
- **インタラクティブなレポートを作りたい人**: 組み込み UI で簡単に実現
- **ノートブックをアプリとしてデプロイしたい人**: 追加ツール不要

### 始め方

```bash
# インストール
pip install marimo

# 新しいノートブックを作成
marimo edit

# 既存のノートブックを開く
marimo edit notebook.py

# アプリとして実行
marimo run notebook.py
```

marimo は Jupyter とは違った魅力があるノートブック環境です。
ぜひ一度試してみてください！

より詳しく知りたい方は、[公式ドキュメント](https://docs.marimo.io/)をご覧ください。

---

## 4. 参考文献 {#references}

- [marimo 公式サイト](https://marimo.io/) - marimo の概要、特徴、インストール方法
- [marimo 公式ドキュメント](https://docs.marimo.io/) - 詳細な使い方、API リファレンス、チュートリアル
- [marimo Agents ドキュメント](https://docs.marimo.io/guides/editor_features/agents/) - ACP を通じた AI エージェント連携機能の説明
- [Project Jupyter 公式サイト](https://jupyter.org/) - Jupyter プロジェクトの概要
- [Agent Client Protocol 公式サイト](https://agentclientprotocol.com/) - AI エージェントとエディタを連携させるプロトコルの仕様
