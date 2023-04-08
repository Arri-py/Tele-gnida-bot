import telebot
import pandas as pd
import numpy as np
from telebot import types


# подключение токена бота
apitoken = '6053060605:AAGvOKVTvn3jELZKKrtiNkNYSykIDSOm_G8' # запишем наш токен в переменную 
bot = telebot.TeleBot(apitoken)


# Создаем базу данных с товарами




# переменные
# если че то это относительный путь*****
products = pd.read_csv("Version1\CsvFile\products.csv")
print(products)



@bot.message_handler(commands=['start']) # отслеживает комманду start
def start(message):
    # тут комманды при вызове комманды start
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')
    bot.send_message(message.chat.id, 'Я торговый telegram-бот')
    bot.send_message(message.chat.id, 'Вам необходимо зарегистрироваться для оформления заказа иначе но будет невозможен (/reg)')



@bot.message_handler(commands=['reg']) # reg тип регистрация
def start(message):
    bot.send_message(message.chat.id, 'Приступим к регистрации')
    bot.send_message(message.chat.id, 'Введите номер телефона')
    bot.register_next_step_handler(message, regmobile) 
    # bot.send_message(message.chat.id, f'Ваш номер телефона {mobile}')

# функция регистрации номера телефона
def regmobile(message):
    # global mobile она (тип глобальная)
    mobile = message.text
    is_num = mobile.isnumeric()
    if is_num == True:
        # int(mobile)
        if len(mobile) == 11:
            # bot.send_message(message.chat.id, f'Ваш номер телефона {mobile}')
            bot.send_message(message.chat.id, 'Поздравляю с успешной регистрацией)')
            bot.send_message(message.chat.id, 'Ознакомьтесь с товарами по скидке (/discounts)')

        else:
            bot.send_message(message.chat.id, 'Вы ввели не верный номер телефона')
            bot.send_message(message.chat.id, 'Повторите попытку')
            bot.register_next_step_handler(message, regmobile)

    else:
        bot.send_message(message.chat.id, 'Вы ввели не верный номер телефона')
        bot.send_message(message.chat.id, 'Повторите попытку')
        bot.register_next_step_handler(message, regmobile) 



# команда spam
@bot.message_handler(commands=['spam'])
def spam(message):
    bot.send_message(message.chat.id, 'Введите фразу и меня ничего не остановит')
    bot.register_next_step_handler(message, spammm) 

def spammm(message):
    mobile = message.text
    i = 0
    j = 100
    while i <= j:
        bot.send_message(message.chat.id, mobile)
        i += 1
    


# команда help
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Она тебе не нужна тут и так все понятно)')



# команда discounts
@bot.message_handler(commands=['discounts'])
def discounts(message):

    bot.send_message(message.chat.id, 'Товары по скидке')
    
    for i in products:
        discounts = int(products[i]['discounts'])

        if discounts > 0:
            title = products[i]['title']
            discounts_price = (int(products[i]['price'])) -((discounts * int(products[i]['price'])) / 100)

            bot.send_message(message.chat.id, f'{title} по {discounts_price}руб')



        # for j in products:
        # bot.send_message(message.chat.id, products[i]['title'] + ' - ' + products[i]['price'] + 'руб')

    # for i in products:
    #     for j  in i:
    #         bot.send_message(message.chat.id, products[i].keys() ' - ' products[j].keys())

    

@bot.message_handler(content_types=['text'])
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, ':)')

    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

    else:
        bot.reply_to(message, 'Я тебя не понимаю')



# для постоянной работы тоба
bot.polling(non_stop=True, interval=0)



