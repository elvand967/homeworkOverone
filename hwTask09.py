# Домашнее задание. Задача №9
# Создай список, замени первый его элемент на [1, 2, 3],
# затем в конец списка добавь сумму элементов вложенного списка.
from random import randint
#from string import ljust
# создаем список из 7 элементов, с случайными числами от 0 до 100 при помощи генератора списков
coment = ['Исходный список:','в 1-ую позицию вложен новый список:','в конец списка добавлена сумму элементов вложенного списка:' ]
for i in range(len(coment)):
    if not i:
        n =len(coment[i])
        print(n)
        continue
    if len(coment[i]) > n:
        n = len(coment[i])
        print(n)
for i in range(len(coment)):
    s = coment[i]
    s.ljust(60,'*')
    print(s)
    coment[i] = s
    print(coment[i])

mylist = [randint(0,100) for i in range(7)]
print(f'{coment[0]}{mylist}')
mylist[0] = [1, 2, 3]
print(f'{coment[1]}{mylist}')
mylist.append(sum(mylist[0]))
print(f'{coment[2]}{mylist}')