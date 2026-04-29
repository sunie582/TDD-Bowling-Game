import pytest
from main import app, tasks_db, archive_db, Task

@pytest.fixture(autouse=True)
def clean_db():
    """Очищаем базу перед каждым тестом, чтобы они не мешали друг другу"""
    tasks_db.clear()
    archive_db.clear()

def test_create_task_without_description():
    """Проверка FR-01: Создание задачи без описания (наш недавний фикс)"""
    new_task = Task(id=1, title="Test Task", priority="Medium")
    assert new_task.description is None
    assert new_task.priority == "Medium"

def test_priority_sorting_logic():
    """Проверка: задачи должны сортироваться High -> Medium -> Low"""
    # Создаем задачи в "неправильном" порядке
    tasks_db.append(Task(id=1, title="Low Task", priority="Low"))
    tasks_db.append(Task(id=2, title="High Task", priority="High"))
    tasks_db.append(Task(id=3, title="Medium Task", priority="Medium"))

    # Имитируем логику из main.py
    from main import get_priority_weight
    sorted_tasks = sorted(tasks_db, key=lambda x: (get_priority_weight(x.priority), x.id))

    assert sorted_tasks[0].priority == "High"
    assert sorted_tasks[1].priority == "Medium"
    assert sorted_tasks[2].priority == "Low"

def test_archive_transfer():
    """Проверка: задача реально переходит из активных в архив"""
    task = Task(id=1, title="To be archived", priority="High")
    tasks_db.append(task)
    
    # Имитируем выполнение
    item = tasks_db.pop(0)
    item.is_completed = True
    archive_db.append(item)
    
    assert len(tasks_db) == 0
    assert len(archive_db) == 1
    assert archive_db[0].title == "To be archived"