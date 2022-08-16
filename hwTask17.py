# Домашнее задание Задача №17
# Проверить, есть ли в последовательности чисел списка дубликаты
import random
mylist = []
for i in range(12):
    mylist.append(random.randint(0,21))
mylist.sort()  # сортируем в поряде возрастания
print(f'В иследуемом списке {mylist}')
if len(mylist) == len(set(mylist)):
    print('нет дубликатов')
else: print(f'{len(mylist) - len(set(mylist))} дублирующихся элементов')