# Домашнее задание Задача №12/3
# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
# (Пример HjkLM- 1 пара нижнего, 1 пара верхнего),
# а также сколько всего букв в слове, сколько гласных и согласных.
import random
alphabet_en=[]
for i in range(65,91):         #Значение ASCII A-Z лежит в диапазоне 65-90,
    alphabet_en.append(chr(i))
for i in range(97, 123):       # а для a-z это значение находится в диапазоне 97 – 122.
    alphabet_en.append(chr(i))
print(alphabet_en)
random.shuffle(alphabet_en)    # перемешаем список строчных и заглавных букв
print(alphabet_en)