'''  Домашка: Типы данных и Базовая арифметика  '''
# https://stepik.org/lesson/1309430/step/1?unit=1324546

# 📚 Полезные ссылки на статьи и разборы задач:
# Вся теория для ЕГЭ в одном месте https://t.me/informatika_kege_itpy/362?comment=1424

"""for i in range(10):
    print ("Привет",)"""
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F =(not(x <= w))or (y <= z) or (not(y))
                if F == 0:
                    print(x, y, z, w,int(F))
            """(x ∧ ¬y) ∨ (y ≡ z) ∨"""""

            '""¬(x → w) ∨ (y → z) ∨ ¬y""'
            ""'y ∧ (x ∨ z) ∨ ¬(y ∨ z) ∨ w"'

            "(y → ¬(x → z)) ∨ w"
            
            
            
            """""(x ∧ ¬y) ∨ (x ≡ z) ∨ w"""""


            """¬(x → z) ∨ (y ≡ w) ∨ y"""

"""" ¬(x ∨ y) ∧ ¬w ∨ ¬(z ∨ w) ∧ y"""
'''F = (not (x or y)) and (not w) or (not (z or w)) and y'''