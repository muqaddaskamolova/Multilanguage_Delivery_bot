import sqlite3

database = sqlite3.connect("bot.db")
cursor = database.cursor()


def create_users_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER BIGINT UNIQUE ,
    full_name TEXT,
    contact TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users_lang(
    user_lang_id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE ,
    users_lang TEXT DEFAULT ''
      )
    """)


create_users_table()
database.commit()
database.close()
