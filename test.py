import argparse
import json
import random
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path


@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: str
    completed: bool = False

    def to_dict(self):
        return asdict(self)


class TaskManager:
    def __init__(self, storage_path: Path):
        self.storage_path = storage_path
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        if not self.storage_path.exists():
            return []
        try:
            with self.storage_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task(**item) for item in data]
        except (json.JSONDecodeError, TypeError):
            return []

    def _save_tasks(self):
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with self.storage_path.open("w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=2)

    def add_task(self, title: str, description: str, due_date: str):
        new_id = max((task.id for task in self.tasks), default=0) + 1
        new_task = Task(id=new_id, title=title, description=description, due_date=due_date)
        self.tasks.append(new_task)
        self._save_tasks()
        return new_task

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self._save_tasks()
                return task
        raise ValueError(f"タスクIDが見つかりません: {task_id}")

    def list_tasks(self, include_completed: bool = True):
        return [task for task in self.tasks if include_completed or not task.completed]


def build_parser():
    parser = argparse.ArgumentParser(description="簡易タスク管理ツール")
    parser.add_argument("--storage", default="./tasks.json", help="タスクを保存するJSONファイルのパス")

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="新しいタスクを追加")
    add_parser.add_argument("title", help="タスクのタイトル")
    add_parser.add_argument("description", help="タスクの説明")
    add_parser.add_argument("due_date", help="期限日 (YYYY-MM-DD)")

    complete_parser = subparsers.add_parser("complete", help="タスクを完了としてマーク")
    complete_parser.add_argument("task_id", type=int, help="完了するタスクのID")

    list_parser = subparsers.add_parser("list", help="タスク一覧を表示")
    list_parser.add_argument("--pending", action="store_true", help="完了していないタスクのみ表示")

    return parser


def format_task(task: Task):
    status = "完了" if task.completed else "未完了"
    return f"[{task.id}] {task.title} ({status})\n  期限: {task.due_date}\n  説明: {task.description}"


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    manager = TaskManager(Path(args.storage))

    if args.command == "add":
        task = manager.add_task(args.title, args.description, args.due_date)
        print("タスクを追加しました:")
        print(format_task(task))
    elif args.command == "complete":
        try:
            task = manager.complete_task(args.task_id)
            print(f"タスクを完了にしました: {task.id} - {task.title}")
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
    elif args.command == "list":
        tasks = manager.list_tasks(include_completed=not args.pending)
        if not tasks:
            print("表示するタスクがありません。")
            return 0
        print(f"タスク一覧 ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
        for task in tasks:
            print(format_task(task))
            print("---")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
