def add_task(tasks, title):
tasks.append({"title": title, "done": False})
def list_tasks(tasks):
if not tasks:
print("Список задач пуст")
return
for i, task in enumerate(tasks, 1):
mark = "x" if task["done"] else " "
print(f"{i}. [{mark}] {task['title']}"
def complete_task(tasks, index):
tasks[index - 1]["done"] = True
def main():
tasks = []
add_task(tasks, "Купить молоко")
add_task(tasks, "Сделать лабораторную")
complete_task(tasks, 1)
list_tasks(tasks)
if __name__ == "__main__":
main()
