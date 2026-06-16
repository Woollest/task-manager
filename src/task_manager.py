import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict, field
from datetime import datetime, date
from pathlib import Path
from typing import Any, Iterable, List, Optional


DATE_FORMAT = "%Y-%m-%d"
PRIORITY_CHOICES = ["low", "normal", "high"]
TAG_SPLIT_PATTERN = re.compile(r"\s*,\s*")


class Color:
    """ANSI color codes for terminal output."""
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'
    
    # Text styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    # Reset
    RESET = '\033[0m'
    
    @staticmethod
    def disable():
        """Disable colors for non-TTY output."""
        for attr in dir(Color):
            if not attr.startswith('_') and attr != 'disable':
                setattr(Color, attr, '')


# Disable colors if not a TTY
if not sys.stdout.isatty():
    Color.disable()


@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: str
    priority: str = "normal"
    tags: List[str] = field(default_factory=list)
    completed: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))

    def __post_init__(self):
        self.priority = self.priority.lower()
        if not isinstance(self.tags, list):
            self.tags = [str(self.tags)]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def due_date_obj(self) -> date:
        return datetime.strptime(self.due_date, DATE_FORMAT).date()

    @property
    def is_overdue(self) -> bool:
        """Check if task is overdue (incomplete and past due date)."""
        if self.completed:
            return False
        return self.due_date_obj < date.today()

    def matches_query(self, query: str) -> bool:
        normalized = query.lower()
        return (
            normalized in self.title.lower()
            or normalized in self.description.lower()
            or any(normalized in tag.lower() for tag in self.tags)
        )


class TaskManager:
    def __init__(self, storage_path: Path):
        self.storage_path = storage_path
        self.tasks = self._load_tasks()

    def _load_tasks(self) -> List[Task]:
        if not self.storage_path.exists():
            return []
        try:
            with self.storage_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task(**item) for item in data]
        except (json.JSONDecodeError, TypeError, ValueError):
            return []

    def _save_tasks(self) -> None:
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with self.storage_path.open("w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=2)

    def add_task(self, title: str, description: str, due_date: str, priority: str, tags: List[str]) -> Task:
        new_id = max((task.id for task in self.tasks), default=0) + 1
        new_task = Task(id=new_id, title=title, description=description, due_date=due_date, priority=priority, tags=tags)
        self.tasks.append(new_task)
        self._save_tasks()
        return new_task

    def complete_task(self, task_id: int) -> Task:
        task = self._find_task(task_id)
        task.completed = True
        self._save_tasks()
        return task

    def delete_task(self, task_id: int) -> Task:
        task = self._find_task(task_id)
        self.tasks.remove(task)
        self._save_tasks()
        return task

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[str] = None,
        priority: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Task:
        task = self._find_task(task_id)
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if due_date is not None:
            task.due_date = due_date
        if priority is not None:
            task.priority = priority
        if tags is not None:
            task.tags = tags
        self._save_tasks()
        return task

    def list_tasks(
        self,
        include_completed: bool = True,
        tag: Optional[str] = None,
        priority: Optional[str] = None,
        due_before: Optional[str] = None,
        due_after: Optional[str] = None,
        sort_by: Optional[str] = None,
    ) -> List[Task]:
        results = [task for task in self.tasks if include_completed or not task.completed]

        if tag:
            results = [task for task in results if tag.lower() in (t.lower() for t in task.tags)]
        if priority:
            results = [task for task in results if task.priority == priority]
        if due_before:
            date_before = datetime.strptime(due_before, DATE_FORMAT).date()
            results = [task for task in results if task.due_date_obj <= date_before]
        if due_after:
            date_after = datetime.strptime(due_after, DATE_FORMAT).date()
            results = [task for task in results if task.due_date_obj >= date_after]

        if sort_by == "due":
            results.sort(key=lambda task: task.due_date_obj)
        elif sort_by == "priority":
            results.sort(key=lambda task: PRIORITY_CHOICES.index(task.priority))
        elif sort_by == "created":
            results.sort(key=lambda task: task.created_at)

        return results

    def search_tasks(self, query: str, include_completed: bool = True) -> List[Task]:
        return [task for task in self.list_tasks(include_completed=include_completed) if task.matches_query(query)]

    def stats(self) -> dict[str, int]:
        total = len(self.tasks)
        completed = sum(task.completed for task in self.tasks)
        pending = total - completed
        return {"total": total, "completed": completed, "pending": pending}

    def _find_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"タスクIDが見つかりません: {task_id}")


