# Домашнее задание Задача №33 (Alex & SmallHouse)
# Прикрепите файл с кодом с практической работы по теме 38

# В предыдущем задании допишите:
# Класс House
# 1. Создайте класс House
# 2. Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price.
# 3. Свои начальные значения они получают из параметров метода __init__()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом
# данной скидки.
# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
# Класс Human
# 1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома:
# уменьшать количество денег на счету и присваивать ссылку на только что купленный дом.
# В качестве аргументов данный метод принимает объект дома и его цену.
# 2. Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и
# совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка
# на дом и размер скидки


class Human:
    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None
        print(f'Создан объект класса: {type(self).__name__}')

    def info(self):
        #print(f'class: {type(self).__name__}')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}')
        print(f'Default age: {Human.default_age}')

    def earn_money(self, amount): # заработок (увеличиваем баланс счета)
        self.__money += amount
        print(f"Вы заработали {amount}. У Вас {self.__money} денег")

    def __make_deal(self, house, price): # учет финансов после покупки дома, статус дома
        self.__money -= price # списываем со счета сумму затраченную на покупку дома
        self.__house = house # запоминаем объект дома
        print(f'Сделка состоялась!!! Поздравляем с приобретением новой недвижимости: {self.__house}')

    def buy_house(self,house,discount):  # покупка дома,
        # принимаем имя переменной с сылкой на экземпляр дома и скидку на его стоимость
        price = house.final_price(discount) # считаем стоимость дома с учетом скидки
        if price>self.__money:
            print("У Вас недостаточно денег")
        else:
            self.__make_deal(house,price)

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
        print(f'Создан объект класса {type(self).__name__}') # вывод на печать имя класса создоваемых объектов

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        return final_price

class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':
    print('!!!Запрос к статической функции: Human.default_info(), еще до создания объекта, для получения значений по умолчанию класса:')
    Human.default_info()
    Alex = Human('Alex', 25)
    print(f'!!!Запрос к обычному методу "Alex.info()" экземпляра класса: {type(Alex).__name__}, для получения значений аргументов объекта:')
    Alex.info()
    drozd = SmallHouse(10000)
    print('!!!Попытка купить домик в Дроздах используя метод: Alex.buy_house(drozd,10))')
    Alex.buy_house(drozd,10)
    print('!!!Усиленно работаем, работаем, работаем...')
    Alex.earn_money(10000)
    Alex.earn_money(5000)
    print('!!!Вторая попытка купить домик в Дроздах используя метод: Alex.buy_house(drozd,10))')
    Alex.buy_house(drozd, 10)
    print('!!!Еше раз поинтересуемся положением дел у Alex:')
    Alex.info()

    # !!!Запрос к статической функции: Human.default_info(), еще до создания объекта, для получения значений по умолчанию класса:
    # Default name: No name
    # Default age: 0
    # Создан объект класса: Human
    # !!!Запрос к обычному методу "Alex.info()" экземпляра класса: Human, для получения значений аргументов объекта:
    # Name: Alex
    # Age: 25
    # Money: 0
    # House: None
    # Создан объект класса SmallHouse
    # !!!Попытка купить домик в Дроздах используя метод: Alex.buy_house(drozd,10))
    # У Вас недостаточно денег
    # !!!Усиленно работаем, работаем, работаем...
    # Вы заработали 10000. У Вас 10000 денег
    # Вы заработали 5000. У Вас 15000 денег
    # !!!Вторая попытка купить домик в Дроздах используя метод: Alex.buy_house(drozd,10))
    # Сделка состоялась!!! Поздравляем с приобретением новой недвижимости: <__main__.SmallHouse object at 0x000001B02EB80370>
    # !!!Еше раз поинтересуемся положением дел у Alex:
    # Name: Alex
    # Age: 25
    # Money: 6000.0
    # House: <__main__.SmallHouse object at 0x000001B02EB80370>