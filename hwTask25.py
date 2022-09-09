# Домашнее задание Задача №25
# Напишите декоратор, который будет считать,
# сколько раз была вызвана декорируемая функция
import random

def fun_decore(fn):
    counter = 0
    n = random.randint(2, 5)
    for i in range(n):
        fn()
        counter +=1
    return counter

def fun():
    print('Привет!')

print(f'Функция "fun" ,была вызвона: {fun_decore(fun)} раз(а)')