def parse_date(value: str) -> str:
    try:
        parsed = datetime.strptime(value, DATE_FORMAT).date()
        return parsed.strftime(DATE_FORMAT)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"日付は {DATE_FORMAT} 形式で指定してください: {value}") from exc


def parse_tags(value: str) -> List[str]:
    if not value.strip():
        return []
    return [tag for tag in TAG_SPLIT_PATTERN.split(value.strip()) if tag]


def build_parser() -> argparse.ArgumentParser:
    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument("--storage", default="./tasks.json", help="タスクを保存するJSONファイルのパス")

    parser = argparse.ArgumentParser(
        description="高機能タスク管理ツール",
        parents=[common_parser],
        add_help=False,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", parents=[common_parser], help="新しいタスクを追加")
    add_parser.add_argument("title", help="タスクのタイトル")
    add_parser.add_argument("description", help="タスクの説明")
    add_parser.add_argument("due_date", type=parse_date, help="期限日 (YYYY-MM-DD)")
    add_parser.add_argument("--priority", choices=PRIORITY_CHOICES, default="normal", help="優先度")
    add_parser.add_argument("--tags", type=parse_tags, default=[], help="タグをカンマ区切りで指定")

    complete_parser = subparsers.add_parser("complete", parents=[common_parser], help="タスクを完了としてマーク")
    complete_parser.add_argument("task_id", type=int, help="完了するタスクのID")

    delete_parser = subparsers.add_parser("delete", parents=[common_parser], help="タスクを削除")
    delete_parser.add_argument("task_id", type=int, help="削除するタスクのID")

    update_parser = subparsers.add_parser("update", parents=[common_parser], help="タスクを更新")
    update_parser.add_argument("task_id", type=int, help="更新するタスクのID")
    update_parser.add_argument("--title", help="新しいタイトル")
    update_parser.add_argument("--description", help="新しい説明")
    update_parser.add_argument("--due_date", type=parse_date, help="新しい期限日 (YYYY-MM-DD)")
    update_parser.add_argument("--priority", choices=PRIORITY_CHOICES, help="新しい優先度")
    update_parser.add_argument("--tags", type=parse_tags, help="更新するタグをカンマ区切りで指定")

    list_parser = subparsers.add_parser("list", parents=[common_parser], help="タスク一覧を表示")
    list_parser.add_argument("--pending", action="store_true", help="完了していないタスクのみ表示")
    list_parser.add_argument("--tag", help="タグで絞り込み")
    list_parser.add_argument("--priority", choices=PRIORITY_CHOICES, help="優先度で絞り込み")
    list_parser.add_argument("--due-before", type=parse_date, help="指定日までのタスク")
    list_parser.add_argument("--due-after", type=parse_date, help="指定日以降のタスク")
    list_parser.add_argument("--sort", choices=["due", "priority", "created"], default="due", help="ソートキー")

    search_parser = subparsers.add_parser("search", parents=[common_parser], help="クエリでタスクを検索")
    search_parser.add_argument("query", help="検索文字列")
    search_parser.add_argument("--pending", action="store_true", help="完了していないタスクのみ対象")

    subparsers.add_parser("stats", parents=[common_parser], help="タスクの統計情報を表示")

    return parser


def get_priority_color(priority: str) -> str:
    """Get color based on priority level."""
    if priority == "high":
        return Color.RED
    elif priority == "normal":
        return Color.YELLOW
    else:  # low
        return Color.GREEN


def format_task(task: Task) -> str:
    """Format task with colors and visual markers."""
    
    # Status marker
    if task.completed:
        status_marker = f"{Color.GREEN}✓{Color.RESET}"
        status_text = f"{Color.GRAY}完了{Color.RESET}"
        title_color = Color.GRAY
        title_style = Color.DIM
    else:
        status_marker = f"{Color.RED}☐{Color.RESET}"
        status_text = f"{Color.RED}未完了{Color.RESET}"
        title_color = ""
        title_style = Color.BOLD
    
    # Title with color
    title = f"{title_color}{title_style}{task.title}{Color.RESET}"
    
    # Priority color
    priority_color = get_priority_color(task.priority)
    priority_text = f"{priority_color}{task.priority}{Color.RESET}"
    
    # Tags with color
    if task.tags:
        tags_colored = ", ".join([f"{Color.CYAN}#{tag}{Color.RESET}" for tag in task.tags])
    else:
        tags_colored = f"{Color.GRAY}なし{Color.RESET}"
    
    # Overdue warning
    overdue_warning = ""
    if task.is_overdue:
        overdue_warning = f"\n  {Color.RED}{Color.BOLD}⚠️ 期限超過！{Color.RESET}"
    
    return (
        f"[{status_marker} {task.id}] {title} ({status_text}){overdue_warning}\n"
        f"  期限: {task.due_date}\n"
        f"  優先度: {priority_text}\n"
        f"  タグ: {tags_colored}\n"
        f"  説明: {task.description}\n"
        f"  作成日時: {task.created_at}"
    )


def print_task_list(tasks: Iterable[Task], header: str) -> None:
    if not tasks:
        print(f"{Color.YELLOW}表示するタスクがありません。{Color.RESET}")
        return
    print(f"{Color.BOLD}{Color.CYAN}{header}{Color.RESET}")
    for task in tasks:
        print(format_task(task))
        print("---")


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    manager = TaskManager(Path(args.storage))

    try:
        if args.command == "add":
            task = manager.add_task(args.title, args.description, args.due_date, args.priority, args.tags)
            print(f"{Color.GREEN}{Color.BOLD}✓ タスクを追加しました:{Color.RESET}")
            print(format_task(task))

        elif args.command == "complete":
            task = manager.complete_task(args.task_id)
            print(f"{Color.GREEN}{Color.BOLD}✓ タスクを完了にしました:{Color.RESET} [{task.id}] {task.title}")

        elif args.command == "delete":
            task = manager.delete_task(args.task_id)
            print(f"{Color.RED}{Color.BOLD}✓ タスクを削除しました:{Color.RESET} [{task.id}] {task.title}")

        elif args.command == "update":
            task = manager.update_task(
                args.task_id,
                title=args.title,
                description=args.description,
                due_date=args.due_date,
                priority=args.priority,
                tags=args.tags,
            )
            print(f"{Color.BLUE}{Color.BOLD}✓ タスクを更新しました:{Color.RESET}")
            print(format_task(task))

        elif args.command == "list":
            tasks = manager.list_tasks(
                include_completed=not args.pending,
                tag=args.tag,
                priority=args.priority,
                due_before=args.due_before,
                due_after=args.due_after,
                sort_by=args.sort,
            )
            print_task_list(tasks, f"タスク一覧 ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")

        elif args.command == "search":
            tasks = manager.search_tasks(args.query, include_completed=not args.pending)
            print_task_list(tasks, f"検索結果: {args.query}")

        elif args.command == "stats":
            stats = manager.stats()
            print(f"{Color.BOLD}{Color.CYAN}📊 タスク統計:{Color.RESET}")
            print(f"  {Color.BOLD}合計:{Color.RESET} {stats['total']}")
            print(f"  {Color.GREEN}✓ 完了:{Color.RESET} {stats['completed']}")
            print(f"  {Color.RED}☐ 未完了:{Color.RESET} {stats['pending']}")
            if stats['total'] > 0:
                completion_rate = (stats['completed'] / stats['total']) * 100
                print(f"  {Color.BOLD}進捗:{Color.RESET} {completion_rate:.1f}%")

        return 0

    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
