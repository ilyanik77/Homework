import sqlite3

from aiogram import Bot, Dispatcher, executor, types

TOKEN = '5506297546:AAGidLGr4eYLatT8qgMjelq-VaJrfUKw5cY'

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

con = sqlite3.connect('Telegram-bot/users.db')
cur = con.cursor()
cur.execute("""CREATE TABLE if not exists users(id integer Primary Key, lastname text);""")
con.commit()
#"""CREATE TABLE if not exists users(id integer Primary Key, firstname text, lastname text, phone number, description text);"""

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_name = message.from_user.first_name
    await message.reply(f'Привет, {user_name}!Выберите действие: \n /add_data - Добавить сотрудника \n /2 - Удалить сотрудника \n /3 - Печать данных сотрудника \n')

@dp.message_handler(commands=['add_data'])
async def add_data(message: types.Message):
    await message.reply("Введите фамилию: ")
    user = message.from_user.text
    cur = con.cursor()
    cur.execute(f"INSERT INTO users(lastname) VALUES('{user}')")
    con.commit()
#"""INSERT INTO users(firstname, lastname, phone, description) VALUES (?, ?, ?, ?)""",  user

@dp.message_handler(commands=['stop'])

async def stop_handler(message: types.Message):

    await message.reply("Всего доброго!")

executor.start_polling(dp)
