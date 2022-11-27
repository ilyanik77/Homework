import random
import view

from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

def start(update, context):
    update.message.reply_text(
        "Привет!Давай играть!",
        reply_markup=view.markup
    )

def play(update, context):
    update.message.reply_text("Введите количество конфет в игре", reply_markup = view.stop_markup)
    return 1

def play_get_candy(update, context):
    global candy
    candy = int(update.message.text)
    update.message.reply_text("Сколько конфет Вы возьмете?")
    return 2

def player_1(update, context):
    global candy
    try:
        candy -= int(update.message.text)
        update.message.reply_text(f"Конфет осталось {candy}")
        if candy > 28:
            temp = random.randint(1, 28)
            candy -= temp
            update.message.reply_text(f"Бот взял {temp} конфет.Конфет осталось {candy}")
            if candy >28:
                update.message.reply_text("Сколько конфет Вы возьмете?")
            else:
                update.message.reply_text("Вы победили!!!", reply_markup = view.markup)
                return ConversationHandler.END
            return 2
        else:
            update.message.reply_text("Бот победил!!!", reply_markup = view.markup)
            return ConversationHandler.END
    except ValueError:
        update.message.reply_text("Введите число: ")
        return 2

def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END

def info(update, context):
    update.message.reply_text("Правила игры")

def close(update, context):
    update.message.reply_text("Спасибо за игру!",
    reply_markup=ReplyKeyboardRemove())
