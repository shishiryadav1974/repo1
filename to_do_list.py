class TodoList:
    def __init__(self):
        self.tasks = []  # store tasks

    def add_task(self, task):
        self.tasks.append(task)
        print(f" Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print(" No tasks yet.")
        else:
            print("\nCurrent to‑do list:")
            for i, t in enumerate(self.tasks, 1):
                print(f"{i}. {t}")

    def delete_task(self, idx):
        try:
            removed = self.tasks.pop(idx - 1)
            print(f" Removed task: {removed}")
        except IndexError:
            print(" Invalid index.")

def main():
    todo = TodoList()
    while True:
        print("\nChoose: (A)dd, (V)iew, (D)elete, (Q)uit")
        choice = input("Your choice: ").strip().upper()
        if choice == 'A':
            task = input("Enter task: ").strip()
            if task: todo.add_task(task)
        elif choice == 'V':
            todo.view_tasks()
        elif choice == 'D':
            todo.view_tasks()
            try:
                i = int(input("Index to delete: "))
                todo.delete_task(i)
            except ValueError:
                print("Please enter a number.")
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()