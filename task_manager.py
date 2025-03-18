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
        with open(filename, 'r', encoding='utf-8') as file:
            self.tasks = json.load(file)


def display_tasks(task_manager):
    if not task_manager.tasks:
        print("Список задач пуст.")
    else:
        for index, task in enumerate(task_manager.tasks):
            status = "Выполнена" if task['completed'] else "Не выполнена"
            print(f"{index}: {task['description']} [{status}]")


def main():
    manager = TaskManager()
    while True:
        print("\nМенеджер задач:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Удалить задачу")
        print("4. Вывести список задач")
        print("5. Сохранить задачи в JSON (tasks.json)")
        print("6. Загрузить задачи из JSON (tasks.json)")
        print("7. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            manager.add_task(description)
            print("Задача добавлена.")
        elif choice == '2':
            try:
                index = int(input("Введите индекс задачи для отметки выполнения: "))
                manager.complete_task(index)
                print("Задача отмечена как выполненная.")
            except (ValueError, IndexError) as e:
                print("Ошибка:", e)
        elif choice == '3':
            try:
                index = int(input("Введите индекс задачи для удаления: "))
                manager.remove_task(index)
                print("Задача удалена.")
            except (ValueError, IndexError) as e:
                print("Ошибка:", e)
        elif choice == '4':
            print("\nСписок задач:")
            display_tasks(manager)
        elif choice == '5':
            try:
                manager.save_to_json("tasks.json")
                print("Задачи сохранены в tasks.json.")
            except Exception as e:
                print("Ошибка при сохранении:", e)
        elif choice == '6':
            try:
                manager.load_from_json("tasks.json")
                print("Задачи загружены из tasks.json:")
                display_tasks(manager)
            except Exception as e:
                print("Ошибка при загрузке:", e)
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == '__main__':
    main()