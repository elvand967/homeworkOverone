# Домашнее задание. Задача №37 (two tables)
# Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
# Если элемент списка слово, записать его в соответствующую таблицу,
# затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел,
# если нечётное, то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello»
import random
import sqlite3
from sqlite3 import Error
import calendar

# функция создания/подключения базы данных с обработчиком исключений (ошибок)
def create_connection(path): # path - путь с названием БД ("E:\\sm_app.db"),
                             # при указании только названия файла базы данных, он будет сформирован в текущем коталоге
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection('two_tables.db')
cursor = connection.cursor() # Создаем объект cursor

cursor.execute('''CREATE TABLE IF NOT EXISTS WORDS(
id_word INTEGER PRIMARY KEY AUTOINCREMENT, word TEXT) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS NUMBERS(
id_number INTEGER PRIMARY KEY AUTOINCREMENT, number INTEGER) ''')
connection.commit()

d = 1
my_list = []               # список для генератора тестовых кортежей
for i in calendar.day_name:
    my_list.append(d)
    my_list.append(i)
    d+=1
print(f'тестовый список: {my_list}')

for i in range(7):
    tn = random.choice(my_list)
    if type(tn) == str:
        cursor.execute('''INSERT INTO WORDS(word) VALUES (?)''',(tn,))
        cursor.execute('''INSERT INTO NUMBERS(number) VALUES (?)''', (len(tn),))
        connection.commit()

    if type(tn) == int:
        if tn%2:
            cursor.execute('''INSERT INTO WORDS(word) VALUES('нечётное')''')
            connection.commit()
        else:
            cursor.execute('''INSERT INTO NUMBERS(number) VALUES (?)''', (tn,))
            connection.commit()

# фукция принимает название таблицы и при необходимости №(int) иследуемого поля(колонки)
def select_tab(name_tab, col_number = None):
    if col_number is None:
        cursor.execute(f'''SELECT * FROM {name_tab}''') # запрос записей в таблице
        connection.commit()
        field = cursor.fetchall()
        print(f'таблица {name_tab}: {field}')
        return field # fetchall() – возвращает число записей в виде упорядоченного списка
    elif col_number is not None:
        cursor.execute(f'''SELECT * FROM {name_tab}''')  # запрос записей в таблице
        connection.commit()
        field = cursor.fetchone()
        return field[0] # – возвращает значение 1-ой записи принятого иследуемого поля(колонки)

select_tab('WORDS')
select_tab('NUMBERS')

cursor.execute('''SELECT COUNT(*) FROM NUMBERS''') # запрос количества записей в таблице
connection.commit()
amt = cursor.fetchone() # fetchone() – возвращает первую запись.
print(f'число записей в таблице чисел: {amt[0]}')

if amt[0] >= 5:
    print(f'число записей больше/равно 5 (id первой записи в WORDS: {select_tab("WORDS",0)})')
    cursor.execute(f'''DELETE FROM WORDS WHERE id_word = {select_tab('WORDS',0)}''')
    connection.commit()
    select_tab('WORDS')
else:
    print(f'число записей меньше 5 (id первой записи в WORDS: {select_tab("WORDS",0)})')
    cursor.execute(f'''UPDATE WORDS SET word = 'hello' WHERE id_word = {select_tab('WORDS',0)}''')
    connection.commit()
    select_tab('WORDS')

cursor.execute('''DELETE FROM WORDS''') # очистка таблицы
cursor.execute('''DELETE FROM NUMBERS''') # очистка таблицы
connection.commit()

# Connection to SQLite DB successful
# тестовый список: [1, 'Monday', 2, 'Tuesday', 3, 'Wednesday', 4, 'Thursday', 5, 'Friday', 6, 'Saturday', 7, 'Sunday']
# таблица WORDS: [(1, 'нечётное'), (2, 'нечётное'), (3, 'Friday'), (4, 'Friday'), (5, 'Monday'), (6, 'нечётное')]
# таблица NUMBERS: [(1, 6), (2, 6), (3, 6), (4, 6)]
# число записей в таблице чисел: 4
# число записей меньше 5 (id первой записи в WORDS: 1)
# таблица WORDS: [(1, 'hello'), (2, 'нечётное'), (3, 'Friday'), (4, 'Friday'), (5, 'Monday'), (6, 'нечётное')]

# Connection to SQLite DB successful
# тестовый список: [1, 'Monday', 2, 'Tuesday', 3, 'Wednesday', 4, 'Thursday', 5, 'Friday', 6, 'Saturday', 7, 'Sunday']
# таблица WORDS: [(7, 'Saturday'), (8, 'Thursday'), (9, 'нечётное'), (10, 'нечётное'), (11, 'Wednesday')]
# таблица NUMBERS: [(5, 8), (6, 8), (7, 4), (8, 6), (9, 9)]
# число записей в таблице чисел: 5
# число записей больше/равно 5 (id первой записи в WORDS: 7)
# таблица WORDS: [(8, 'Thursday'), (9, 'нечётное'), (10, 'нечётное'), (11, 'Wednesday')]