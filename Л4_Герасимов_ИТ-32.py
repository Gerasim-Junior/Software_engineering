import json

file_tasks = "tasks.json"

def load_tasks():
    try:
        with open(file_tasks, "r", encoding="UTF-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Ошибка: {e}")
        return []

def save_task(tasks):
    try:
        with open(file_tasks, "w") as file:
            json.dump(tasks, file, indent=4)
    except ValueError as e:
        print(f"Ошибка: {e}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_task(tasks)
    print("\nЗадача добавлена!")

def edit_task(index, new_task):
    tasks = load_tasks()
    if 0 <= index <= len(tasks):
        tasks[index] = new_task
        save_task(tasks)
        print("\nЗадача изменена!")
    else:
        print("\nНекорректный номер задачи!")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_task(tasks)
        print("\nЗадача удалена!")
    else:
        raise ValueError("\nНекорретный номер задачи!")

def list_tasks():
    tasks = load_tasks()
    if tasks:
        print("\nСписок задач: ")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    else:
        print("Список задач пуст.")

def To_Do_List():
    try:
        while True:
            print("\nМеню:")
            print("1. Добавить задачу")
            print("2. Редактировать задачу")
            print("3. Удалить задачу")
            print("4. Показать список задач")
            print("5. Выйти")

            choice = input("\nВыберите операцию: ")

            if choice == "1":
                task = input("\nВведите задачу: ")
                add_task(task)

            elif choice == "2":
                list_tasks()
                index = int(input("\nВведите номер задачи для редактирования: ")) - 1
                new_task = input("Введите новый текст задачи: ")
                edit_task(index, new_task)

            elif choice == "3":
                list_tasks()
                index = int(input("Введите номер задачи для удаления: ")) - 1
                delete_task(index)

            elif choice == "4":
                list_tasks()

            elif choice == "5":
                print("Выход из программы.")
                break

            else:
                print("Некорректный операция, попробуйте снова!")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")



To_Do_List()
