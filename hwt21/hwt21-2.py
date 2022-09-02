# Домашнее задание Задача №21/2
# Даны два списка чисел.
# Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
import random
# функция генерации рондонных списков рондонных чисел
def myRanList(n1=1,n2=99,l1=5,l2=20):
    MyRanList = [random.randint(n1,n2) for a in range(random.randint(l1,l2))]
    return MyRanList

list_a = myRanList(1,15,5,10)
list_b = myRanList(1,15,5,10)
print('Даны два списка чисел:')
print(list_a)
print(list_b)
set_c = set(list_a + list_b)
print(f'Одновременно в данных списках содержиться {len(set_c)} чисел:\n{set_c}')

