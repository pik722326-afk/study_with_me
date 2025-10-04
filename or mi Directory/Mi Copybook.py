#Номер 13
'''
# Номер 13 https://education.yandex.ru/ege/task/b6ff76ad-5608-4e7d-833d-dced5a6e2479
from ipaddress import *
for mask in range(1, 32+1):
    net = ip_network(f"111.81.27.208/{mask}", 0)
    print (net, net.netmask)
# Ответ-192,  111.81.27.192
'''
#13 задание Школа
"""
'''from ipaddress import *
cnt = 0
net = ip_network('192.168.32.176/255.255.255.240', 0)
for ip in net:
    if f'{ip:b}'.count('1') % 2 != 0:
        cnt += 1
print(cnt)'''#Answer: 8

'''from ipaddress import *
R = []
net = ip_network('191.128.66.83/255.192.0.0', 0)
print(net[-2])'''#Answer: 191.191.255.254

'''from ipaddress import *
cnt = 0
net = ip_network('252.67.33.87/255.248.0.0', 0)
for ip in net:
    if f'{ip:b}'[16:].count('1') / f'{ip:b}'[:16].count('1') > 2:
        cnt += 1
print(cnt)'''#Answer: 17
'''from ipaddress import *
net = ip_network('45.172.106.203/255.255.252.0', 0)
print(net[-2])'''#Answer: 45.172.107.254
'''from ipaddress import *
cnt = 0
net = ip_network('172.16.192.0/255.255.192.0', 0)
for ip in net:
    if f'{ip:b}'.count('1') % 5 != 0:
        cnt += 1
print(cnt)'''#Answer: 13003
'''from ipaddress import *
cnt = 0
net = ip_network('192.168.160.0/255.255.224.0', 0)
for ip in net:
    if f'{ip:b}'.count('1')==19:
        cnt+=1
print(cnt)'''#Answer: 13
'''from ipaddress import *
cnt = 0
net = ip_network('123.222.0.192/255.255.255.224', 0)
for ip in net:
    if f'{ip:b}'.count('0') == f'{ip:b}'.count('1'):
        cnt += 1
print(cnt)'''#Answer: 10
'''from ipaddress import *
cnt = 0
net = ip_network('123.222.111.192/255.255.255.192', 0)
for ip in net:
    if f'{ip:b}'[24:].count('1') % 3 != 0:
        cnt += 1
print(cnt)'''#Answer: 43
"""
#Домашка на 23.09.2025
# Задание номер 5 https://stepik.org/lesson/1038432/step/1?unit=1060804

# Задание №6 https://stepik.org/lesson/1038843/step/2?unit=1062794
# Направо 120 Повтори 8 [Вперёд 4 Направо 60]
"""import turtle as t
t.screensize(500, 500)
t.tracer(0)
t.left(90)
s = 20
t.right(120)
for i in range(8):
    t.forward(4 * s)
    t.right(60)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * s, y * s)
        t.dot(3, 'red')
t.update()
t.done()"""

# Задание №6 https://stepik.org/lesson/1038843/step/3?unit=1062794

# Повтори 2 [Вперёд 10 Направо 90 Вперёд 18 Направо 90]
#   Поднять хвост
#   Назад 6 Направо 90 Вперёд 9 Налево 90
#   Опустить хвост
#   Повтори 2 [Вперёд 17 Направо 90 Вперёд 5 Направо 90]
import turtle as t
t.screensize(1500, 1500)
t.left(90)
t.tracer(0)
s = 30
for i in range(2):
    t.color('red')
    t.forward(10 * s)
    t.right(90)
    t.forward(18 * s)
    t.right(90)
t.up()
t.backward(6 * s)
t.right(90)
t.fd (9 * s)
t.right(90)
t.down()
for i in range(2):
    t.color('blask')
    t.forward(17 * s)
    t.right(90)
    t.fd (5 * s)
    t.right(90)
t.up ()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * s, y * s)
        t.dot(2,'purple')
t.update()
t.done()

"""def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

M = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        z = ''
        for x in s:
            z += x * 2
    else:
        s = s.replace('0', '*')
        s = s.replace('1', '+')
        s = s.replace('2', '0')
        s = s.replace('*', '1')
        s = s.replace('+', '2')
        z = ''
        for x in s:
            z += x * 2
    r = int(z, 3)
    print(r)
    if r > 120:
        M.append(n)
print(min(M))"""

# Задание №6 https://stepik.org/lesson/1038843/step/3?unit=1062794

