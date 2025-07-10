import sqlite3

#Connect to local database
conn = sqlite3.connect('tasks.db') 
cursor = conn.cursor()

#Create tasks table
cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               task varchar(255),
               done bool DEFAULT 0,
               created_at date DEFAULT (DATE('now', 'localtime'))
               );""")

#+---------------------- functions ----------------------+
def add_task(task: str) -> None:
    """Insert a task into tasks table"""
    cursor.execute(f"""INSERT INTO tasks (task)
                   VALUES (?)""", (task,))
    conn.commit()

def finish_task(id:int) -> None:
    """Changes the status of the task with id"""
    cursor.execute(f"""UPDATE tasks
                   SET done = 1
                   WHERE id = (?);""", (id,))
    conn.commit

def get_undone_tasks() -> list[tuple[int, str, bool]]:
    """returns a string of all undone tasks"""
    undone_str = ""
    tasks = cursor.execute("""SELECT *
                           FROM tasks
                           WHERE done = 0
                           ORDER BY id;""").fetchall()
    for i in enumerate(tasks, start=1):
        undone_str += f"{i[0]} - {i[1][1]}\n"
    return undone_str

def get_real_id(cur_id):
    undone_tasks = cursor.execute("""SELECT *
                                  FROM tasks
                                  WHERE done = 0
                                  ORDER BY id;""").fetchall()
    real_id = undone_tasks[int(cur_id)-1][0]
    return real_id

def get_done_tasks():
    """returns a string of all done tasks"""
    done_str = ""
    tasks = cursor.execute("""SELECT *
                           FROM tasks
                           WHERE done = 1
                           ORDER BY id;""").fetchall()
    for i in enumerate(tasks, start=1):
        done_str += f"{i[0]} - {i[1][1]}\n"
    return done_str

def get_all_tasks():
    """returns a string of all tasks"""
    tasks_str = ""
    tasks = cursor.execute("""SELECT *
                           FROM tasks
                           ORDER BY id;""").fetchall()
    for i in tasks:
        if i[2]:
            tasks_str += f"{i[0]} - {i[1]} 🟢\n"
        else:
            tasks_str += f"{i[0]} - {i[1]} 🔴\n"
    return tasks_str

#+---------------------- information ----------------------+
help_text = """
**Commands:**
📝 **!add <task>**
- Adds a task to your list

📋 **!undone**
- Lists all undone tasks

📋 **!done**
- Lists all done tasks

📋 **!list**
- Lists all tasks

✅ **!finish <task_id>**
- marks the task as done

❓ **!about**
- Information about the bot

🆘 **!h**
- Help message
"""

about = """🤖A task list bot for your server"""