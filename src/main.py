"""Консольный менеджер задач."""

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
    """Удаляет задачу по номеру. Возвращает True, если задача найдена."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False


def main():
    while True:
        print("\n1. Добавить задачу\n2. Показать задачи\n3. Выполнить задачу\n0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            add_task(input("Название задачи: "))
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            if not complete_task(int(input("Номер задачи: "))):
                print("Задача не найдена.")
        elif choice == "0":
            break


if __name__ == "__main__":
    main()
