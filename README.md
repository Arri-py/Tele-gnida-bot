# Tele-gnida-bot
Телеграмм бот торгующий концелярией 


1) Приветствие с пользователем 
    
2) Авторизация телефона 
    если он уже есть в нашей бд то не надо повторно регистрировать номер 
    смена номера телефона(он просто поменяемя в бд)
    если да то он сможет заказать товар
    если нет то предупредить что пользователь не сможет заказать товар (при попытке заказать что либо предложить регистрацию телефона)
    
3) Создать csv с товарами 
    Формат: article_number,title,price,discounts,quantity,url_tovar

4) Предложить товары по акции (создать кнопочку с товарами по акции)

5) Предложить все товары (создать кнопочку со всеми товарами)

6) Создать кнопку "заказать товар" 
    1. Какой товар(код товара, скок штук)
    2. Адрес доставки(город, улица, дома, кв)
    3. Оплата заказа 
        спасибо за покупку ваш заказ приедет через (читай 4 пункт)
    4. Заказ пользователя приедет через 7 дней
7) создать csv с историей заказов
    формат: имя пользователя, номер телефона, зака на сумму, город, улица, дома, кв

8) Пускай пользователь оценит качество работы бота по 10 бальной шкале
