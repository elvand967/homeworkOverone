# Домашнее задание Задача №34 (ведомость коммунальных платежей за воду)

# В многоэтажных домах (House_number) с квартирами (count_apartments) от 4 до 20, по заданной улице (street), населенного пункта (locality)
# в некоторых квартирах (apartment_number), с проживающими там некотором количестве людей (count_people),
# пользующимися льготами, а также люди возмещающие экономически обоснованные затраты,
# установлен счетчик на воду, в других нет.
# в ЖРУ поставленна задача подготовить ведомость счетов за потребленную воду и водоотведение для всех жильцов выбранного дома
# с учетом действующих тарифов:
# 1. Для квартир оснащенных приборами индивидуального учета расхода воды за потребление и водоотведение применяються Тарифы:
#   - Фиксированный тариф (subsidies = True), субсидируемый государством: 2,1835 руб. за 1 м3;
#   - Фиксированный тариф (subsidies = False), обеспечивающий полное возмещение экономически обоснованных затрат 2,2222  руб. за 1 м3.
# 2. Для квартир НЕоснащенных приборами индивидуального учета расхода воды исходя из нормы расхода на 1-го человека в сутки:
#   - Норма водопотребления лиц имеющих льготу(subsidies = True), субсидируемых государством: 230 л + 230 л. (+водоотведение);
#   - Норма водопотребления лиц (subsidies = False), обеспечивающий полное возмещение экономически обоснованных затрат
#     400 л + 400 л. (+водоотведение).
import random
from datetime import datetime

class House():
    count_apartments = None
    default_street = 'В.Гостинец'
    default_house_number = 124
    default_locality = 'Молодечно'
    default_count_apartments = None

    def __init__(self, street = default_street, house_number=default_house_number, locality=default_locality):
        self.street = street
        if self.street is None:
            self.street = input('Укажите название улицы: ')
        self.house_number = house_number
        if self.house_number is None:
            self.house_number = int(input('Укажите номер дома: '))
        self.locality = locality
        if self.locality is None:
            self.locality = input('Укажите населенный пункт: ')

    @staticmethod
    def even_generator(start=1, end=1000000):  # генератор четных чисел int
        n = random.randint(start, end - 1)
        return (n % 2 == 0 and n) or n + 1

    @classmethod
    def get_count_apartments(cls, count_apartments=default_count_apartments):
        cls.count_apartments = count_apartments
        if cls.count_apartments is None:
            cls.count_apartments = cls.even_generator(4, 20)  # генерируем четное количество квартир
        return cls.count_apartments

    def info(self):
        print(f'Class name: {type(self).__name__}')
        print(f'населенный пункт: {self.locality}')
        print(f'улица: {self.street}')
        print(f'дом: {self.house_number}')
        print(f'всего квартир: {self.count_apartments}')
        print('---------------------------------')



class Flat(House):
    apartment_number = -1 # шапка ведомости создает дополнительный экземпляр. корректировка (-1)
    default_count_people = None
    default_subsidies = None
    default_water_meter = None


    def __init__(self, count_people=default_count_people, subsidies = default_subsidies,
                 water_meter = default_water_meter):
        super().__init__()
        self.count_people = count_people
        if self.count_people is None:
            self.count_people = random.randint(1, 5)
        self.subsidies = subsidies
        if subsidies is None:
            #self.subsidies = random.choice([True, False])
            self.subsidies = bool(random.getrandbits(1)) # более быстрый генератор, но воспринимается сложнее
        self.water_meter = water_meter
        if water_meter is None:
            self.water_meter = random.choice([True,True,True, False])
            #self.water_meter = bool(random.getrandbits(1)) # более быстрый генератор, но воспринимается сложнее
        Flat.apartment_number += 1

    def info(self):
        print(f'Class name: {type(self).__name__}')
        print(f'населенный пункт: {self.locality}')
        print(f'улица: {self.street}')
        print(f'дом: {self.house_number}')
        print(f'квартира: {self.apartment_number}')
        print(f'проживает (зарегестрированно): {self.count_people} человек(а)')
        print(f'тариф субсидируемый государством: {self.subsidies}')
        print('--------------------------------------------')

class Water_supply_record_sheet(Flat):
    default_water = None
    default_water_meter = None


    def water(self):
        pass

    def __int__(self,water = default_water):
        super().__init__()
        self.water = water
        if water is None:
            self.water = self.water()




    @staticmethod
    def get_reporting_period():
        str_month = {1:'Январь', 2:'Февраль', 3:'Март', 4:'Апрель', 5:'Май', 6:'Июнь',
                     7:'Июль', 8:'Август', 9:'Сентябрь', 10:'Октябрь', 11:'Ноябрь', 12:'Декабрь'}
        current_datetime = datetime.now()
        if current_datetime.month != 1:
            get_month = str_month[current_datetime.month - 1]
            get_year = str(current_datetime.year) + 'г.'
        else:
            get_month = str_month[12]
            get_year = str(current_datetime.year -1) + 'г.'

        return get_month + ' ' + get_year

    def info(self):
        n = 89
        print('\t\t\tведомость коммунальных платежей за потребленную воду и водоотведение')
        print(f'населенный пункт: {self.locality}')
        print(f'улица: {self.street}')
        print(f'дом: {self.house_number}')
        print(f'отчетный период: {self.get_reporting_period()}\n')
        print('=' * n)
        print(f'|\t№\t|\tпроживает\t|\tтариф,\t\t\t|\tналичие\t\t\t|\tобъем\t|\tсумма\t|')
        print(f'|\tкв.\t|\t(зарег.)\t|\tсубсидируемый\t|\tприборов\t\t|\tводы\t|\t\t\t|')
        print(f'|\t\t|\tчел.\t\t|\tгосударством\t|\tучеты воды\t\t|\t м3\t\t|\tруб.\t|')
        print('='* n)
        self.apartments = House.get_count_apartments()
        self.objs = [Flat for i in range(self.apartments)]
        for obj in self.objs:
            object = obj()
            print(f'|\t{object.apartment_number}\t|\t\t{object.count_people}\t\t|\t{object.subsidies}\t\t\t|'
                  f'\t{object.water_meter}\t\t\t|\t{self.water()}\t|\t"test"\t|')
        print('=' * n)

ved_water = Water_supply_record_sheet()
ved_water.info()
