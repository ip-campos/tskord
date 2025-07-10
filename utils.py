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
                   VALUES ('{task}')""")

def finish_task(id:int) -> None:
    """Changes the status of the task with id"""
    cursor.execute(f"""UPDATE tasks
                   SET done = 1
                   WHERE id = {id};""")

def get_undone_tasks() -> list[tuple[int, str, bool]]:
    """returns all undone tasks"""
    tasks = cursor.execute("""SELECT *
                           FROM tasks
                           WHERE done = 0;""").fetchall()
    return tasks


    


