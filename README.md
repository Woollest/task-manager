# Task Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/badge/GitHub-Woollest/task--manager-black.svg)](https://github.com/Woollest/task-manager)

シンプルで堅牢なコマンドラインタスク管理ツールです。JSON ストレージを使用し、外部依存なしで利用できます。

## 特徴

- タスクの追加、完了、削除、更新、検索
- 優先度とタグによる分類
- 期限によるフィルタとソート
- タスク統計の表示
- JSON 形式のローカル保存
- すぐに使えるセットアップ

## クイックスタート

```bash
git clone https://github.com/Woollest/task-manager.git
cd task-manager
bash setup.sh
python3 src/task_manager.py list
```

## 使い方

### 基本コマンド

```bash
python3 src/task_manager.py --help
python3 src/task_manager.py add "タイトル" "説明" 2026-06-30 --priority high --tags work,urgent
python3 src/task_manager.py complete 1
python3 src/task_manager.py delete 1
python3 src/task_manager.py update 1 --title "新しいタイトル" --priority low
python3 src/task_manager.py list --pending --tag work --sort priority
python3 src/task_manager.py search "キーワード"
python3 src/task_manager.py stats
```

### list コマンド

```bash
python3 src/task_manager.py list --pending
python3 src/task_manager.py list --tag work
python3 src/task_manager.py list --priority high
python3 src/task_manager.py list --due-after 2026-06-01 --due-before 2026-06-30
python3 src/task_manager.py list --sort priority
```

### add コマンド

```bash
python3 src/task_manager.py add "タイトル" "説明" YYYY-MM-DD
python3 src/task_manager.py add "買い物" "牛乳と卵" 2026-06-20 --priority high
python3 src/task_manager.py add "会議" "プロジェクト打ち合わせ" 2026-06-18 --priority normal --tags meeting,team
```

### ストレージの切り替え

```bash
python3 src/task_manager.py --storage ./my_tasks.json add "タスク" "説明" 2026-06-30
```

## 使用例

![Task Manager Usage Example](usage_screenshot.png)

## プロジェクト構成

```
task-manager/
├── src/
│   └── task_manager.py
├── tests/
├── README.md
├── README.en.md
├── LICENSE
├── CHANGELOG.md
├── setup.sh
├── demo.sh
├── requirements.txt
├── .gitignore
└── usage_screenshot.png
```

## タスク形式

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

## 要件

- Python 3.8 以上
- 追加パッケージ不要（標準ライブラリのみ）

## ローカル設定

- `tasks.json` がローカルタスクを保存します
- `.gitignore` に追加されるため、リポジトリには含まれません

## ライセンス

MIT License - [LICENSE](LICENSE)

## 貢献

改善提案やバグ報告は GitHub Issues で受け付けます。
