"""Утилиты"""

import json
from common.variables import MAX_PACKAGE_LENGTH, ENCODING

def get_message(client):
    '''
    Утилита приёма и декодирования сообщения
    принимает байты выдаёт словарь, если приняточто-то другое отдаёт ошибку значения
    :param client:
    :return:
    '''

    encoded_response = client.recv(MAX_PACKAGE_LENGTH) # Получаем из сокета данные в байтах
    if isinstance(encoded_response, bytes): # Проверяем тип данных на байты
        json_response = encoded_response.decode(ENCODING) # Полученные байты декодируем в строку
        response = json.loads(json_response) # Переводим строку в словарь
        if isinstance(response, dict): # Проверяем тип данных словарь или нет
            return response
        raise ValueError # Если не словарь выдаем ошибку
    raise ValueError # Если тип данных не словарь выдаем ошибку


def send_message(sock, message):
    '''
    Утилита кодирования и отправки сообщения
    принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    '''

    js_message = json.dumps(message) # Преобразовываем данные в строку формата JSON
    encoded_message = js_message.encode(ENCODING) # Строку преобразовываем в байты
    sock.send(encoded_message) # Данные преобразованные в байты передаем в сокет
