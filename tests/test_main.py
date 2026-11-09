import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from main import add_task, complete_task
def test_add_task():
tasks = []
add_task(tasks, "Тест")

assert tasks[0]["title"] == "Тест"
assert tasks[0]["done"] is False
def test_complete_task():
tasks = []
add_task(tasks, "Тест")
complete_task(tasks, 1)
assert tasks[0]["done"] is True
