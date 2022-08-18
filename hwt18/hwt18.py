# Домашнее задание Задача №18
# Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел.
# Вывести в файл ‘output.txt’ их разность
import random
x = random.randint(1,100)
y = random.randint(1,100)

f = open('input.txt', 'w')
f.write(f'{x} {y}') # 1-ая часть задания
f.close()
with open('input.txt', 'r') as f_input, open('output.txt', 'w') as f_output:
   mylist = f_input.readline().split() # считаем ранее созданную строку файла,
   # с помощью .split() создадим список с числами по разделителю пробел, пока в формате str
   mylist = [int(i) for i in mylist] # преобразуем элементы списка в int()
   f_output.write(f'{mylist[0]-mylist[1]}') # 2-ая часть задания



