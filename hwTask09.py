# Домашнее задание. Задача №9
# Создай список, замени первый его элемент на [1, 2, 3],
# затем в конец списка добавь сумму элементов вложенного списка.
from random import randint
# создаем список из 7 элементов, с случайными числами от 0 до 100 при помощи генератора списков
mylist = [randint(0,100) for i in range(7)]
print(mylist)
mylist[0] = [1, 2, 3]
print(mylist)
x = sum(mylist[0])
print(x)