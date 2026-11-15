import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from search import search_tasks, filter_by_status

TASKS = [
    {"id": 1, "title": "Купить хлеб", "done": False},
    {"id": 2, "title": "Написать отчёт", "done": True},
]


def test_search_tasks():
    assert search_tasks(TASKS, "ХЛЕБ") == [TASKS[0]]
    assert search_tasks(TASKS, "яблоко") == []


def test_filter_by_status():
    assert filter_by_status(TASKS, True) == [TASKS[1]]
    assert filter_by_status(TASKS, False) == [TASKS[0]]
