import sqlite3

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               task varchar(255),
               done bool DEFAULT 0
               );""")

def add_task(task: str):
    cursor.execute(f"""INSERT INTO tasks (task)
                   VALUES ('{task}')""")

def finish_task(id):
    cursor.execute(f"""UPDATE tasks
                   SET done = 1
                   WHERE id = {id};""")

def get_undone_tasks():
    tasks = cursor.execute("""SELECT *
                           FROM tasks
                           WHERE done = 0;""")
    return tasks
    
