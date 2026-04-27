import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Введите задачу: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Задача добавлена!")

def show_tasks(tasks):
    if not tasks:
        print("Нет задач.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Введите номер задачи для удаления: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Удалено!")
    except:
        print("Ошибка!")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()