# Домашнее задание Задача №19
# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os

import os
os.mkdir('test') # создание новой папки (директории)
os.chdir('test') # переход в новую, созданную директорию
for i in range(1,4):  # создание новых файлов в дириктории 'test'
    f = open(f'test_{i}.txt', 'w')
    f.close()

# os.chdir('test') # переход в новую, созданную директорию
# for i in range(1,4):  # переименование файлов в дириктории 'test'
#     os.rename(f'test_{i}.txt',f'rename_{i}.txt')

# os.chdir('test') # переход в новую, созданную директорию
# for i in range(1,4):  # переименование файлов в дириктории 'test'
#     os.remove(f'rename_{i}.txt')
# os.chdir('..')   # выйдем из директории 'test'
# os.rmdir('test') # и удалим ее