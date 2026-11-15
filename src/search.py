"""Поиск и фильтрация задач."""


def search_tasks(tasks, query):
    """Возвращает задачи, в названии которых есть query (без учёта регистра)."""
    query = query.strip().lower()
    return [task for task in tasks if query in task["title"].lower()]
