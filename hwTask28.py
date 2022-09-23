# Домашнее задание Задача №28
# Допишите несколько атрибутов в класс с прошлого задания, продемонстрируйте их работу
from random import choice

class Car():
    car_count = 0
    def __init__(self):
        print ("легковой автомобиль")
        self.name = "corolla"
        self.make = "toyota"
        self.model = 2020
        self.color = choice(['white','black','red'])
        self.tires = choice(['Windforce Catchfors H/P 205/55 R16 91V',
                    'Kormoran Road Performance 205/55 R16 94V XL','DX640 225/40 ZR18 92W XL FR']) # Шины для авто
        Car.car_count += 1

car_a = Car()
print(f'№ {car_a.car_count} | {car_a.make} | {car_a.name}  | {car_a.model} г.в.\n'
      f'цвет: {car_a.color}  | шины: {car_a.tires}\n')

car_b = Car()
print(f'№ {car_b.car_count} | {car_b.make} | {car_b.name}  | {car_b.model} г.в.\n'
      f'цвет: {car_b.color}  | шины: {car_b.tires}\n')

car_c = Car()
print(f'№ {car_c.car_count} | {car_c.make} | {car_c.name}  | {car_c.model} г.в.\n'
      f'цвет: {car_c.color}  | шины: {car_c.tires}\n')

# легковой автомобиль
# № 1 | toyota | corolla  | 2020 г.в.
# цвет: black  | шины: Kormoran Road Performance 205/55 R16 94V XL
#
# легковой автомобиль
# № 2 | toyota | corolla  | 2020 г.в.
# цвет: white  | шины: Kormoran Road Performance 205/55 R16 94V XL
#
# легковой автомобиль
# № 3 | toyota | corolla  | 2020 г.в.
# цвет: red  | шины: DX640 225/40 ZR18 92W XL FR

