# Домашнее задание Задача №24(1)
# Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
import random
def func(testlist, n = None):
    if n is None:
        n = len(testlist)
    if n > 0:
        return testlist[n-1] + func(testlist, n-1)
    else: return 0

mylist = []
x = random.randint(5,20)
for i in range(x):
    mylist.append(random.randint(1,100))
print(f'Сумма чисел списка (из {x} чисел): {mylist} = {func(mylist)}')