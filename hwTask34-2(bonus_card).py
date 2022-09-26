# Домашнее задание Задача №34/2 (бонусная карта)
# Придумайте свой примеры видов полиморфизма. Прикрепите скриншоты или файл с ними.

# Покупатель рассчитывается за приобретенный товар в автоматической кассе самообслуживания.
# Отсканировал штрих код товара и наблюдает на мониторе сумму к оплате,
# а так-же предложением отсканировать номер бонусной карты или пропустить действие.
# После ввода номера бонусной карты, кассовой аппарат выводит итоговую сумму к оплате

import random
from datetime import datetime

class Product():
    default_products = None  # словарь товаров ({товар:цена за единицу,...}

    def __init__(self,products = default_products):
        self.products = products
        if self.products is None:
            # проработать ручной ввод
            #self.products = dict(input('Сформируйте номенклатуру товаров в формате {товар=цена за единицу,...}: '))
            self.products = {a+1: self.float_generator() for a in range(10)}

    @staticmethod
    def float_generator(start=0.0, end=100.0):  # генератор вещественных чисел (float)
        return round(random.uniform(start, end - 1), 2)

    def info(self):
        return f'номенклатура товаров: {self.products}'

class Chek(Product):
    default_date_purchase = None
    default_product = None
    default_amount_payable = None # подлежащая уплате сумма


    def __init__(self, date_purchase=default_date_purchase, product = default_product, amount_payable = default_amount_payable):
        super().__init__()
        self.date_purchase = date_purchase
        if date_purchase is None:
           self.date_purchase = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.product = product
        self.amount_payable = amount_payable
        if amount_payable is None:
           self.purchase_amount = self.goods_scanning()

    def goods_scanning(self): # сканирование товара
        self.product = int(input('Сканируйте товар (введите номер товара "1-10"): '))
        return self.products[self.product]

    def discount_card(self):
        card = input('сканируйте (введите номер) карты скидок\nпри ее отсутствии нажмите "ввод": ')
        if card == '':
            self.amount_payable = self.products[self.product]
        else:
            print('Вам предоставленна скидка 10 %')
            self.amount_payable = format(self.products[self.product]*0.9, '.2f')

    def info(self):
        n = 30
        print('='*n)
        print(f'дата/время совершения покупки:\n{self.date_purchase}')
        print(f'покупка товара: "{self.product}", по цене: {self.products[self.product]} руб.')
        self.discount_card()
        print(f'суума к оплате: {self.amount_payable} руб.')


m = Chek()
m.info()

# Сканируйте товар (введите номер товара "1-10"): 8
# ==============================
# дата/время совершения покупки:
# 24-09-2022 17:57
# покупка товара: "8", по цене: 18.0 руб.
# сканируйте (введите номер) карты скидок
# при ее отсутствии нажмите "ввод": 32
# Вам предоставленна скидка 10 %
# суума к оплате: 16.20 руб.