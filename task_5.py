"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet
import platform

addrlist = ['yandex.ru', 'youtube.com']
param = '-n' if platform.system().lower() == 'windows' else '-c'
for ip in addrlist:
    S_ping = subprocess.Popen(['ping', ip, param, '3'], stdout=subprocess.PIPE)
    for str in S_ping.stdout:
        output = chardet.detect(str)
        line = str.decode(output['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
