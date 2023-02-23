# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 1 - герб, 0 - решка
# Ввод:
# 4 - число монет
# 0  1  1  1
# Вывод:
# 1

from random import randint

n = int(input())
print()

orel = 0
resh = 0
for i in range(n):
    or_resh = randint(0, 1)
    print(or_resh)
    if or_resh == 0:
        orel += 1
    else:
        resh += 1
if orel < resh:
    print (f'Меньшее количество у монеты с орлом: {orel}')
else:
    print(f'Меньшее количество у монеты с решкой: {resh}')

