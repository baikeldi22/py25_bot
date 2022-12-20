import telebot
import random

from env import token 

bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('да')
button2 = telebot.types.KeyboardButton('нет')
keyboard.add(button1,button2)


@bot.message_handler(commands=['start', 'hi'])
def start_function(message):
   # print(message.chat.id)
    msg = bot.send_message(message.chat.id,f'привет {message.chat.first_name}начнем игру?',reply_markup=keyboard)
    bot.register_next_step_handler(msg,answer_check)
    # bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAJKdWOhPfUTZvDWFWXglCYeC7y3NS4QAAI7AwAC8-O-C8DVacJZfGSGLAQ')
#     bot.send_photo(message.chat.id, 'https://i.gifer.com/AYUm.mp4')
# @bot.message_handler(commands=['start', 'hi'])
# def echo_all(message):
#     bot.send_message(message.chat.id,message.text)

def answer_check(msg):
    if msg.text == 'да':
        bot.send_message(msg.chat.id, 'у тя есть 3 попытки угадать число от 1 до 10')
        random_number = random.randint(1,10)
        p = 3
        start_game(msg,random_number,p)
    else:
        bot.send_message(msg.chat.id, 'ну и ладно!')

def start_game(msg,random_number, p):
    msg = bot.send_message(msg.chat.id, 'введи число от 1 до 10;')
    bot.register_next_step_handler(msg, check_func,
    p-1, random_number)

def check_func(msg, random_number, p):
    if msg.text == str(random_number):
        bot.send_message(msg.chat.id, 'вы победили')

    elif p == 0:
        bot.send_message(msg.chat.id, f'вы проиграли число было - {random_number}')

    else:
        bot.send_message(msg.chat.id, f'попруй еще раз  у тя остался {p} попыток')
        start_game(msg, random_number, p)


bot.polling()



#  git init    git add .   git commit -m '    '      git remote add origin ssh/https    git push origin master  