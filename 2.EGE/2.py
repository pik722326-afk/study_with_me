# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 2 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1461

# region Место для вашего конспекта ⬇️
print ("x y z w") #Выводим названия перименных
for x in range(2): #Проверяем каждые переменные на соотвецтвие
    for y in range (2):
        for z in range (2):
            for  w in range (2):
                F =(x<= y) or (not(w <= z)) #Преобразуем формулу
                if F == 1: #Выводим значение F которые нам нужны
                    print (x , y , z , w) #Выводим перименные

#Номер 1 (x∨¬y)∧¬(y≡z)∧¬w
#(x or (not y)) and (not(y == z)) and (not w)

#Номер 2 (х→y)∨¬(w→z)
#(x<= y) or (not(w <= z))

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not (x <= w)) or (y <= z) or (not (y))
                if F == 0:
                    print(x, y, z, w, int(F))
            """(x ∧ ¬y) ∨ (y ≡ z) ∨"""""

            '""¬(x → w) ∨ (y → z) ∨ ¬y""'
            ""'y ∧ (x ∨ z) ∨ ¬(y ∨ z) ∨ w"'

            "(y → ¬(x → z)) ∨ w"

            """""(x ∧ ¬y) ∨ (x ≡ z) ∨ w"""""

            """¬(x → z) ∨ (y ≡ w) ∨ y"""

"""" ¬(x ∨ y) ∧ ¬w ∨ ¬(z ∨ w) ∧ y"""
'''F = (not (x or y)) and (not w) or (not (z or w)) and y'''
'''
Запустите бота: https://t.me/ilandroxxy_bot и нажмите кнопку: "📚 Получить конспект"
'''
# endregion Место для вашего конспекта ⬆️

# Домашка 2 номер: https://stepik.org/lesson/1038536/step/1?unit=1062771

# Практика 2 номер: https://stepik.org/lesson/1152671/step/1?unit=1164793
