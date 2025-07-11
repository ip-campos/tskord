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
               done bool DEFAULT 0,
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
    undone_tasks = cursor.execute("""SELECT *
                                  FROM tasks
                                  WHERE done = 0 AND user_id = (?) AND guild_id = (?)
                                  ORDER BY id;""", (user_id, guild_id)).fetchall()
    real_id = undone_tasks[int(task_id)-1][0]
    cursor.execute(f"""UPDATE tasks
                   SET done = 1
                   WHERE id = (?) AND user_id = (?) AND guild_id = (?);""", (real_id, user_id, guild_id))
    conn.commit()

def get_undone_tasks(user_id, guild_id) -> str:
    """returns a string of all undone tasks"""
    undone_str = ""
    tasks = cursor.execute("""SELECT task
                           FROM tasks
                           WHERE done = 0 AND user_id = (?) AND guild_id = (?)
                           ORDER BY id;""", (user_id, guild_id)).fetchall()
    for i in enumerate(tasks, start=1):
        undone_str += f"{i[0]} - {i[1][0]}\n"
    return undone_str

def get_done_tasks(user_id:int, guild_id:int)->str:
    """returns a string of all done tasks"""
    done_str = ""
    tasks = cursor.execute("""SELECT task
                           FROM tasks
                           WHERE done = 1 AND user_id = (?) AND guild_id = (?)
                           ORDER BY id;""", (user_id, guild_id)).fetchall()
    for i in enumerate(tasks, start=1):
        done_str += f"{i[0]} - {i[1][0]}\n"
    return done_str

def get_all_tasks(user_id:int, guild_id:int)->str:
    """returns a string of all tasks"""
    tasks_str = ""
    tasks = cursor.execute("""SELECT task, done
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