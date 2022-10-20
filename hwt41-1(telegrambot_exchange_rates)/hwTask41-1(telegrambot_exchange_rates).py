#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Домашнее задание. Задача №41-1 (Telegrambot erfByn_bot v1.0)
# Разработка телеграмм бота, который по запросу предоставляет курсы валют
# комерческих банков РБ в г Молодечно
# первоисточник основы: https://www.youtube.com/watch?v=4L57oY3J378
# бот находиться по адресу t.me/CurrencyRatesMoloBot
# 5526229345:AAHJfpzPVb1Gju11W1ZzM2_aCS5Nr3i7a_Q

import telebot  # импортируем библиотеки
from telebot import types
import os
import random
import requests
import sqlite3
from bs4 import BeautifulSoup
from transliterate import translit
import time
import datetime

token = '5526229345:AAHJfpzPVb1Gju11W1ZzM2_aCS5Nr3i7a_Q'
bot = telebot.TeleBot(token)  # подключаем токен бота


class MyDatabase:
    default_ru_city = 'Молодечно'
    default_url = 'https://myfin.by/currency/'  # источник данных
    # заголовки - описывают пользователя
    # (если их не передать то будет считаться что заходит бот и запрос не будет обработан)
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', }

    def __init__(self, ru_city=default_ru_city, url=default_url, headers=default_headers):
        self.ru_city = ru_city
        self.url = url + self.fun_ru_city()
        self.headers = headers
        self.connect = sqlite3.connect('dbBot/ExchangeRates.db',
                                       check_same_thread=False)  # Создаём/подключаем Базу данных
        self.cursor = self.connect.cursor()  # Создаем объект cur (курсор), который позволяет нам взаимодействовать с базой данных
        # проверим наличие нужных таблиц в БД
        if not self.fun_checking_if_table_exists('USERS'):
            self.fun_table_users()
        if not self.fun_checking_if_table_exists('BANK_CITY'):  # банки в населенном пункте
            self.fun_table_bank_city()
        if not self.fun_checking_if_table_exists('EXCHANGE_RATES'):  # курсы валют
            self.fun_table_exchange_rates()
        self.fun_get_courses()  # загрука/обновление курсов валют

    # функция возвращает новую строку, в которой каждый RU символ в строке заменяется на EN
    @staticmethod
    def fun_ru_city(citi=default_ru_city):
        if citi is None or citi == '':
            citi = input('Введите название населенного пункта')
        en_city = translit(citi, language_code='ru', reversed=True)
        return en_city.lower()

    # функция проверки наличия таблицы в базе данных
    def fun_checking_if_table_exists(self, name_tabl):
        # get the count of tables with the name (получить количество таблиц с именем)
        self.cursor.execute(f''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{name_tabl}' ''')
        return self.cursor.fetchone()[0]  # возвращаем количество 0 или 1,2,3 :)

    # функция создания таблицы пользователя
    def fun_table_users(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS USERS(
         idUser INTEGER PRIMARY KEY AUTOINCREMENT,
         telegramID INTEGER,
         first_name TEXT,
         last_name TEXT,
         username TEXT,
         city_user TEXT,
         type TEXT);
         ''')
        self.cursor.connection.commit()  # сохраним изменения

    # функция создания/заполнения таблицы банков города Молодечно
    def fun_table_bank_city(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS BANK_CITY(
                 idBankCiti INTEGER PRIMARY KEY AUTOINCREMENT,
                 elected INT,
                 city TEXT,
                 bank TEXT,
                 address  TEXT,
                 mode  TEXT);
                 ''')

        self.list_line = []
        with open('ReferenceBooks/bank_molodechno.txt',
                  'r') as self.f:  # справочный файл размещен в папке директории где находится исполняемый файл Python
            for self.line in self.f.readlines():
                self.line = self.line.split('\t')  # разделим нашу строку на строки по сиволу табуляции
                self.line = [s.strip() for s in self.line]  # удалим сивол переноса строки
                # стоит заметить, что .strip() также удаляет любой пробел в начале и в конце строки
                self.tuple_line = tuple(self.line)
                if self.tuple_line[0] == '':
                    continue  # пропустим кортеж с пустыми значениями (символ переноса строки, который ранее был удален .strip(), но пустой элемент кортежа остался
                self.list_line.append(self.tuple_line)
        # print(self.list_line)
        for self.i in range(len(self.list_line)):
            self.cursor.execute('''INSERT INTO BANK_CITY (elected, city, bank, address, mode) VALUES(?,?,?,?,?)''',
                                (self.list_line[self.i][0], self.list_line[self.i][1], self.list_line[self.i][2],
                                 self.list_line[self.i][3], self.list_line[self.i][4]))

        self.cursor.connection.commit()  # сохраним изменения
        self.list_line = None
        self.f.close()

    # функция создания таблицы курсов
    def fun_table_exchange_rates(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS EXCHANGE_RATES(
                 idExchangeRates INTEGER PRIMARY KEY AUTOINCREMENT,
                 date_time TEXT,
                 citi_bank TEXT,
                 bank_exchange TEXT,
                 USD_buys REAL,
                 USD_sells REAL,
                 EUR_buys REAL,
                 EUR_sells REAL,
                 RUB100_buys REAL,
                 RUB100_sells REAL,
                 EUR_USD_buys REAL,
                 EUR_USD_sells REAL);
                 ''')
        self.cursor.connection.commit()  # сохраним изменения

    # функция загрузки/обновления курсов
    def fun_get_courses(self):
        # названия банков временно загрузим из таблицы ''BANK_CITY' , в перспективе организации избранных банков - изменить
        self.cursor.execute('''SELECT bank FROM BANK_CITY GROUP BY bank;
                                    ''')
        self.list_selected_banks = []  # избранный список банков пользователем
        self.list_selected = self.cursor.fetchall()
        for self.s in self.list_selected:  # преобразуем список кортежей банков в список строк
            self.list_selected_banks.append(''.join(self.s))

        self.res = requests.get(self.url, self.headers).text  # отправим запрос на сайт
        self.soup = BeautifulSoup(self.res, 'lxml')  # получим всю страницу

        for self.tables in self.soup.select("table tr"):  # выберем все значения из ячеек таблиц
            self.bank_rate = [self.item.get_text(strip=True) for self.item in self.tables.select("td")]
            if self.bank_rate == []:
                continue
            if self.bank_rate[
                0] in self.list_selected_banks:  # нас интересуют все строки таблиц в первой ячейке которых указан один из наших выбранных банков
                self.cursor.execute(
                    f'''SELECT * FROM EXCHANGE_RATES  WHERE citi_bank = '{self.ru_city}' AND bank_exchange = '{self.bank_rate[0]}' ;''')

                if self.cursor.fetchall() == []:
                    self.cursor.execute('''INSERT INTO EXCHANGE_RATES (date_time, citi_bank, bank_exchange, USD_buys, USD_sells,
                                   EUR_buys, EUR_sells, RUB100_buys, RUB100_sells, EUR_USD_buys, EUR_USD_sells) VALUES(datetime('now', 'localtime'),?,?,?,?,?,?,?,?,?,?)''',
                                        (self.ru_city, self.bank_rate[0], self.bank_rate[1], self.bank_rate[2],
                                         self.bank_rate[3],
                                         self.bank_rate[4], self.bank_rate[5], self.bank_rate[6], self.bank_rate[7],
                                         self.bank_rate[
                                             8]))  # time.strftime("%d.%m.%Y  %H : %M", time.localtime(time.time()))
                else:
                    self.cursor.execute(
                        f'''UPDATE EXCHANGE_RATES SET date_time = datetime('now','localtime'), citi_bank = '{self.ru_city}', 
                    bank_exchange = '{self.bank_rate[0]}', USD_buys = '{self.bank_rate[1]}', USD_sells = '{self.bank_rate[2]}',
                    EUR_buys = '{self.bank_rate[3]}', EUR_sells = '{self.bank_rate[4]}', RUB100_buys = '{self.bank_rate[5]}', 
                    RUB100_sells = '{self.bank_rate[6]}', EUR_USD_buys = '{self.bank_rate[7]}', EUR_USD_sells = '{self.bank_rate[8]}' 
                    WHERE citi_bank = '{self.ru_city}' AND bank_exchange = '{self.bank_rate[0]}' ;    ''')

        self.cursor.connection.commit()  # сохраним изменения


class InteractionWithTelegrambot(MyDatabase):
    def __init__(self):
        super().__init__()

    # функция возращает список кортежей загруженных курсов
    def fun_all_courses(self):
        self.cursor.execute(
            f'''SELECT bank_exchange, USD_buys, USD_sells, EUR_buys, EUR_sells, 
                                    RUB100_buys, RUB100_sells, EUR_USD_buys, EUR_USD_sells, date_time
                                    FROM EXCHANGE_RATES  WHERE citi_bank = '{self.ru_city}';  ''')
        self.cursor.connection.commit()  # сохраним изменения
        return self.cursor.fetchall()

    # функция возращает форматированную строку с курсами всех банков для передачи в message
    def fun_form_all_courses(self):
        self.list_cur = self.fun_all_courses()
        self.str_courses = 'Банк' + 'покупает / продает \n'.rjust(41, ' ')
        for self.element in self.list_cur:
            self.str_courses += ('=' * 31) + '\n' + (self.element[9])[0:16] + (
                ''.join(map(str, self.element[0]))).rjust(18, ' ') + '\n'
            self.str_courses += 'USD   '.rjust(29, ' ') + (
                '{:7.4f}  /  {:7.4f}'.format(self.element[1], self.element[2])) + '\n'
            self.str_courses += 'EUR   '.rjust(29, ' ') + (
                '{:7.4f}  /  {:7.4f}'.format(self.element[3], self.element[4])) + '\n'
            self.str_courses += '100 RUB   '.rjust(25, ' ') + (
                '{:7.4f}  /  {:7.4f}'.format(self.element[5], self.element[6])) + '\n'
            self.str_courses += 'EUR / USD   '.rjust(24, ' ') + (
                '{:7.4f}  /  {:7.4f}'.format(self.element[7], self.element[8])) + '\n'
        self.str_courses += ('=' * 31)
        return self.str_courses

    # функция возращает лучшие курсы
    def fun_best_courses(self):
        self.list_cur = self.fun_all_courses()  # получим список кортежей с курсами банков
        self.list_best_cur = []  # сюда соберем лучшие курсы (покупка - max; продажа - min)
        # [USD Покупает/Продает - 0,1 элемент, EUR Покупает/Продает - 2,3 элемент, 100RUB Покупает/Продает - 4,5 элемент, EUR/USD Покупает/Продает - 6,7 элемент, ]
        # [[Банк, Покупает], [Банк, Продает], [Банк, Покупает], [Банк, Продает],[Банк, Покупает], [Банк, Продает],[Банк, Покупает], [Банк, Продает]]
        for self.element in self.list_cur:  # цикл по кортежам - элементам списка
            if not len(self.list_best_cur):
                self.list_best_cur = [[self.element[0], self.element[1]], [self.element[0], self.element[2]],  # USD
                                      [self.element[0], self.element[3]], [self.element[0], self.element[4]],  # EUR
                                      [self.element[0], self.element[5]], [self.element[0], self.element[6]],  # 100RUB
                                      [self.element[0], self.element[7]],
                                      [self.element[0], self.element[8]]]  # EUR / USD
                continue

            if self.element[1] > self.list_best_cur[0][1]:
                self.list_best_cur[0][0] = self.element[0]
                self.list_best_cur[0][1] = self.element[1]

            if self.element[2] < self.list_best_cur[1][1]:
                self.list_best_cur[1][0] = self.element[0]
                self.list_best_cur[1][1] = self.element[2]

            if self.element[3] > self.list_best_cur[2][1]:
                self.list_best_cur[2][0] = self.element[0]
                self.list_best_cur[2][1] = self.element[3]

            if self.element[4] < self.list_best_cur[3][1]:
                self.list_best_cur[3][0] = self.element[0]
                self.list_best_cur[3][1] = self.element[4]

            if self.element[5] > self.list_best_cur[4][1]:
                self.list_best_cur[4][0] = self.element[0]
                self.list_best_cur[4][1] = self.element[5]

            if self.element[6] < self.list_best_cur[5][1]:
                self.list_best_cur[5][0] = self.element[0]
                self.list_best_cur[5][1] = self.element[6]

            if self.element[7] > self.list_best_cur[6][1]:
                self.list_best_cur[6][0] = self.element[0]
                self.list_best_cur[6][1] = self.element[7]

            if self.element[8] < self.list_best_cur[7][1]:
                self.list_best_cur[7][0] = self.element[0]
                self.list_best_cur[7][1] = self.element[8]

        return self.list_best_cur

    # функция возращает дату, время загруженных курсов
    def fun_datetime_courses(self):
        self.cursor.execute(
            f'''SELECT date_time FROM EXCHANGE_RATES  WHERE citi_bank = '{self.ru_city}' GROUP BY date_time;  ''')
        self.cursor.connection.commit()  # сохраним изменения
        return self.cursor.fetchone()

    # функция выбора случайных картинок
    def fun_image_file_name(self, dir='images'):
        self.list_img = []
        for root, dirs, files in os.walk('.'):
            for filename in files:
                if root == '.\\' + dir:
                    new_file = root[2:] + '/' + filename
                    self.list_img.append(new_file)
        img = ' '.join(map(str, (random.choices(self.list_img, weights=None, cum_weights=None, k=1))))  # случайный файл
        return img  # images/89334773_r3Pw_yMtdjw.jpg


cityBank = InteractionWithTelegrambot()

# new_mess = cityBank.fun_image_file_name()
# print(new_mess)
print('start Bot')


def fun_keyboard_TopCourses():
    best_courses = cityBank.fun_best_courses()
    keyboard_TopCourses = types.InlineKeyboardMarkup(row_width=3)  # клавиатура "Лучшие курсы"
    btn1 = types.InlineKeyboardButton(
        text=f'Получено {cityBank.fun_datetime_courses()[0]}. Обновить данные?',
        callback_data='btn1')
    keyboard_TopCourses.add(btn1)
    btn2 = types.InlineKeyboardButton(text=f'{(cityBank.fun_datetime_courses()[0])[0:16]}', callback_data='btn2')
    btn3 = types.InlineKeyboardButton(text='Банки покупают', callback_data='btn3')
    btn4 = types.InlineKeyboardButton(text='Банки продают', callback_data='btn4')
    btn5 = types.InlineKeyboardButton(text='USD', callback_data='btn5')
    btn6 = types.InlineKeyboardButton(text='{:5.4f}'.format(best_courses[0][1]), callback_data='btn6')
    btn7 = types.InlineKeyboardButton(text='{:5.4f}'.format(best_courses[1][1]), callback_data='btn7')
    btn8 = types.InlineKeyboardButton(text='EUR', callback_data='btn5')
    btn9 = types.InlineKeyboardButton(text='{:5.4f}'.format(best_courses[2][1]), callback_data='btn6')
    btn10 = types.InlineKeyboardButton(text='{:5.4f}'.format(best_courses[3][1]), callback_data='btn7')
    btn11 = types.InlineKeyboardButton(text='100RUB', callback_data='btn5')
    btn12 = types.InlineKeyboardButton(text='{:5.4f}'.format(best_courses[4][1]), callback_data='btn6')
    btn13 = types.InlineKeyboardButton(text='{:5.4f}'.format(best_courses[5][1]), callback_data='btn7')
    btn14 = types.InlineKeyboardButton(text='EUR/USD', callback_data='btn5')
    btn15 = types.InlineKeyboardButton(text='{:5.4f}'.format(best_courses[6][1]), callback_data='btn6')
    btn16 = types.InlineKeyboardButton(text='{:5.4f}'.format(best_courses[7][1]), callback_data='btn7')
    keyboard_TopCourses.add(btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,
                            btn16)
    btn17 = types.InlineKeyboardButton(text='Показать все курсы валют Банков', callback_data='btn17')
    keyboard_TopCourses.add(btn17)
    return keyboard_TopCourses


@bot.message_handler(commands=['start'])
def start_bot(message):
    # user_id =message.chat.id
    # first_name = message.chat.first_name
    # last_name = message.chat.last_name
    # username = message.chat.username
    # type = message.chat.type
    # #citiBank.fun_reg_users(message.chat.id, message.chat.first_name, message.chat.last_name, message.chat.username, message.chat.type)
    bot.send_message(message.chat.id, 'Хорошего времени суток!', reply_markup=fun_keyboard_TopCourses())



# объявляем метод для получения текстовых сообщений
@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.from_user.id,
                     'Приветствую Вас!\n'
                     'Ознакомтесь в режиме 24/7,\n'
                     'с актуальными курсами обмена иностранной валюты\n'
                     'в коммерческих банках г.Молодечно, Республики Беларусь.', reply_markup=fun_keyboard_TopCourses())
    bot.register_next_step_handler(message, fun_proceed)


def fun_proceed(message):
    bot.send_message(message.from_user.id, 'Уточните свой вопрос, пожалуйста.')  # можно дальше развивать сервис
    img = open(cityBank.fun_image_file_name(), 'rb')
    bot.send_photo(
        chat_id=message.chat.id,
        photo=img,
        caption='',
        reply_markup=fun_keyboard_TopCourses())
    bot.register_next_step_handler(message, start)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = fun_keyboard_TopCourses()
    if not call.message:
        pass

    if call.data == 'btn1':  # Обновить?
        img = open(cityBank.fun_image_file_name(), 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption='')
        cityBank.fun_get_courses()
        msg = 'pause'
        bot.send_message(call.message.chat.id, msg, reply_markup=fun_keyboard_TopCourses())

    if call.data == 'btn17':
        msg = cityBank.fun_form_all_courses()
        bot.send_message(call.message.chat.id, msg, reply_markup=fun_keyboard_TopCourses())


if __name__ == "__main__":
    bot.polling(none_stop=True)
