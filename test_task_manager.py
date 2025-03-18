import pytest
from task_manager import TaskManager


@pytest.fixture
def task_manager():
    return TaskManager()


def test_add_and_complete_task(task_manager):
    task_manager.add_task("Тестовая задача")
    assert len(task_manager.tasks) == 1, "Задача не была добавлена"

    task_manager.complete_task(0)
    assert task_manager.tasks[0]['completed'] is True, "Статус задачи не изменился на True"


def test_remove_task(task_manager):
    task_manager.add_task("Задача для удаления")
    assert len(task_manager.tasks) == 1, "Задача не была добавлена"

    task_manager.remove_task(0)
    assert len(task_manager.tasks) == 0, "Задача не была удалена"


def test_save_and_load_json(tmp_path, task_manager):
    task_manager.add_task("Задача 1")
    task_manager.add_task("Задача 2")
    task_manager.complete_task(1)

    temp_file = tmp_path / "tasks.json"
    task_manager.save_to_json(str(temp_file))

    new_manager = TaskManager()
    new_manager.load_from_json(str(temp_file))

    assert new_manager.tasks == task_manager.tasks, "Загруженные данные не совпадают с сохраненными"