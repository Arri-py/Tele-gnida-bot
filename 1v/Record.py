# import pandas as pd

# import csv

# with open('products.csv', 'w') as file:
#     reader = csv.reader(file, delimiter=',')
#     for row in reader:
#         print(row)


# отслеживание текстовых сообщений
# @bot.message_handler(content_types=['text'])

# отслеживание commands
# def command(message):
#     if message.text == '/start':
#         bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')
#         bot.send_message(message.chat.id, 'Привет желаете зарегистрироваться?')
#         registrat(message)



# def registrat(message):
#     if message.text == 'да' or message.text == 'Да':
#         bot.send_message(message.chat.id, 'werwet')



# mess_text = mess_text(message)



# def registr(message):
#     bot.send_message(message.chat.id, 'Желаете зарегистрироваться?')
#     if mess_text == 'да':
#         bot.send_message(message.chat.id, 'да?')
        


# def command(message):
#     if message.text == '/start':
#         bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}') 
         


# обычные текстовые сообщения
# def text(message):
#     if message.text == 'Привет' or message.text == 'привет':
#         bot.send_message(message.chat.id, ':)')

    
    # bot.send_message(message.chat.id, 'Желаете зарегистрироваться?')
    # if message.text == 'Да' or message.text == 'да':
    #     bot.send_message(message.chat.id, 'хорошо')

    

# длы постоянной работы бота 



# отслеживание комманд это те самые через '/'
# @bot.message_handler(commands=['start', 'message', 'my_id'])
# def start(message):

#     if message.text == '/start':
#         bot.send_message(message.chat.id, 'Привет')

#     elif message.text == '/message':
#         bot.send_message(message.chat.id, 'Держи всю информацию')
#         bot.send_message(message.chat.id, message)
    
#     elif message.text == '/my_id':
#         bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}')

        

# для отслеживания любых текстовых сообщений
# @bot.message_handler(content_types=['text'])
# def textmessage(message):
    # ...
    
    # когда хотим взаимодействовать с ботом нам надо к нему обратиться
    # в методе send мы может отправть что у годно (чекай автотаб)  
    # пертвые 2 параметра обязательные 1: чат; 2: сам текст сообщения; 3: режим отправки сообщений  parse_mode='text' ('text' or 'html')
    # mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    # bot.send_message(message.chat.id, mess)



# это чтобы он на постоянке работал
# bot.polling(none_stop=True, interval=0)



# декоратор для получения текствовых сообщений
# @bot.message_handler(content_types=['text', 'document', 'audio'])



# def get_text_messages(message):
#     if message.text == "Привет" or message.text == "привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")

#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")

#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")



# bot.polling(none_stop=True, interval=0)



# bot=telebot.TeleBot(apitoken)
# @bot.message_handler(commands=['start'])

# def start_message(message):
#     bot.send_message(message.chat.id,'Привет')



# @bot.message_handler(commands=['button'])
# def button_message(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1=types.KeyboardButton("Кнопка")
#     markup.add(item1)
#     bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)



# @bot.message_handler(content_types='text')
# def message_reply(message):
#     if message.text=="Кнопка":
#         bot.send_message(message.chat.id,"https://habr.com/ru/users/lubaznatel/")
# bot.infinity_polling()