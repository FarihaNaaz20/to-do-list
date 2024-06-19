import tkinter as tk
from tkinter import simpledialog, messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_frame = tk.Frame(master)
        self.task_frame.pack(padx=20, pady=20)

        self.task_listbox = tk.Listbox(self.task_frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task_name = simpledialog.askstring("Add Task", "Enter task name:")
        if task_name:
            self.tasks.append(task_name)
            self.update_task_list()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_name = simpledialog.askstring("Update Task", "Enter updated task name:", initialvalue=self.tasks[selected_index[0]])
            if task_name:
                self.tasks[selected_index[0]] = task_name
                self.update_task_list()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            response = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if response:
                del self.tasks[selected_index[0]]
                self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
