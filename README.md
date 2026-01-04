# Telegram Mood & Compliment Bot 🤖

A friendly Telegram bot built with **Python** to send **compliments** and **mood-based messages** in a group chat. This bot is designed to provide positivity, motivation, and interactive engagement for users.
## Features 
- **Compliment Generator** – Sends a random compliment from a pre-defined list.
- **Mood Messages** – Sends mood-based messages for `happy`, `sad`, `stressed`, or `love`.
- **Group Only Access** – Works only in a specified Telegram group to keep interactions private.
- **Easy Commands**:
  - `/start` – Starts the bot and confirms it is active.
  - `/compliment` – Sends a random compliment.
  - `/mood <mood>` – Sends a random message based on mood. Example: `/mood happy`.
## Tech Stack 
- **Python 3.10+** – Programming language used.
- **python-telegram-bot** – Official Telegram bot library for Python.
- **Random Module** – For selecting random messages from lists.
- **Scheduler (Optional)** – Can be used to send messages automatically at specific times.
- **Configuration Files**:
  - `config.py` – Stores sensitive data like `BOT_TOKEN` and `GROUP_ID`.
  - `messages.py` – Stores all compliments and mood messages.

## How it Works 
1. The bot uses **Telegram’s Bot API** via the `python-telegram-bot` library.
2. When a command like `/compliment` or `/mood happy` is triggered in the group, the bot:
   - Picks a random message from the corresponding list (`compliments` or `mood_messages`).
   - Sends the message to the group chat.
3. `/mood` checks if the mood entered is valid (`happy`, `sad`, `stressed`, `love`).  
   If invalid, it prompts the user to try again.
4. `/start` simply confirms the bot is active in the group.
