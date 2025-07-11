# Tskord

A simple Discord bot made in Python to manage a to-do list directly on your server.

## About the Bot

Tskord allows you and your server members to add, view, and mark tasks as complete. It uses a SQLite database to persist data, ensuring your tasks are not lost.

## Features

  * **Add Tasks:** Add new tasks to your list.
  * **List Tasks:** View all tasks, only the unfinish ones, or only the completed ones.
  * **Mark as finish:** Mark tasks as finished.
  * **Data Persistence:** Tasks are saved in a `tasks.db` database file.

## Tech Stack

  * **Python:** The main language for the project.
  * **discord.py:** A library for interacting with the Discord API.
  * **SQLite3:** The database used for task storage.

## Getting Started

Follow the steps below to set up and run the bot on your own Discord server.

### **Prerequisites**

  * [Python 3.8+](https://www.python.org/downloads/)
  * A Discord account and a server where you have permission to add bots.
  * A Discord bot token. You can create one on the [Discord Developer Portal](https://discord.com/developers/applications).

### **Installation**

1.  **Clone the repository:**

    ```bash
    git clone https://YOUR-USERNAME/YOUR-REPOSITORY.git
    cd YOUR-REPOSITORY
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**

      * Create a file named `.env` in the root of the project.
      * Inside the `.env` file, add your bot token:
        ```
        DISCORD_TOKEN=YOUR_TOKEN_HERE
        ```

### **Running the Bot**

To start the bot, run the `main.py` file:

```bash
python main.py
```

If everything is configured correctly, you will see a message in your terminal confirming that the bot is online, and it will appear as active on your Discord server.

## 📝 Bot Commands

Here are the available commands to interact with the TaskBot:

| Command | Description | Example |
|---|---|---|
| `!add <task>` | Adds a new task to the list. | `!add Create the README` |
| `!unfinished` | Lists all pending tasks. | `!unfinish` |
| `!finished` | Lists all completed tasks. | `!finish` |
| `!list` | Lists all tasks (🟢/🔴). | `!list` |
| `!finish <id>` | Marks a task as completed. | `!finish 1` |
| `!about` | Shows information about the bot. | `!about` |
| `!h` | Displays the help message. | `!h` |
