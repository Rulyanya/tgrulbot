import telebot
from telebot import types
import time
from API import bot_api


bot = telebot.TeleBot(bot_api)

bot.send_message(548408024, 'Бот перезапущен(Ботам тоже нужно отдыхать🥺)')

bottom = ['1', '1.5', '2', '2.5', '3']

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    iter = 0
    for i in bottom:
        print(f'Итерация номер: {iter} это значение: {i}')
        iter += 1
        item = types.KeyboardButton(i)
        markup.add(item)
    bot.send_message(message.chat.id, f'Приветствую, этот бот даст вам возможность отслеживать перерывы. \nВведите, в часах, через какой промежуток времени желаете сделать перерыв ?', reply_markup = markup)

@bot.message_handler(content_types = 'text')
def text(message):
    try:        
        int(message.text)
        bot.send_message(message.chat.id, f'Я напомню тебе о перерыве через: {message.text} часа!')
        bot.send_chat_action(message.chat.id, action='typing')

        time.sleep((float(message.text) * 60)* 60)
        bot.send_message(message.chat.id, f'Время вышло! Сделай перерыв!')
    except ValueError:
        bot.send_message(message.chat.id, f'Введите число!')
        





bot.infinity_polling()