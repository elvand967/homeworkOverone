# Домашнее задание Задача №10/1
# Даны 2 списка:
# a = [4,6,'pу','tell',78]
# b = [44,'hello’,56,'exept’,[‘world’,5.7],3,6]
# Тебе нужно выполнить следующие операции:
# 1. Сложить два списка
# 2. Добавить элемент 6 на 3 позицию.
# 3. Посчитать сколько раз встречается число 6
# 4. Посчитать количество элементов списка
# 5. Вывести 1 элемент вложенного списка
a = [4,6,'pу','tell',78]
b = [44,'hello',56,'exept',['world',5.7],3,6]
print(f'исходные списки: \n{a}\n{b}\n')
c = a +b
print(f'1. Новый список, сформированный путем сложения исходных списков: \n{c}\n')
c.insert(2, 6)
print(f'2. Добавлен элемент 6 на 3 позицию: \n{c}\n')
print(f'3. Число 6 в списке встречается: {c.count(6)} раз\n')
print(f'4. В списке {len(c)} елементов\n')
for i in c:
    # print(f'{i} тип элемента {type(i)}')
    if str(type(i)) == "class 'list'":
        print(f'5. 1-ый элемент вложенного списка: "{i[0]}"')
# print(f'5. 1-ый элемент вложенного списка: "{c[10][0]}"')