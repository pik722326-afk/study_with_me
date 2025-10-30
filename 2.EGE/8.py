# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 8 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1471

# region Место для вашего конспекта ⬇️
'''
Запустите бота: https://t.me/ilandroxxy_bot и нажмите кнопку: "📚 Получить конспект"
'''
# endregion Место для вашего конспекта ⬆️


'''
s = 'abc'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            cnt += 1
            print(cnt, a, b, c)
'''


'''
from itertools import product

for p in product('abc', repeat=3):
    word = ''.join(p)
    print(p, word)
'''

'''
from itertools import permutations
for p in permutations('abc', r=3):
    word = ''.join(p)
    print(p, word)
'''


# № 23746 Демоверсия 2026 (Уровень: Базовый)
'''
# Вариант 1
s = sorted('СТРОКА')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1  # n = n + 1
                    if n % 2 == 0:
                        if a not in 'АСТ':
                            if word.count('О') == 2:
                                print(n)
'''
# Вариант 2
'''
RES = []
from itertools import product
n = 0
for p in product(sorted('СТРОКА'), repeat=5):
    word = ''.join(p)
    a, b, c, d, e = word
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АСТ':
            if word.count('О') == 2:
                RES.append(n)
print(max(RES))
'''


# № 18042 (Уровень: Базовый)
#Ваня составляет 5-буквенные слова,
#в которых могут быть использованы только буквы Л, Ю, С, Т, Р, А,
#причём буква Ю используется не более двух раз.
#Каждая из других допустимых букв может встречаться в слове любое количество
#раз или не встречаться совсем. Также слово не должно оканчиваться согласными буквами.
#Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
# Сколько существует таких слов, которые может написать Ваня?
'''
from itertools import product
cnt = 0
for p in product('ЛЮСТРА', repeat=5):
    word = ''.join(p)
    if word.count('Ю') <= 2:
        if word[-1] not in 'ЛСТР':
            cnt += 1
print(cnt)
'''


# № 17862 Демоверсия 2025 (Уровень: Базовый)
#Определите количество 12-ричных пятизначных чисел,
#в записи которых ровно одна цифра 7
#и не более трёх цифр с числовым значением, превышающим 8.
'''
from itertools import product
cnt = 0
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('7') == 1:
            # if num.count('9') + num.count('A') + num.count('B') <= 3:
            if len([x for x in num if x > '8']) <= 3:
                cnt += 1
print(cnt)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 13, 14]

# Домашка 8 номер: https://stepik.org/lesson/1038667/step/1?unit=1062772

# Практика 8 номер: https://stepik.org/lesson/1227099/step/1?unit=1240617
