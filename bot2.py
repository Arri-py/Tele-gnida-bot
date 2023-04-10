import telebot
import pandas as pd

# подключение токена бота
apitoken = '6053060605:AAGvOKVTvn3jELZKKrtiNkNYSykIDSOm_G8' # запишем наш токен в переменную 
bot = telebot.TeleBot(apitoken)

# относителььный путь к бд с товарами
file_product_csv = 'Version1\CsvFile\products.csv'
# относительный путь к бд с историей
file_history_csv = 'Version1\CsvFile\history.csv'

products = pd.read_csv(file_product_csv)    # товары
history = pd.read_csv(file_history_csv)     # история


@bot.message_handler(commands=['start'])    # отслеживает комманду start
def start(message):
    
    pass