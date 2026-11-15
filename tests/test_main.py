import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import main


def test_add_task():
    main.tasks.clear()
    task = main.add_task("Купить хлеб")
    assert task["title"] == "Купить хлеб"
    assert task["done"] is False


def test_complete_task():
    main.tasks.clear()
    main.add_task("Тест")
    assert main.complete_task(1) is True
    assert main.complete_task(99) is False
