# 📋 Task Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/badge/GitHub-Woollest/task--manager-black.svg)](https://github.com/Woollest/task-manager)

シンプルで強力なコマンドラインタスク管理ツール。JSON ストレージで、セットアップ不要、すぐに使える。

## ✨ 特徴

- ✅ **タスク管理**: 追加、完了、削除、更新、検索
- 🎯 **優先度とタグ**: タスク分類と優先順位付け
- 📅 **日付フィルタ**: 期限で絞り込み、ソート
- 📊 **統計表示**: タスク進捗を一目で把握
- 💾 **JSON ストレージ**: 外部ツール不要、軽量高速
- 🚀 **セットアップ簡単**: `bash setup.sh` でワンコマンド
- 📖 **ドキュメント完備**: 日本語・英語対応
- 🎓 **デモンストレーション**: `bash demo.sh` で機能確認

## 🚀 クイックスタート

### 1分でセットアップ

```bash
# リポジトリをクローン
git clone https://github.com/Woollest/task-manager.git
cd task-manager

# セットアップ実行（初回のみ）
bash setup.sh

# タスク一覧を表示
python3 src/task_manager.py list
```

### デモンストレーション

すべての機能を自動的に実演します。

```bash
bash demo.sh
```

## 📖 使い方

### 基本コマンド

```bash
# ヘルプを表示
python3 src/task_manager.py --help

# タスク追加
python3 src/task_manager.py add "タイトル" "説明" 2026-06-30 \
  --priority high --tags work,urgent

# タスク完了
python3 src/task_manager.py complete 1

# タスク削除
python3 src/task_manager.py delete 1

# タスク更新
python3 src/task_manager.py update 1 \
  --title "新タイトル" --priority low

# タスク一覧（フィルタ・ソート例）
python3 src/task_manager.py list \
  --pending --tag work --sort priority

# タスク検索
python3 src/task_manager.py search "キーワード"

# 統計表示
python3 src/task_manager.py stats
```

### 詳細オプション

#### `list` コマンド

```bash
# 未完了のみ表示
python3 src/task_manager.py list --pending

# タグで絞り込み
python3 src/task_manager.py list --tag work

# 優先度で絞り込み
python3 src/task_manager.py list --priority high

# 期限で範囲指定
python3 src/task_manager.py list \
  --due-after 2026-06-01 --due-before 2026-06-30

# ソート（due | priority | created）
python3 src/task_manager.py list --sort priority
```

#### `add` コマンド

```bash
# 基本形式
python3 src/task_manager.py add "タイトル" "説明" YYYY-MM-DD

# 優先度指定（low | normal | high）
python3 src/task_manager.py add "買い物" "牛乳と卵" 2026-06-20 \
  --priority high

# タグ指定（カンマ区切り）
python3 src/task_manager.py add "会議" "プロジェクト打ち合わせ" 2026-06-18 \
  --priority normal --tags meeting,team
```

### ストレージ切り替え

デフォルトは `tasks.json` ですが、別のファイルを使う場合:

```bash
python3 src/task_manager.py --storage ./my_tasks.json add "タスク" "説明" 2026-06-30
```

## 📸 使用例スクリーンショット

![Task Manager Usage Example](usage_screenshot.png)

## 🏗️ プロジェクト構成

```
task-manager/
├── src/
│   └── task_manager.py      # メインツール
├── tests/                    # テストディレクトリ
├── README.md                 # このファイル（日本語）
├── README.en.md              # 英語版 README
├── LICENSE                   # MIT License
├── CHANGELOG.md              # 変更履歴
├── setup.sh                  # セットアップスクリプト
├── demo.sh                   # デモンストレーション
├── requirements.txt          # 依存パッケージ
├── .gitignore                # Git 設定
└── usage_screenshot.png      # スクリーンショット
```

## 📋 タスク形式

各タスクは以下の情報を持ちます:

```json
{
  "id": 1,
  "title": "タスクタイトル",
  "description": "タスク説明",
  "due_date": "2026-06-30",
  "priority": "high",
  "tags": ["work", "urgent"],
  "completed": false,
  "created_at": "2026-06-16T12:34:56"
}
```

## ⚙️ 必要環境

- Python 3.8 以上
- 追加パッケージなし（標準ライブラリのみ）

## 📝 ローカル設定

- `tasks.json` はローカルのタスク状態保存用です
- `.gitignore` で除外しているため、Git に記録されません
- リポジトリをクローンして利用する複数の環境で、各々独立したタスクを管理できます

## 🔄 データの永続化

タスク情報は `tasks.json` に JSON 形式で保存されます:

- **自動保存**: コマンド実行時に自動保存
- **ポータブル**: JSON なので他ツールとも互換
- **拡張可能**: 必要に応じてデータベースに切り替え可能

## 📄 ライセンス

MIT License - [LICENSE](LICENSE) ファイルを参照

詳細は [CHANGELOG.md](CHANGELOG.md) を参照してください。

## 🤝 コントリビューション

改善提案やバグ報告は [GitHub Issues](https://github.com/Woollest/task-manager/issues) までお願いします。

---

**Happy Task Managing! 🎯**
