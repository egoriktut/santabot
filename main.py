import telebot
from telebot import types


TOKEN = '5796877316:AAEh6v0q73D62kufwmTqtFSPWLNIWEmkQrQ'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот тайного санты!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Составим список для тайного санты!')
    item2 = types.KeyboardButton('Послушаем музыку!')
    item3 = types.KeyboardButton('Как дела!?')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Что будем делать?', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text.lower() == 'как дела!?':
        bot.send_message(message.chat.id, 'нормик')
    elif message.text.lower() == 'послушаем музыку!':
        bot.send_message(message.chat.id, 'https://music.yandex.ru/home')
    elif message.text.lower() == 'составим список для тайного санты!':
        bot.send_message(message.chat.id, 'ok')
    else:
        bot.send_message(message.chat.id, 'Будь внимательней, выбери что-то из списка!')


bot.polling(none_stop=True)
