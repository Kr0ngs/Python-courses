import random
import telebot

bot = telebot.TeleBot('6951731322:AAHIQrjqfDDyEIIzbEutofHYZjgqLoUpqZI')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id,
                         "Викулька какулька, я тебя люблю")

    else:
        bot.send_message(message.from_user.id, "Напиши привет")


bot.polling(none_stop=True, interval=0)
