# Домашнее задание. Задача №36
# 1.Сформулируйте SQL запрос для создания таблицы book. Структура таблицы book:
# Поле                    |  Тип, описание
# book_id                 |  INT PRIMARY KEY AUTO_INCREMENT
# title                   |  VARCHAR(50)
# author                  |  VARCHAR(30)
# price                   |  DECIMAL(8, 2)
# amount                  |  INT
# 2.Занесите новую строку в таблицуbook
# 3.Выбрать информацию о всех книгах из таблицы book.

import sqlite3
bs = sqlite3.connect('bookstore.db') # Создаём Базу данных "магазин книг"
cursor = bs.cursor() # Создаем объект cursor, который позволяет нам взаимодействовать с базой данных
# Создадим таблицу и ее структуру: bookshelf (книжная полка)
cursor.execute('''CREATE TABLE IF NOT EXISTS bookshelf(
book_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50),
author VARCHAR(30),
price DECIMAL(8, 2),
amount INT) ''')
bs.commit()

books = [
    ('"Война и мир"', 'Лев Толстой', 55.34, 6),
    ('"Евгений Онегин"', 'Александр Пушкин', 16.69, 4),
    ('"Сымон-музыка"', 'Якуб Колас', 28.86, 8),
    ('"Выбранае Янка Купала"', 'Янка Купала', 21.9, 5)]

# Заполнение таблицы данными списка кортежей "books"
cursor.executemany('''INSERT INTO bookshelf(title, author, price, amount)
VALUES(?, ?, ?, ?)''', (books))
bs.commit()
# Запрос данных таблицы "bookshelf"
cursor.execute('''SELECT * FROM bookshelf;''')
book_results = cursor.fetchmany(20) # вывод результатов, максимум 20 кортежей
for i in book_results:
    s = ''
    for n in range (len(i)):
        s +=' ' + str(i[n])
        if n == 3:
            s += ' руб.'
        elif n == 4:
            s += ' шт.'
    print(s)