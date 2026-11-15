"""Консольный менеджер задач."""

tasks = []

MENU = """
==== Менеджер задач ====
1. Добавить задачу
2. Показать задачи
3. Выполнить задачу
0. Выход
========================"""


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
    print("Ваши задачи:")
    for task in tasks:
        mark = "[x]" if task["done"] else "[ ]"
        print(f"{task['id']}. {mark} {task['title']}")
    done = sum(1 for task in tasks if task["done"])
    print(f"Выполнено: {done} из {len(tasks)}")


def complete_task(task_id):
    """Отмечает задачу выполненной. Возвращает True, если задача найдена."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def main():
    while True:
        print(MENU)
        choice = input("Выберите действие: ")
        if choice == "1":
            add_task(input("Название задачи: "))
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Номер задачи: "))
            except ValueError:
                print("Нужно ввести число.")
                continue
            if not complete_task(task_id):
                print("Задача не найдена.")
        elif choice == "0":
            break
        else:
            print("Неизвестная команда, попробуйте ещё раз.")


if __name__ == "__main__":
    main()
