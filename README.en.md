# Task Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/badge/GitHub-Woollest/task--manager-black.svg)](https://github.com/Woollest/task-manager)

A simple and reliable command-line task manager with JSON storage and no external dependencies.

## Features

- Add, complete, delete, update and search tasks
- Classification by priority and tags
- Filtering and sorting by due date
- Task statistics overview
- Local storage in JSON format
- Easy setup and immediate use

## Quick Start

```bash
git clone https://github.com/Woollest/task-manager.git
cd task-manager
bash setup.sh
python3 src/task_manager.py list
```

## Usage

### Basic Commands

```bash
python3 src/task_manager.py --help
python3 src/task_manager.py add "Title" "Description" 2026-06-30 --priority high --tags work,urgent
python3 src/task_manager.py complete 1
python3 src/task_manager.py delete 1
python3 src/task_manager.py update 1 --title "New title" --priority low
python3 src/task_manager.py list --pending --tag work --sort priority
python3 src/task_manager.py search "keyword"
python3 src/task_manager.py stats
```

### list Command

```bash
python3 src/task_manager.py list --pending
python3 src/task_manager.py list --tag work
python3 src/task_manager.py list --priority high
python3 src/task_manager.py list --due-after 2026-06-01 --due-before 2026-06-30
python3 src/task_manager.py list --sort priority
```

### add Command

```bash
python3 src/task_manager.py add "Title" "Description" YYYY-MM-DD
python3 src/task_manager.py add "Shopping" "Milk and eggs" 2026-06-20 --priority high
python3 src/task_manager.py add "Meeting" "Project discussion" 2026-06-18 --priority normal --tags meeting,team
```

### Change Storage File

```bash
python3 src/task_manager.py --storage ./my_tasks.json add "Task" "Description" 2026-06-30
```

## Usage Example

![Task Manager Usage Example](usage_screenshot.png)

## Project Structure

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

## Task Format

```json
{
  "id": 1,
  "title": "Task title",
  "description": "Task description",
  "due_date": "2026-06-30",
  "priority": "high",
  "tags": ["work", "urgent"],
  "completed": false,
  "created_at": "2026-06-16T12:34:56"
}
```

## Requirements

- Python 3.8 or higher
- No additional packages required

## Local Configuration

- `tasks.json` is used for local task storage
- It is excluded from git via `.gitignore`

## License

MIT License - [LICENSE](LICENSE)

## Contributing

Feature requests and bug reports are welcome through GitHub Issues.
