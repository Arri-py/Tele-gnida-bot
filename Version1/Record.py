import pandas as pd

# создаем базу данных с товарами

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

## и так мы созади 10 товаров 
## теперь их нужно закинуть в файлик

products_df = pd.DataFrame(products)

## указываем относительный путь (у нас все csv будут в отдельной папочке😐)
products_df.to_csv('Version1\CsvFile\products.csv', index=False)
## чекаем результат
prod = pd.read_csv('Version1\CsvFile\products.csv',sep=',')
print(prod)

## тут уже история покупок
history = pd.DataFrame([{'Id': 0,
                      'User_id': 'test', 
                      'User_first_name': 'test', 
                      'Phone': 0, 
                      'Order amount': 0,
                      'Address': 'test',}])

## указываем относительный путь (у нас все csv будут в отдельной папочке😐)
## чтобы меньше писать кода мы укажем 'index=True' оно тип само будет индексироваться
history.to_csv('Version1\CsvFile\history.csv', index=True)

## чекаем результат
his = pd.read_csv('Version1\CsvFile\history.csv', sep=',')
print(his)


