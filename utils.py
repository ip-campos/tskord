import sqlite3

#Connect to local database
conn = sqlite3.connect('tasks.db') 
cursor = conn.cursor()

#Create tasks table
cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id integer NOT NULL,
               guild_id integer NOT NULL,
               task varchar(255),
               finished bool DEFAULT 0,
               created_at date DEFAULT (DATE('now', 'localtime'))
               );""")

#+---------------------- functions ----------------------+
def add_task(task: str, user_id:int, guild_id:int) -> None:
    """Insert a task into tasks table"""
    cursor.execute(f"""INSERT INTO tasks (task, user_id, guild_id)
                   VALUES ((?), (?), (?))""", (task, user_id, guild_id))
    conn.commit()

def finish_task(task_id:int, user_id:int, guild_id:int) -> None:
    """Changes the status of the task with id"""
    unfinished_tasks = cursor.execute("""SELECT *
                                  FROM tasks
                                  WHERE finished = 0 AND user_id = (?) AND guild_id = (?)
                                  ORDER BY id;""", (user_id, guild_id)).fetchall()
    real_id = unfinished_tasks[int(task_id)-1][0]
    cursor.execute(f"""UPDATE tasks
                   SET finished = 1
                   WHERE id = (?) AND user_id = (?) AND guild_id = (?);""", (real_id, user_id, guild_id))
    conn.commit()

def get_unfinished_tasks(user_id, guild_id) -> str:
    """returns a string of all unfinished tasks"""
    unfinished_str = ""
    tasks = cursor.execute("""SELECT task
                           FROM tasks
                           WHERE finished = 0 AND user_id = (?) AND guild_id = (?)
                           ORDER BY id;""", (user_id, guild_id)).fetchall()
    for i in enumerate(tasks, start=1):
        unfinished_str += f"{i[0]} - {i[1][0]}\n"
    return unfinished_str

def get_finished_tasks(user_id:int, guild_id:int)->str:
    """returns a string of all finished tasks"""
    finished_str = ""
    tasks = cursor.execute("""SELECT task
                           FROM tasks
                           WHERE finished = 1 AND user_id = (?) AND guild_id = (?)
                           ORDER BY id;""", (user_id, guild_id)).fetchall()
    for i in enumerate(tasks, start=1):
        finished_str += f"{i[0]} - {i[1][0]}\n"
    return finished_str

def get_all_tasks(user_id:int, guild_id:int)->str:
    """returns a string of all tasks"""
    tasks_str = ""
    tasks = cursor.execute("""SELECT task, finished
                           FROM tasks
                           WHERE user_id = (?) AND guild_id = (?)
                           ORDER BY id;""", (user_id, guild_id)).fetchall()
    for i in enumerate(tasks, start=1):
        if i[1][1]:
            tasks_str += f"{i[0]} - {i[1][0]} 🟢\n"
        else:
            tasks_str += f"{i[0]} - {i[1][0]} 🔴\n"
    return tasks_str

#+---------------------- information ----------------------+
help_text = """
**Commands:**
📝 **!add <task>**
- Adds a task to your list

📋 **!unfinished**
- Lists all unfinished tasks

📋 **!finished**
- Lists all finished tasks

📋 **!list**
- Lists all tasks

✅ **!finish <task_id>**
- marks the task as finished

❓ **!about**
- Information about the bot

🆘 **!h**
- Help message
"""

about = """🤖A task list bot for your server"""