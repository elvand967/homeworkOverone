# Домашнее задание Задача №24(1)
# Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
import random
def func(testlist, n = -99):
    if n == -99:
        n = len(testlist)
    if n > 0:
        return testlist[n-1] + func(testlist, n-1)
    else: return 0

mylist = []
for i in range(10):
    mylist.append(random.randint(1,100))
print(f'Сумма чисел списка: {mylist} = {func(mylist)}')