
TaskForge is a **console-based task manager** written in Python that allows users to efficiently create, update, filter, and manage tasks. Tasks are stored persistently in a JSON file, ensuring data is available across sessions.

---

## Features

- **Add Tasks**  
  Create tasks with a title, priority (Low/Medium/High), and due date.

- **View Tasks**  
  Display all tasks in a tabular format with details: ID, Title, Priority, Due Date, and Status.

- **Update Tasks**  
  Modify the title, priority, or due date of an existing task.

- **Mark as Complete**  
  Update a task's status to `Completed`.

- **Delete Tasks**  
  Permanently remove tasks from the system.

- **Filter Tasks**  
  - By **Status** → Pending or Completed.  
  - By **Due Date** → Tasks due Today or within This Week.

---

## Project Structure

TaskForge/

├── tasks forge.py 
└── README.md # Project documentation

---

## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/taskforge.git
cd taskforge

2. Run the Application
python task_manager.py

3. Use the Interactive Menu

=== 📌 TaskForge – Console-Based Task Manager ===
1. Add Task
2. View All Tasks
3. Update Task
4. Mark Task Complete
5. Delete Task
6. Filter Tasks
7. Save & Exit

## Example
Adding a Task

Enter task title: Write report
Enter priority (Low/Medium/High): High
Enter due date (YYYY-MM-DD): 2025-08-20

✅ Task added successfully!

📋 Task List:
----------------------------------------------------------------------
ID        Title               Priority  Due Date    Status
----------------------------------------------------------------------
a1b2c3d4  Write report        High      2025-08-20  Pending
----------------------------------------------------------------------

##Technical Details
Language: Python 3.x

Dependencies: No external dependencies (uses Python standard library only)

Storage: JSON file (tasks.json) for persistent task management

Classes
Task → Represents individual tasks.

TaskManager → Handles task operations (CRUD, filtering, saving/loading).

##License

License: Pranav
This project is licensed under the Pranav License. You may use, modify, and distribute it, but ownership and primary credit remain with Pranav.
