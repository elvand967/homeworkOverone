# Домашнее задание Задача №24
# Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
import random
def func(testlist, n = 10):
    if n >= 0:
        n -= 1
        return testlist[n] + func(testlist, n)
    else: return 0

mylist = []
for i in range(10):
    mylist.append(random.randint(1,100))
print(f'Сумма чисел списка: {mylist}')
print(f'ровна: {func(mylist)}')


# def fun1(a = 25):
#     global b
#     b = 10
#     return a*b
# print(fun1()) # !!! без предварительного вызова функции с глобальной переменной,
#               # далее по коду она (глоб.пер) не видна
#
# def fun2(c,e=b):
#     return c/e
#
# print(fun2(int(input(f'Введите любое целое число, для его деления {b}: '))))
