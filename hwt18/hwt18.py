# Домашнее задание Задача №18
# Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел.
# Вывести в файл ‘output.txt’ их разность
import random
x = random.randint(1,100)
y = random.randint(1,100)
# with open('input.txt', 'w') as f_input, open('output.txt', 'w') as f_output:
#    f_input.write(f'{x} {y}')
#    f_output.write(f'{x-y}')
f = open('input.txt', 'w')
f.write(f'{x} {y}')
f.close()
with open('input.txt', 'r') as f_input:
   mytxt = f_input.readline()

print(mytxt)


