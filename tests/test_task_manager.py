import sys
import json
import tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from task_manager import Task, TaskManager


def test_task_creation():
    """Test Task dataclass creation."""
    task = Task(
        id=1,
        title="Test",
        description="Test description",
        due_date="2026-06-30",
        priority="high",
        tags=["test"],
        completed=False
    )
    assert task.id == 1
    assert task.title == "Test"
    assert task.priority == "high"
    assert task.tags == ["test"]
    print("✓ test_task_creation passed")


def test_task_manager_create_and_list():
    """Test TaskManager add and list operations."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = Path(f.name)
    
    try:
        manager = TaskManager(temp_file)
        
        # Add task
        task = manager.add_task("Buy groceries", "Milk and eggs", "2026-06-20", "high", ["shopping"])
        assert task.id == 1
        assert task.title == "Buy groceries"
        
        # List tasks
        tasks = manager.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == 1
        
        print("✓ test_task_manager_create_and_list passed")
    finally:
        temp_file.unlink()


def test_task_completion():
    """Test Task completion."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = Path(f.name)
    
    try:
        manager = TaskManager(temp_file)
        task = manager.add_task("Test task", "Description", "2026-06-25", "normal", [])
        
        # Complete task
        completed_task = manager.complete_task(1)
        assert completed_task.completed is True
        
        # Verify persistence
        tasks = manager.list_tasks(include_completed=True)
        assert tasks[0].completed is True
        
        print("✓ test_task_completion passed")
    finally:
        temp_file.unlink()


def test_task_deletion():
    """Test Task deletion."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = Path(f.name)
    
    try:
        manager = TaskManager(temp_file)
        manager.add_task("Task 1", "Desc 1", "2026-06-20", "normal", [])
        manager.add_task("Task 2", "Desc 2", "2026-06-21", "normal", [])
        
        # Delete task
        deleted = manager.delete_task(1)
        assert deleted.id == 1
        
        # Verify deletion
        remaining = manager.list_tasks()
        assert len(remaining) == 1
        assert remaining[0].id == 2
        
        print("✓ test_task_deletion passed")
    finally:
        temp_file.unlink()


def test_task_search():
    """Test Task search functionality."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = Path(f.name)
    
    try:
        manager = TaskManager(temp_file)
        manager.add_task("Buy groceries", "Milk and eggs", "2026-06-20", "high", ["shopping"])
        manager.add_task("Work project", "Implement features", "2026-06-25", "high", ["work"])
        manager.add_task("Call mom", "Weekly check-in", "2026-06-18", "normal", ["personal"])
        
        # Search by keyword
        results = manager.search_tasks("work")
        assert len(results) == 1
        assert "work" in results[0].title.lower()
        
        # Search by tag
        results = manager.search_tasks("shopping")
        assert len(results) == 1
        assert "shopping" in results[0].tags
        
        print("✓ test_task_search passed")
    finally:
        temp_file.unlink()


def test_task_filtering():
    """Test Task filtering."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = Path(f.name)
    
    try:
        manager = TaskManager(temp_file)
        manager.add_task("Urgent task", "High priority", "2026-06-20", "high", ["urgent"])
        manager.add_task("Normal task", "Regular priority", "2026-06-25", "normal", ["normal"])
        manager.add_task("Low task", "Low priority", "2026-07-01", "low", ["low"])
        
        # Filter by priority
        high_priority = manager.list_tasks(priority="high")
        assert len(high_priority) == 1
        assert high_priority[0].priority == "high"
        
        # Filter by tag
        urgent = manager.list_tasks(tag="urgent")
        assert len(urgent) == 1
        assert "urgent" in urgent[0].tags
        
        print("✓ test_task_filtering passed")
    finally:
        temp_file.unlink()


def test_task_stats():
    """Test Task statistics."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = Path(f.name)
    
    try:
        manager = TaskManager(temp_file)
        manager.add_task("Task 1", "Desc", "2026-06-20", "normal", [])
        manager.add_task("Task 2", "Desc", "2026-06-21", "normal", [])
        manager.add_task("Task 3", "Desc", "2026-06-22", "normal", [])
        
        manager.complete_task(1)
        
        stats = manager.stats()
        assert stats['total'] == 3
        assert stats['completed'] == 1
        assert stats['pending'] == 2
        
        print("✓ test_task_stats passed")
    finally:
        temp_file.unlink()


if __name__ == "__main__":
    print("Running tests...")
    print()
    test_task_creation()
    test_task_manager_create_and_list()
    test_task_completion()
    test_task_deletion()
    test_task_search()
    test_task_filtering()
    test_task_stats()
    print()
    print("✓ All tests passed!")
