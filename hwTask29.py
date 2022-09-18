# Домашнее задание Задача №29
# Допишите по 2 динамических и статических свойства в класс с предыдущего задания. Продемонстрируйте их работу
class Car():
    car_count = 0          # Статический атрибут (поле) - ???
    default_color = 'Grey' #Статический атрибут (поле)

    def __init__(self, color, model):
        print("легковой автомобиль")
        self.name = "corolla"  # Статический атрибут (поле)
        self.make = "toyota"   # Статический атрибут (поле)
        self.model = model  # Динамический атрибут (поле)
        self.color = color  # Динамический атрибут (поле)
        Car.car_count += 1

new_car = Car('Red',2020)              # легковой автомобиль
print(new_car.make, new_car.name, new_car.model)     # toyota corolla 2020
print(new_car.default_color)           # Grey
print(new_car.color)                   # Red


