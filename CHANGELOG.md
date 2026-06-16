# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-16

### Added

- **Task Management CLI**: Full-featured command-line interface for managing tasks
  - `add`: Add new tasks with priority, tags, and due dates
  - `list`: Display tasks with filtering and sorting options
  - `complete`: Mark tasks as completed
  - `delete`: Remove tasks
  - `update`: Edit task details
  - `search`: Search tasks by keywords across titles, descriptions, and tags
  - `stats`: Display task statistics

- **Features**:
  - Priority levels: low, normal, high
  - Tagging system for task organization
  - Date filtering and sorting
  - Persistent JSON storage
  - Type hints throughout codebase
  - Comprehensive error handling

- **Project Structure**:
  - Organized `src/` directory for main code
  - `tests/` directory for unit tests
  - Professional README with Quick Start guide
  - Bilingual documentation (Japanese and English)
  - Setup and demo scripts

- **Documentation**:
  - Japanese README (README.md)
  - English README (README.en.md)
  - Usage screenshot
  - Quick start guide

- **Automation**:
  - `setup.sh`: One-command initialization
  - `demo.sh`: Interactive demonstration
  - `.gitignore`: Proper file exclusions

### Notes

- Initial public release
- MIT License
- Ready for production use
- Extensible architecture for future enhancements
