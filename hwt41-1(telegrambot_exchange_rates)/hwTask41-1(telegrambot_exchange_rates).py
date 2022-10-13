#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Домашнее задание. Задача №41-1 (Telegrambot erfByn_bot v1.0)
# Разработка телеграмм бота, который по запросу предоставляет курсы валют
# комерческих банков РБ в заданном населенном пункте
# первоисточник основы: https://www.youtube.com/watch?v=4L57oY3J378
# https://github.com/elvand967/TelegrambotExchangeRates.git
# 5655341772:AAEFesP0r7MXMqPPyXYvbeCjtzZQQVnnx2A
import requests
from bs4 import BeautifulSoup
from transliterate import translit

list_bank_by = ['Абсолютбанк',
                'Альфа-Банк',
                'Банк Дабрабыт',
                'Банк Решение',
                'Белагропромбанк',
                'Беларусбанк',
                'Банк БелВЭБ',
                'Белгазпромбанк',
                'Белинвестбанк',
                'Сбер Банк',
                'БСБ Банк',
                'БТА Банк',
                'ВТБ Беларусь',
                'МТБанк',
                'Paritetbank',
                'Приорбанк',
                'РРБ-Банк',
                'Статусбанк',
                'ТехноБанк',
                'ТК Банк',
                'Франсабанк',
                'Цептер Банк']
ru_city = 'Молодечно'
# заголовки - описывают пользователя
# (если их не передать то будет считаться что заходит бот и запрос не будет обработан)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
list_currencies = ['Доллар США', 'Евро', 'Российский рубль100', 'Польский злотый10', 'Гривна100']


class ExchangeRates:
    global ru_city
    global headers
    global list_bank_by
    global list_currencies

    def __init__(self, en_citi=None, list_bank_by=None):
        self.en_city = en_citi
        if self.en_city is None:
            self.en_city = self.fun_ru_city()
        # источник info:
        self.url = f'https://myfin.by/currency/{self.en_city}'
        self.headers = headers

        self.list_bank_by = list_bank_by
        if self.list_bank_by is None:
            self.list_bank_by = list_bank_by

        self.list_currencies = list_currencies
        self.data_super = []
        self.data = []
        self.fun_pivot_tables()

    def get_list_bank_by(self):
        pass

    def fun_ru_city(self, citi=ru_city):
        if citi is None or citi == '':
            citi = input('Введите название населенного пункта')
        en_city = translit(citi, language_code='ru', reversed=True)
        return en_city

    def fun_pivot_tables(self):
        res = requests.get(self.url, self.headers).text
        soup = BeautifulSoup(res, 'lxml')

        for tables in soup.select("table tr"):
            n = [item.get_text(strip=True) for item in tables.select("td")]
            if len(n) == 0 or n[0] == '':
                continue
            if n[0] in list_currencies:
                for i in range(1, len(n)):
                    if '+' in n[i]:
                        n[i] = n[i].split('+')
                        n[i][1] = '+' + n[i][1]
                    elif '-' in n[i]:
                        n[i] = n[i].split('-')
                        n[i][1] = '-' + n[i][1]
                self.data_super.append(n)
                continue
            if not n[0] in list_bank_by:
                continue
            else:
                self.data.append(n)

        for i in self.data_super:
            print(i)
        print('*****')
        for i in self.data:
            print(i)


molo = ExchangeRates()
