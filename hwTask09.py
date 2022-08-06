# Домашнее задание. Задача №9
# Создай список, замени первый его элемент на [1, 2, 3],
# затем в конец списка добавь сумму элементов вложенного списка.
from random import randint
# создаем список из 7 элементов, с случайными числами от 0 до 100 при помощи генератора списков
coment = ['Исходный список:',
          'в 1-ую позицию вложен новый список:',
          'в конец списка добавлена сумму элементов вложенного списка:' ]
for i in range(len(coment)):
    if not i:
        n =len(coment[i])
        continue
    if len(coment[i]) > n:
        n = len(coment[i])
mylist = [randint(0,100) for i in range(7)]
print(coment[0].ljust(n,' '),mylist)
mylist[0] = [1, 2, 3]
print(coment[1].ljust(n,' '),mylist)
mylist.append(sum(mylist[0]))
print(coment[2].ljust(n,' '),mylist)