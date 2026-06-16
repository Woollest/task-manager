# Task Manager Tool

This repository contains a simple command-line task manager using JSON storage.

## Quick Start

### Setup in 1 minute

```bash
# Clone the repository
git clone https://github.com/Woollest/task-manager.git
cd task-manager

# Run setup (first time only)
bash setup.sh

# Display your tasks
python3 test.py list
```

### Demo

```bash
# See usage examples
bash demo.sh
```

## Features

- Add, complete, delete, and update tasks
- List tasks and search tasks
- Filter and sort by due date, priority, and tags
- Show task statistics
- Save tasks to a JSON file (`tasks.json`)
- `tasks.json` is excluded from git using `.gitignore`

## Requirements

- Python 3.8 or higher

## Usage

Run the following command from the repository root:

```bash
python3 test.py --help
```

### Add a task

```bash
python3 test.py add "Title" "Description" 2026-06-30 --priority high --tags test,cli
```

### Complete a task

```bash
python3 test.py complete 1
```

### Delete a task

```bash
python3 test.py delete 1
```

### Update a task

```bash
python3 test.py update 1 --title "New title" --description "New description" --due_date 2026-07-01 --priority low --tags bug,urgent
```

### List tasks

```bash
python3 test.py list
```

Filter example:

```bash
python3 test.py list --pending --tag cli --sort priority
```

### Usage screenshot

Below is a sample screenshot of the command usage.

![Task manager usage example](usage_screenshot.png)

### Search tasks

```bash
python3 test.py search "keyword"
```

### Show statistics

```bash
python3 test.py stats
```

## Change storage file

To use a different storage file instead of `tasks.json`:

```bash
python3 test.py --storage ./my_tasks.json add "Title" "Description" 2026-06-30
```

## Notes

- `tasks.json` is used for local task state storage.
- It is ignored by git, so task operations will not create repository diffs.
