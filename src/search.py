"""Поиск и фильтрация задач."""


def search_tasks(tasks, query):
    """Возвращает задачи, в названии которых есть query (без учёта регистра)."""
    query = query.strip().lower()
    return [task for task in tasks if query in task["title"].lower()]


def filter_by_status(tasks, done):
    """Возвращает задачи с нужным статусом: выполненные или нет."""
    return [task for task in tasks if task["done"] == done]
