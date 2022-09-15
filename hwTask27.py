# Домашнее задание Задача №27
# Напишите пример любого класса и создайте его объект

class Car:
    def __init__(self):
        print ("легковой автомобиль")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 2020

car_a = Car()  # легковой автомобиль
print(car_a.name)  # corolla