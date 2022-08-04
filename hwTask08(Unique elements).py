# Домашнее задание. Задача №8
# Введи список, отсортируй его и оставь только уникальные элементы
# Примечание: Уникальные элементы - это элементы, которые появляются только один раз в списке
import random

mylist = []
UniqueElements = []
for i in range(12):
    mylist.append(random.randint(2,11))
mylist.sort()  # сортируем в поряде возрастания
print(mylist)
for i in range(len(mylist)):
    if mylist.count(mylist[i]) == 1:
        UniqueElements.append(mylist[i])
print(UniqueElements)