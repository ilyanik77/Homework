import sqlite3

con = sqlite3.connect('DataBase/users.db')
cur = con.cursor()

# Создаем таблицу
cur.execute("""CREATE TABLE if not exists users(id integer Primary Key, firstname text, lastname text, phone number, description text);""")
con.commit()


# Добавление данных в таблицу
def add_data( user):

    cur = con.cursor()

    cur.execute("""INSERT INTO users(firstname, lastname, phone, description) VALUES (?, ?, ?, ?)""",  user)

    con.commit()


# Обновление данных в таблице
def update_data( index, lastname):
    cur = con.cursor()

    cur.execute(f"UPDATE users SET lastname = '{lastname}' WHERE id = {index}")

    con.commit()


# Обновление номера телефона
def update_tel( index, tel):
    cur = con.cursor()

    cur.execute(f"UPDATE users SET phone = '{tel}' WHERE id = {index}")

    con.commit()

# Печать таблицы
def print_all_data():
    cur = con.cursor()

    cur.execute("""SELECT * FROM users""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    con.commit()

# Печать данных сотрудника
def print_user_data(index):
    cur = con.cursor()

    cur.execute(f"SELECT * FROM users WHERE id = {index}") # по индексу

    res = cur.fetchall()
    for row in res:
        print(row)

    con.commit()

# Удаление данных сотрудника
def delete_user(index):
    cur = con.cursor()

    cur.execute(f"DELETE  FROM users WHERE id = {index}") # по индексу


    con.commit()

# Удаление таблицы
def delete_data():
    cur = con.cursor()
    cur.execute("""'DROP table if exists users'""")


    con.commit()


    con.close()
