import telebot
import pandas as pd

# подключение токена бота
apitoken = '6053060605:AAGvOKVTvn3jELZKKrtiNkNYSykIDSOm_G8' # запишем наш токен в переменную 
bot = telebot.TeleBot(apitoken)

# Создаем базу данных с товарами b историей в файле Record.py\

# получаем наши csv
# если че то это относительный путь*****
file_product_csv = 'Version1\CsvFile\products.csv'
products = pd.read_csv(file_product_csv)
# print(products) # затестим 
file_history_csv = 'Version1\CsvFile\history.csv'
# print(history)




products = {
    '0tovar':{
        'article_number': '0tovar',
        'title': 'Шариковая ручка "PARKER"',
        'quantity': 100,
        'price': 75480,
        'discounts': 20,
        'url_tovar': 'https://www.parkerrussia.ru/pens/duofold/PR20B-MLT53/'},

    '1tovar':{
        'article_number': '1tovar',
        'title': 'Перьевая ручка "PARKER"',
        'quantity': 100,
        'price': '200000',
        'discounts': 0,
        'url_tovar': 'https://pen-parker.ru/fountains/parker-duofold-2123549/'},
    
    '2tovar':{
        'article_number': '2tovar',
        'title': 'Ручка школьника',
        'quantity': 100,
        'price': '70',
        'discounts': 0,
        'url_tovar': 'https://www.ozon.ru/product/ruchka-lego-918586094/?asb2=ZiB0lHfB6UzaxePKIo6Jo77phqNBi8Dbiuz5Q-w8rCcRCTpZUmss_gDvoh0BuMZv&avtc=1&avte=2&avts=1680357851&keywords=ручки+шариковые&sh=iNe1bzckrQ'},

    '3tovar':{
        'article_number': '3tovar',
        'title': 'Карандаш механический "Bruno Visconti"',
        'quantity': 100,
        'price': '52',
        'discounts': 0,
        'url_tovar': 'https://leonardo.ru/ishop/group_67541861234/'},
        
    '4tovar':{
        'article_number': '4tovar',
        'title': 'Ластик для чернографитных карандашей "KOH-I-NOOR Hardtmuth"',
        'quantity': 100,
        'price': '117',
        'discounts': 10,
        'url_tovar': 'https://leonardo.ru/ishop/good_5040500583/'},

    '5tovar':{
        'article_number': '5tovar',
        'title': 'Карандаш корректирующий "Edding"',
        'quantity': 100,
        'price': '260',
        'discounts': 0,
        'url_tovar': 'https://leonardo.ru/ishop/good_31744315742/'},
    
    '6tovar':{
        'article_number': '6tovar',
        'title': 'Клей-карандаш "PRYM"',
        'quantity': 375,
        'price': '84',
        'discounts': 0,
        'url_tovar': 'https://leonardo.ru/ishop/good_209767311/'},
    
    '7tovar':{
        'article_number': '7tovar',
        'title': 'Маркер перманентный "Pentel"',
        'quantity': 840,
        'price': '38',
        'discounts': 0,
        'url_tovar': 'https://leonardo.ru/ishop/good_73277167744/'},

    '8tovar':{
        'article_number': '8tovar',
        'title': 'Маркер акриловый "PEBEO"',
        'quantity': 100,
        'price': '275',
        'discounts':15,
        'url_tovar': 'https://leonardo.ru/ishop/group_35861226922/'},

    '9tovar':{
        'article_number': '9tovar',
        'title': 'Декоративная ручка "Sakura"',
        'quantity': 100,
        'price': '203',
        'discounts': 0,
        'url_tovar': 'https://leonardo.ru/ishop/good_21808617932/'},

    '10tovar':{
        'article_number': '10tovar',
        'title': 'Маркер лаковый "Edding"',
        'quantity': 100,
        'price': '622',
        'discounts': 50,
        'url_tovar': 'https://leonardo.ru/ishop/good_74180313104/'}
}




@bot.message_handler(commands=['start']) # отслеживает комманду start
def start(message):
    # для начала нам понять заходил пользователь ранее или нет 
    # функция q это лучшее авторское решение 
    def q():
        history = pd.read_csv(file_history_csv)
        user_id = history['User_id'].tolist()
        
        if message.from_user.id in user_id:
            bot.send_message(message.chat.id, 'Привет')
            bot.send_message(message.chat.id, 'Как хорошо что ты вернулся')

        else:
            bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')
            bot.send_message(message.chat.id, 'Я торговый telegram-бот')
            bot.send_message(message.chat.id, 'Вам необходимо зарегистрироваться для оформления заказа иначе но будет невозможен (/reg)')
            new = pd.DataFrame([{'User_id': message.from_user.id,
                                'User_first_name': message.from_user.username,
                                'Phone': None,
                                'Order_amount': None,
                                'Address': None}])
            new.to_csv(file_history_csv, mode='a', index=False, header=False)
    q()


# message.from_user.id
# message.from_user.first_name
# message.from_user.last_name
# message.from_user.username

# комманда reg
# как она работает 
# для начала нам надо понять есть ли пользователь в нашей бд 
# если его нет то сразу же кидаем его на регистрацию номера телефона 
# если он есть то чекаем есть ли его номер телефона если нет то тоже кидаем на регистрацию телефона 
# если пользователь и номер его телефонаесть то 
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


"""оно не работет так как хотелось бы"""
# # комманда reg
# @bot.message_handler(commands=['reg']) # reg тип регистрация
# def start(message):
#     def q():
#         history = pd.read_csv(file_history_csv)
#         user_id = history['User_id'].tolist()

#         if message.from_user.id in user_id:
#             user_id_bot = str(message.from_user.id)
#             user_Phone = history[history.iloc[user_id_bot]],['Phone'].tolist()
#             if user_Phone.len() > 11: # сотрим есть ли 
#                 bot.send_message(message.chat.id, 'Приступим к повторной регистрации')    
#                 bot.register_next_step_handler(message, regmobile)

#             else:
#                 bot.send_message(message.chat.id, 'Ваш номер телефона не зарегистрирован')
#                 bot.send_message(message.chat.id, 'Приступим к регистрации вашего телефона')

#         else:   
#             bot.send_message(message.chat.id, 'Приступим к регистрации')
#             bot.send_message(message.chat.id, 'Введите номер телефона')
#             bot.register_next_step_handler(message, regmobile) 
#         # bot.send_message(message.chat.id, f'Ваш номер телефона {mobile}')
#     q()

# # функция повторной регистации пользователя 
# def povtor_regregmobile(message):
#     pass

# # функция регистрации номера телефона
# def regmobile(message): # вот это: regmobile для вот этого: register_next_step_handler
#     # опять применем лучшее авторкое решение
#     def q():
#         mobile = message.text
#         is_num = mobile.isnumeric()
#         if is_num == True:
#             # int(mobile)
#             if len(mobile) == 11:
#                 # bot.send_message(message.chat.id, f'Ваш номер телефона {mobile}')
    
#                 bot.send_message(message.chat.id, 'Поздравляю с успешной регистрацией)')
#                 bot.send_message(message.chat.id, 'Ознакомьтесь с товарами по скидке (/discounts)')
    
#             else:
#                 bot.send_message(message.chat.id, 'Вы ввели не верный номер телефона')
#                 bot.send_message(message.chat.id, 'Повторите попытку')
#                 bot.register_next_step_handler(message, regmobile)
    
#         else:
#             bot.send_message(message.chat.id, 'Вы ввели не верный номер телефона')
#             bot.send_message(message.chat.id, 'Повторите попытку')
#             bot.register_next_step_handler(message, regmobile) 
#     q()



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



