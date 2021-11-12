"""Программа-клиент"""

import sys
import json
import socket
import time
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message


def create_presence(account_name='Guest'):
    '''
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    '''
    # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    '''Загружаем параметы коммандной строки'''
    # client.py 192.168.1.2 8079
    try:
        server_address = sys.argv[1] # Применяем значение аргументов если указаны для адреса хоста
        server_port = int(sys.argv[2]) # Применяем значение аргументов если указаны для порта
        if server_port < 1024 or server_port > 65535:
            raise ValueError # Выдаем ошибку если порт вне допустимого диапазона
    except IndexError: # Берем дефолтные значнеия из констант если аргументы не указаны
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создаем сокет как сетевой-потоковый
    transport.connect((server_address, server_port)) # Привязываем сокет к адресу и порту
    message_to_server = create_presence() # Вызываем функцию построения словаря
    send_message(transport, message_to_server) # Шлем сообщенеи серверной части
    try:
        answer = process_ans(get_message(transport)) # Получаем ответное сообщение от сервера через функцию парсинга
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
