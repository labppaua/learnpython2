"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "принтер",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json


def get_data():
    data = list()
    data.append(['принтер', '10', '6700', 'Ivanov I.I.', '24.09.2017'])
    data.append(['scaner', '20', '10000', 'Petrov P.P.', '11.01.2018'])
    return data


def write_order_to_json(item, quantity, price, buyer, date):
    data = {}
    with open('orders_1.json', encoding='utf-8') as infile:
        data = json.load(infile)
    orders = data['orders']
    orders.append({"item": item, "quantity": quantity, "price": price, "buyer": buyer, "date": date})
    with open("orders_1.json", "w", encoding='utf-8') as orders_file:
        json.dump(data, orders_file, indent=4, ensure_ascii=False)


for i in get_data():
    if len(i) == 5:
        write_order_to_json(i[0], i[1], i[2], i[3], i[4])
