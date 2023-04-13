import telebot
import pandas as pd


# подключение токена бота
apitoken = '6053060605:AAGvOKVTvn3jELZKKrtiNkNYSykIDSOm_G8'     #запишем наш токен в переменную 
bot = telebot.TeleBot(apitoken)


# относителььный путь к бд с товарами
file_product_csv = 'Version1\CsvFile\products.csv'
# относительный путь к бд с историей
file_history_csv = 'Version1\CsvFile\history.csv'


products = pd.read_csv(file_product_csv)    # товары
history = pd.read_csv(file_history_csv)     # историяz




@bot.message_handler(commands=['start'])    #отслеживает комманду start
def start(message):
    # для начала нам понять заходил пользователь ранее или нет 
    # функция q это лучшее авторское решение 

    def check():
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
            
    check() 



bot.polling(non_stop=True, interval=0)  # для постоянной работы бота