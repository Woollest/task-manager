#!/bin/bash
# Task Manager - Quick Setup Script

set -e

echo "====================================="
echo "タスク管理ツール - セットアップ"
echo "====================================="
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python バージョン: $python_version"

# Verify Python 3.8+
required_version="3.8"
if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "✗ エラー: Python 3.8 以上が必要です"
    exit 1
fi

# Install requirements (currently none needed, but keep for future)
echo "✓ 依存パッケージ確認中..."
if [ -f "requirements.txt" ]; then
    python3 -m pip install -r requirements.txt --quiet 2>/dev/null || echo "  (依存パッケージなし)"
fi

# Create sample data if not exists
if [ ! -f "tasks.json" ]; then
    echo "✓ サンプルタスクを作成中..."
    python3 - <<'PYTHON'
import json
from datetime import datetime, timedelta

sample_tasks = [
    {
        "id": 1,
        "title": "プロジェクト提出",
        "description": "新しいタスク管理ツールの完成",
        "due_date": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
        "priority": "high",
        "tags": ["work", "important"],
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    },
    {
        "id": 2,
        "title": "ドキュメント作成",
        "description": "README とサンプル実行例を整理",
        "due_date": (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d"),
        "priority": "normal",
        "tags": ["docs"],
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    }
]

with open("tasks.json", "w", encoding="utf-8") as f:
    json.dump(sample_tasks, f, ensure_ascii=False, indent=2)

print("  完了: tasks.json を作成しました")
PYTHON
fi

echo ""
echo "====================================="
echo "セットアップ完了！"
echo "====================================="
echo ""
echo "最初のコマンド:"
echo "  python3 test.py list"
echo ""
echo "ヘルプ:"
echo "  python3 test.py --help"
echo ""
