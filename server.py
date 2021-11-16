"""Программа-сервер"""

import socket
import sys
import json
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message


def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    '''
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest': # Валидация сообщения
        return {RESPONSE: 200} # Возвращаем словарь если прошли валидацию
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    } # Выдаем ошибку если не прошли валидацию


def main():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p 8079 -a 192.168.1.2
    :return:
    '''

    try:
        if '-p' in sys.argv: # Для списка аргументов
            listen_port = int(sys.argv[sys.argv.index('-p') + 1]) # Если аргументы указаны - применяем их значения
        else:
            listen_port = DEFAULT_PORT # Если порт не указан берем порт по дефолту из констант
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError # Выдаем ошибку если порт вне допустимого диапазона
    except IndexError: # Выдаем ошибку если не указали номер порта
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1] # Получаем значение хоста из аргументов
        else:
            listen_address = '' # Используем значнеие хоста из констант если аргумент не указан

    except IndexError: # Выдвем ошибку если забыли указать значение аргумента
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создаем сокет как сетевой-потоковый
    transport.bind((listen_address, listen_port)) # Привязываем сокет к адресу и порту

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS) # Ожидание запроса

    while True:
        client, client_address = transport.accept() # Принимаем запрос на установку соедиения
        try:
            message_from_cient = get_message(client) # Берем сообщение словарь от клиента
            print(message_from_cient)
            # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
            response = process_client_message(message_from_cient) # Отправляем клиенту ответное сообщение
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError): # Выдаем ошибку
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
