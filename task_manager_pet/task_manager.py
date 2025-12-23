import json
import os
import tkinter as tk
from tkinter import messagebox

file_name = "tasks.json"


def load_tasks():
    if not os.path.exists(file_name):
        return []

    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


def add_task(text):
    tasks = load_tasks()
    new_task = {"id": len(tasks) + 1, "text": text, "done": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print("Задача добавлена! ✅")


def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]

    for i, t in enumerate(tasks, start=1):
        t["id"] = i

    save_tasks(tasks)
    print("Задача удалена! 🗑️")


def show_tasks():
    tasks = load_tasks()

    if not tasks:
        print("Нет задач.")
        return

    for task in tasks:
        status = "✅" if task["done"] else "❌"
        print(f"{task['id']}. [{status}] {task['text']}")


def search_tasks(keyword):
    tasks = load_tasks()
    results = [t for t in tasks if keyword.lower() in t["text"].lower()]

    if not results:
        print("Ничего не найдено.")
        return

    for task in results:
        print(f"{task['id']}. {task['text']}")


def mark_done(task_id):
    tasks = load_tasks()

    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True

    save_tasks(tasks)
    print("Задача отмечена как выполненная! ✅")

### TKinter

def add_task_gui():
    text = entry.get()
    if text:
        add_task(text)
        entry.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Ошибка!", "Введите текст задачи!")


def refresh_tasks():
    listbox.delete(0, tk.END)
    tasks = load_tasks()
    for t in tasks:
        status = "✅" if t["done"] else "❌"
        listbox.insert(tk.END, f"{t['id']}. [{status}] {t['text']}")


def delete_task_gui():
    try:
        selection = listbox.curselection()[0]
        task_line = listbox.get(selection)
        task_id = int(task_line.split(".")[0])
        delete_task(task_id)
        refresh_tasks()
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу для удаления!")


def mark_done_gui():
    try:
        selection = listbox.curselection()[0]
        task_line = listbox.get(selection)
        task_id = int(task_line.split(".")[0])
        mark_done(task_id)
        refresh_tasks()
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу для отметки!")


window = tk.Tk()
window.geometry("500x400")
window.title("Таск-менеджер")

listbox = tk.Listbox(window, width=50)
listbox.pack()

entry = tk.Entry(window, width=50, bg="white", fg="black")
entry.pack(padx=5, pady=5)

frame = tk.Frame(window)
frame.pack(pady=5)

add_btn = tk.Button(frame, text="Добавить", width=15, command=add_task_gui)
add_btn.grid(row=0, column=0, padx=5, pady=5)

delete_btn = tk.Button(frame, text="Удалить", width=15, command=delete_task_gui)
delete_btn.grid(row=0, column=1, padx=5, pady=5)

done_btn = tk.Button(frame, text="Выполнено", width=15, command=mark_done_gui)
done_btn.grid(row=1, column=0, padx=5, pady=5)

refresh_button = tk.Button(frame, text="Обновить", width=15, command=refresh_tasks)
refresh_button.grid(row=1, column=1, padx=5, pady=5)

window.mainloop()
