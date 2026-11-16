"""Консольный менеджер задач v2.0 (feature-версия)."""

tasks = []


def add_task(title):
    """Добавляет задачу в список."""
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    return task


def show_tasks():
    """Выводит все задачи на экран."""
    if not tasks:
        print("Список задач пуст.")
        return
    for task in tasks:
        mark = "[x]" if task["done"] else "[ ]"
        print(f"{task['id']}. {mark} {task['title']}")


def complete_task(task_id):
    """Отмечает задачу выполненной. Возвращает True, если задача найдена."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def delete_task(task_id):
    """Удаляет задачу по её номеру. Возвращает True, если задача найдена."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False


def validate_title(title):
    """Возвращает очищенное название или None, если оно пустое."""
    title = title.strip()
    if not title:
        return None
    return title


def read_task_id():
    """Запрашивает номер задачи. Возвращает число или None при неверном вводе."""
    text = input("Номер задачи: ")
    if not text.isdigit():
        print("Нужно ввести целое положительное число.")
        return None
    return int(text)


def main():
    while True:
        print("\n1. Добавить задачу\n2. Показать задачи\n3. Выполнить задачу\n4. Удалить задачу\n0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            title = validate_title(input("Название задачи: "))
            if title is None:
                print("Название не может быть пустым.")
            else:
                add_task(title)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            task_id = read_task_id()
            if task_id is not None and not complete_task(task_id):
                print("Задача не найдена.")
        elif choice == "4":
            task_id = read_task_id()
            if task_id is not None and not delete_task(task_id):
                print("Задача не найдена.")
        elif choice == "0":
            break
        else:
            print("Неизвестная команда, попробуйте ещё раз.")


if __name__ == "__main__":
    main()
