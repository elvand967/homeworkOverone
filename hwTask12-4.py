# Домашнее задание Задача №12/4
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
import random
List = []
UniqueLetters = []
alphabet_en = ''
for i in range(97, 123):  # Значение ASCII для a-z находится в диапазоне 97 – 122.
    alphabet_en += chr(i)
for i in range(14):
    List.append(random.choice(alphabet_en))
print(List)
for i in List:
    if List.count(i) == 1:
        UniqueLetters.append(i)
print(UniqueLetters)