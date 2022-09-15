# Домашнее задание Задача №28
# Допишите несколько атрибутов в класс с прошлого задания, продемонстрируйте их работу

class Car:
    def __init__(self):
        print ("легковой автомобиль")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 2020

car_a = Car()  # легковой автомобиль
print(car_a.name)  # corolla