# Домашнее задание Задача №34 (ведомость коммунальных платежей за воду)

# В многоэтажных домах (House_number) с квартирами (count_apartments) от 4 до 16, по заданной улице (street), населенного пункта (locality)
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
    default_street = 'В.Гостинец'
    default_house_number = 124
    default_locality = 'Молодечно'
    default_count_apartments = None

    def __init__(self, street=default_street, house_number=default_house_number,
                 locality=default_locality, count_apartments = default_count_apartments):
        self.street = street
        if self.street is None:
            self.street = input('Укажите название улицы: ')
        self.house_number = house_number
        if self.house_number is None:
            self.house_number = int(input('Укажите номер дома: '))
        self.locality = locality
        if self.locality is None:
            self.locality = input('Укажите населенный пункт: ')
        self.count_apartments = count_apartments
        if self.count_apartments is None:
            # self.count_apartments = input('Укажите количество квартир в доме: ')
            self.count_apartments = self.even_generator(4, 16)

    @staticmethod
    def even_generator(start, end):  # генератор четных чисел int
        n = random.randint(start, end - 1)
        return (n % 2 == 0 and n) or n + 1

    @staticmethod
    def float_generator(start=0.0, end=100.0):  # генератор вещественных чисел (float)
        return round(random.uniform(start, end - 1), 2)

    def info(self):
        print(f'Class name: {type(self).__name__}')
        print(f'населенный пункт: {self.locality}')
        print(f'улица: {self.street}')
        print(f'дом: {self.house_number}')
        print(f'всего квартир: {self.count_apartments}')
        print('---------------------------------')

class Flat(House):
    apartment_number = -1  # номер квартиры
    # шапка ведомости создает дополнительный экземпляр. корректировка (-1)
    default_count_people = None # прописанно человек
    default_subsidies = None    # прим. льготный расчет (bool)
    default_water_meter = None  # наличие счетчиков (bool)
    default_water = None        # кол-во воды в месяц (bool)
    norm_water_people = 0.8     # норма чел/сут м3 (float)
    norm_water_people_subsidies = 0.46
    water_price = 2.2222              # тариф руб*1м3
    water_price_subsidies = 2.1835

    def __init__(self, count_people=default_count_people, subsidies=default_subsidies,
                 water_meter=default_water_meter, water=default_water):
        super().__init__()
        self.count_people = count_people
        if self.count_people is None:
            self.count_people = random.randint(1, 5)
        self.subsidies = subsidies
        if subsidies is None:
            self.subsidies = random.choice([True, False])
            # self.subsidies = bool(random.getrandbits(1))  # более быстрый генератор, но воспринимается сложнее
        self.water_meter = water_meter
        if water_meter is None:
            self.water_meter = random.choice([True, True, True, False])
        self.water = water
        if water is None:
            # self.water = float(input('Укажите объем использованной воды (м3): '))
            self.water = self.get_water()
        Flat.apartment_number += 1

    def get_water(self): #  функция-генератор, получения расчетного объема воды
        if self.water_meter:  # если установлен счетчик воды
            return format(self.float_generator(4.0,20.0), '.2f')
        else:  # пока условно число дней в месяце примем 30
            if self.subsidies:  # если применен льготный тариф
                return format(self.count_people * self.norm_water_people_subsidies * 30, '.2f')
            else:  # если применен тариф обеспечивающий полное возмещение экономически обоснованных затрат
                return format(self.count_people * self.norm_water_people * 30, '.2f')

    def get_amount(self): #  функция получения суммы счета за воду
        if self.subsidies:  # если применен льготный тариф
            return format(float(self.water) * self.water_price_subsidies, '.2f')
        else:
            return format(float(self.water) * self.water_price, '.2f')

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

    def __int__(self, water=default_water):
        super().__init__()
        self.water = water
        if water is None:
            self.water = self.water()

    @staticmethod
    def get_reporting_period():
        str_month = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
                     7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
        current_datetime = datetime.now()
        if current_datetime.month != 1:
            get_month = str_month[current_datetime.month - 1]
            get_year = str(current_datetime.year) + 'г.'
        else:
            get_month = str_month[12]
            get_year = str(current_datetime.year - 1) + 'г.'
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
        print('=' * n)
        self.objs = [Flat for i in range(self.count_apartments)]
        for obj in self.objs:
            object = obj()
            print(f'|\t{object.apartment_number}\t|\t\t{object.count_people}\t\t|\t{object.subsidies}\t\t\t|'
                  f'\t{object.water_meter}\t\t\t|\t{object.water}\t|\t{object.get_amount()}\t|')
        print('=' * n)
        print(f'тариф за воду, обесп. полное возмещение 1м3: {self.water_price} руб.;'
              f' (субсидируемый 1м3: {self.water_price_subsidies} руб.)')
        print(f'норма при отсутствии приборов учета на 1-го чел в сутки: {self.norm_water_people} м3;'
              f' (субсидируемый: {self.norm_water_people_subsidies} м3.)')



ved_water = Water_supply_record_sheet()
ved_water.info()

# 			ведомость коммунальных платежей за потребленную воду и водоотведение
# населенный пункт: Молодечно
# улица: В.Гостинец
# дом: 124
# отчетный период: Август 2022г.
#
# =======================================================================================
# |	№	|	проживает	|	тариф,			|	наличие			|	объем	|	сумма	|
# |	кв.	|	(зарег.)	|	субсидируемый	|	приборов		|	воды	|			|
# |		|	чел.		|	государством	|	учеты воды		|	 м3		|	руб.	|
# =======================================================================================
# |	1	|		5		|	True			|	False			|	69.00	|	150.66	|
# |	2	|		1		|	True			|	True			|	9.75	|	21.29	|
# |	3	|		1		|	True			|	True			|	18.09	|	39.50	|
# |	4	|		4		|	True			|	False			|	55.20	|	120.53	|
# |	5	|		3		|	False			|	True			|	5.74	|	12.76	|
# |	6	|		2		|	True			|	True			|	17.29	|	37.75	|
# =======================================================================================
# тариф за воду, обесп. полное возмещение 1м3: 2.2222 руб.; (субсидируемый 1м3: 2.1835 руб.)
# норма при отсутствии приборов учета на 1-го чел в сутки: 0.8 м3; (субсидируемый: 0.46 м3.)