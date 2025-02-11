import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Loads tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Saves tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Displays the current task list."""
    if not tasks:
        print("📜 No tasks available.")
    else:
        print("\n📋 To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Adds a new task to the list."""
    task = input("➕ Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!")

def remove_task(tasks):
    """Removes a task by its number."""
    display_tasks(tasks)
    try:
        task_num = int(input("❌ Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"🗑️ Removed task: {removed_task}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def mark_task_done(tasks):
    """Marks a task as completed."""
    display_tasks(tasks)
    try:
        task_num = int(input("✔️ Enter task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num] += " ✅ (Completed)"
            save_tasks(tasks)
            print(f"🎯 Task marked as completed: {tasks[task_num]}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    """Main loop for the To-Do List application."""
    tasks = load_tasks()

    while True:
        print("\n📌 Choose an option:")
        print("1️⃣ View tasks")
        print("2️⃣ Add task")
        print("3️⃣ Remove task")
        print("4️⃣ Mark task as completed")
        print("5️⃣ Exit")

        choice = input("➡️ Enter your choice: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select a valid option.")

# Run the To-Do List application
if __name__ == "__main__":
    main()
