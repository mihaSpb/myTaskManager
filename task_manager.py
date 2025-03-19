import json
import os


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str):
        task = {'description': description, 'completed': False}
        self.tasks.append(task)

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            raise IndexError("Task index out of range")

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Task index out of range")

    def save_to_json(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def load_from_json(self, filename: str):
        if not os.path.exists(filename):
            print("Файл не найден. Список задач пуст.")
            self.tasks = []
            return
        with open(filename, 'r', encoding='utf-8') as file:
            self.tasks = json.load(file)

    def display_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Выполнена" if task['completed'] else "Не выполнена"
                print(f"{index}: {task['description']} [{status}]")


class TaskManagerUI:
    def __init__(self, manager: TaskManager):
        self.manager = manager

    def add_task_action(self):
        description = input("Введите описание задачи: ")
        self.manager.add_task(description)
        print("Задача добавлена.")

    def complete_task_action(self):
        try:
            index = int(input("Введите индекс задачи для отметки выполнения: "))
            self.manager.complete_task(index)
            print("Задача отмечена как выполненная.")
        except (ValueError, IndexError) as e:
            print("Ошибка:", e)

    def remove_task_action(self):
        try:
            index = int(input("Введите индекс задачи для удаления: "))
            self.manager.remove_task(index)
            print("Задача удалена.")
        except (ValueError, IndexError) as e:
            print("Ошибка:", e)

    def display_tasks_action(self):
        print("\nСписок задач:")
        self.manager.display_tasks()

    def save_tasks_action(self):
        try:
            self.manager.save_to_json("tasks.json")
            print("Задачи сохранены в tasks.json.")
        except Exception as e:
            print("Ошибка при сохранении:", e)

    def load_tasks_action(self):
        try:
            self.manager.load_from_json("tasks.json")
            print("Задачи загружены из tasks.json:")
            self.manager.display_tasks()
        except Exception as e:
            print("Ошибка при загрузке:", e)


def main():
    manager = TaskManager()
    ui = TaskManagerUI(manager)

    menu_options = {
        "1": ("Добавить задачу", lambda: ui.add_task_action()),
        "2": ("Отметить задачу как выполненную", lambda: ui.complete_task_action()),
        "3": ("Удалить задачу", lambda: ui.remove_task_action()),
        "4": ("Вывести список задач", lambda: ui.display_tasks_action()),
        "5": ("Сохранить задачи в JSON (tasks.json)", lambda: ui.save_tasks_action()),
        "6": ("Загрузить задачи из JSON (tasks.json)", lambda: ui.load_tasks_action()),
        "7": ("Выход", None)
    }

    while True:
        print("\nМенеджер задач:")
        for key, (desc, _) in menu_options.items():
            print(f"{key}. {desc}")
        choice = input("Выберите опцию: ")

        if choice in menu_options:
            if choice == "7":
                print("Выход из программы.")
                break
            else:
                action = menu_options[choice][1]
                action()
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == '__main__':
    main()