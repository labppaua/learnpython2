"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

addrlist = ["yandex.ru", "youtube.com"]
for ip in addrlist:
    ping = subprocess.Popen('ping ' + ip, stdout=subprocess.PIPE)
    for str in ping.stdout:
        output = chardet.detect(str)
        line = str.decode(output['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
