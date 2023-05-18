import sqlite3


def insert_user(telegram_id, full_name, contact):
    database = sqlite3.connect("bot.db")
    cursor = database.cursor()

    cursor.execute('''
    INSERT INTO users(telegram_id, full_name, contact)
    VALUES (?, ?, ? ) ''', (telegram_id, full_name, contact))

    database.commit()
    database.close()


def insert_users_lang(telegram_id):
    database = sqlite3.connect("bot.db")
    cursor = database.cursor()

    cursor.execute('''
        INSERT OR IGNORE INTO users_lang(telegram_id)
        VALUES (?) ''', (telegram_id,))

    database.commit()
    database.close()


def update_users_lang(telegram_id, language):
    database = sqlite3.connect("bot.db")
    cursor = database.cursor()

    cursor.execute('''
        UPDATE  users_lang
        SET users_lang = ?
        WHERE telegram_id  = ?
         ''', (language, telegram_id))

    database.commit()
    database.close()


def get_user_lang(telegram_id):
    database = sqlite3.connect("bot.db")
    cursor = database.cursor()

    cursor.execute('''
        SELECT   users_lang
        FROM users_lang 
        WHERE telegram_id  = ?
         ''', (telegram_id,))
    user_language = cursor.fetchone()[0]
    return user_language


def get_all_users():
    database = sqlite3.connect("mybot.db")
    cursor = database.cursor()
    cursor.execute("""
    SELECT telegram_id FROM users;
    """, )
    users = cursor.fetchall()
    users_tg_ids = []

    for user in users:
        users_tg_ids.append(user[0])
    database.close()

    return users_tg_ids
