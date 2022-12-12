import telebot
from telebot import types
import random


TOKEN = '5796877316:AAEh6v0q73D62kufwmTqtFSPWLNIWEmkQrQ'
bot = telebot.TeleBot(TOKEN)
check = False


def my_mood():
    return random.choice(["замечательно", "неплохо", "прекрасно", "отменно", "изумительно",
"чудесно", "славно", "здорово", "замечательно", "чудно", "идеально", "превосходно",
"замечательно", "добротно", "неплохо", "славно", "ништяк", "тип-топ", "нормик"])


def functional(message):
    if message.text.lower() == 'у меня все! спасибо! :)':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Пиши если что!', reply_markup=markup)
    else:
        people = message.text.split()
        count_people = len(people)
        answer = list()
        random.shuffle(people)
        clone = list(people)
        if count_people <= 1:
            bot.send_message(message.chat.id, "Сам себе не подаришь!!!")
            bot.send_message(message.chat.id,
                             'Напиши список людей, учавствующих в жеребьевке, по одному человеку в каждую строчку или через пробел.')
            global check
            check = True
        else:
            for i in range(count_people):
                first_person = people[i]
                second_peron = clone[random.randint(0, count_people - 1)]
                while first_person == second_peron:
                    second_peron = clone[random.randint(0, count_people - 1)]
                answer.append(f'{first_person} дарит {second_peron}')
                count_people -= 1
                clone.remove(second_peron)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Составить еще один список!')
            item2 = types.KeyboardButton('У меня все! Спасибо! :)')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Список получился такой", reply_markup=markup)
            bot.send_message(message.chat.id, '\n'.join(answer))



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот тайного санты!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Составим список!')
    item2 = types.KeyboardButton('Послушаем музыку!')
    item3 = types.KeyboardButton('Как дела!?')
    item4 = types.KeyboardButton('У меня все! Спасибо! :)')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Что будем делать?', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    global check
    if check:
        check = False
        functional(message)
    elif message.text.lower() == 'как дела!?':
        bot.send_message(message.chat.id, my_mood())
    elif message.text.lower() == 'послушаем музыку!':
        bot.send_message(message.chat.id, 'Тогда тебе сюда)')
        bot.send_message(message.chat.id, 'https://music.yandex.ru/home')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Пиши если что!', reply_markup=markup)
    elif message.text.lower() == 'составим список!' or message.text.lower() == 'составить еще один список!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('У меня все! Спасибо! :)')
        markup.add(item1)
        bot.send_message(message.chat.id,
                         'Напиши список людей, учавствующих в жеребьевке, по одному человеку в каждую строчку или через пробел.',
                         reply_markup=markup)
        check = True
    elif message.text.lower() == 'у меня все! спасибо! :)':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Пиши если что!', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Будь внимательней, выбери что-то из списка!')


bot.polling(none_stop=True)
