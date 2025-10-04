# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 5 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1465

# region Место для вашего конспекта ⬇️
'''
Запустите бота: https://t.me/ilandroxxy_bot и нажмите кнопку: "📚 Получить конспект"
'''
from lib2to3.pytree import convert

# endregion Место для вашего конспекта ⬆️

# Переводы в различные системы исчисления
"""
# Универсальная функция перевода 
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 8  # 1000

# Перевод в двоичную запись
print(bin(n)[2:])  # '1000'
print(f'{n:b}')  # '1000'
print(int('1000', 2))  #


# Перевод в восьмеричную запись
print(oct(n)[2:])  # '10'
print(f'{n:o}')  # '10'
print(int('10', 8))  # 8


# Перевод в шестнадцатеричную запись
print(hex(n)[2:])  # '8'
print(f'{n:x}')  # '8'
print(int('8', 16))  # 8
# ValueError: int() base must be >= 2 and <= 36, or 0
"""
# Примеры переводов
"""
n = 10**9
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]
print(convert(n, 2))  # 111011100110101100101000000000
print(int('111011100110101100101000000000', 2))  # 10**9

print(convert(n, 8))  # 7346545000
print(int('7346545000', 8))  # 10**9

print(convert(n, 16))  # 3B9ACA00
print(int('3B9ACA00', 16))  # 10**9

print(convert(n, 3))  # 2120200200021010001
print(int('2120200200021010001', 3))  # 10**9
"""

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

# Домашка 5 номер: https://stepik.org/lesson/1038432/step/1?unit=1060804

# Практика 5 номер: https://stepik.org/lesson/1228668/step/1?unit=1242201
