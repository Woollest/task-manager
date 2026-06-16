#!/bin/bash
# Task Manager - Demo Script

echo "====================================="
echo "タスク管理ツール - デモンストレーション"
echo "====================================="
echo ""

# Ensure setup is complete
if [ ! -f "tasks.json" ]; then
    echo "セットアップを実行中..."
    bash setup.sh
fi

echo "【1】タスク一覧を表示"
echo "  $ python3 src/task_manager.py list"
python3 src/task_manager.py list
echo ""

echo "【2】未完了のタスクのみ表示"
echo "  $ python3 src/task_manager.py list --pending"
python3 src/task_manager.py list --pending
echo ""

echo "【3】タスク統計を表示"
echo "  $ python3 src/task_manager.py stats"
python3 src/task_manager.py stats
echo ""

echo "【4】優先度で絞り込み"
echo "  $ python3 src/task_manager.py list --priority high"
python3 src/task_manager.py list --priority high
echo ""

echo "【5】新しいタスクを追加"
echo "  $ python3 src/task_manager.py add \"テスト実行\" \"デモが正常に動作しているか確認\" 2026-06-25 --priority normal --tags demo"
python3 src/task_manager.py add "テスト実行" "デモが正常に動作しているか確認" 2026-06-25 --priority normal --tags demo
echo ""

echo "【6】最新のタスク一覧"
echo "  $ python3 src/task_manager.py list --sort created"
python3 src/task_manager.py list --sort created
echo ""

echo "====================================="
echo "デモンストレーション完了"
echo "====================================="
