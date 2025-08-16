import json
import os
import uuid
from datetime import datetime, timedelta


class Task:
    def __init__(self, title, priority, due_date, status="Pending", task_id=None):
        self.id = task_id if task_id else str(uuid.uuid4())[:8]
        self.title = title
        self.priority = priority.capitalize()
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            priority=data["priority"],
            due_date=data["due_date"],
            status=data["status"],
            task_id=data["id"]
        )


class TaskManager:
    def __init__(self):
        self.task_list = []
        self.file_name = "tasks.json"
        self.load_from_file()

    def add_task(self):
        title = input("Enter task title: ").strip()
        priority = self.get_priority_input()
        due_date = self.get_date_input("Enter due date (YYYY-MM-DD): ")
        task = Task(title, priority, due_date)
        self.task_list.append(task)
        print("\n✅ Task added successfully!")

    def view_tasks(self, tasks=None):
        if tasks is None:
            tasks = self.task_list
        if not tasks:
            print("\n⚠ No tasks found.")
            return
        print("\n📋 Task List:")
        print("-" * 70)
        print(f"{'ID':<10}{'Title':<20}{'Priority':<10}{'Due Date':<12}{'Status':<10}")
        print("-" * 70)
        for task in tasks:
            print(f"{task.id:<10}{task.title:<20}{task.priority:<10}{task.due_date.strftime('%Y-%m-%d'):<12}{task.status:<10}")
        print("-" * 70)

    def update_task(self):
        task_id = input("Enter Task ID to update: ").strip()
        task = self.find_task_by_id(task_id)
        if task:
            print("\nLeave blank to keep current value.")
            title = input(f"Title ({task.title}): ").strip() or task.title
            priority = input(f"Priority ({task.priority}): ").strip().capitalize() or task.priority
            due_date = input(f"Due Date ({task.due_date}): ").strip()
            if due_date:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            else:
                due_date = task.due_date
            task.title = title
            task.priority = priority
            task.due_date = due_date
            print("\n✏ Task updated successfully!")
        else:
            print("❌ Task not found.")

    def mark_complete(self):
        task_id = input("Enter Task ID to mark complete: ").strip()
        task = self.find_task_by_id(task_id)
        if task:
            task.status = "Completed"
            print("✅ Task marked as completed!")
        else:
            print("❌ Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ").strip()
        task = self.find_task_by_id(task_id)
        if task:
            self.task_list.remove(task)
            print("🗑 Task deleted successfully!")
        else:
            print("❌ Task not found.")

    def filter_tasks(self):
        print("\nFilter by:\n1. Status\n2. Due Date")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            status = input("Enter status (Pending/Completed): ").capitalize()
            filtered = [t for t in self.task_list if t.status == status]
            self.view_tasks(filtered)
        elif choice == "2":
            print("1. Today\n2. This Week")
            date_choice = input("Enter choice: ").strip()
            today = datetime.today().date()
            if date_choice == "1":
                filtered = [t for t in self.task_list if t.due_date == today]
            elif date_choice == "2":
                week_end = today + timedelta(days=7)
                filtered = [t for t in self.task_list if today <= t.due_date <= week_end]
            else:
                print("❌ Invalid choice.")
                return
            self.view_tasks(filtered)
        else:
            print("❌ Invalid choice.")

    def save_to_file(self):
        with open(self.file_name, "w") as f:
            json.dump([t.to_dict() for t in self.task_list], f, indent=4)

    def load_from_file(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                data = json.load(f)
                self.task_list = [Task.from_dict(item) for item in data]

    def find_task_by_id(self, task_id):
        return next((t for t in self.task_list if t.id == task_id), None)

    @staticmethod
    def get_priority_input():
        while True:
            priority = input("Enter priority (Low/Medium/High): ").strip().capitalize()
            if priority in ["Low", "Medium", "High"]:
                return priority
            print("❌ Invalid priority. Please enter Low, Medium, or High.")

    @staticmethod
    def get_date_input(prompt):
        while True:
            try:
                date_str = input(prompt).strip()
                return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                print("❌ Invalid date format. Please use YYYY-MM-DD.")


def main():
    manager = TaskManager()
    while True:
        print("\n=== 📌 TaskForge – Console-Based Task Manager ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Mark Task Complete")
        print("5. Delete Task")
        print("6. Filter Tasks")
        print("7. Save & Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.update_task()
        elif choice == "4":
            manager.mark_complete()
        elif choice == "5":
            manager.delete_task()
        elif choice == "6":
            manager.filter_tasks()
        elif choice == "7":
            manager.save_to_file()
            print("💾 Data saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
