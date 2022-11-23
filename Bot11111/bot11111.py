
import telebot

bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text', 'document', 'audio']) #получает
def get_text_messages(message): #обрабатывает
    if message.text == "Паника":
        bot.send_message(message.from_user.id, "Заразна!")
    else:
        bot.send_message(message.from_user.id, "Напиши Паника")

bot.polling(none_stop=True, interval=0)
