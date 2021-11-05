import platform

l = ['ping', 'ya.ru']
if platform.system()=='Linux':
     l.extend(['-c', '3'])
     print(l)