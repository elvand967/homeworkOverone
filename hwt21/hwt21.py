# Домашнее задание Задача №21/1
# Клиент приходит в кондитерскую.
# Он хочет приобрести один или несколько видов продукции,
# а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и т.д.).
# Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке: С клавиатуры вводите название торта и его кол-во.
# n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке
# 6. До свидания.

def ContinueWork():
    if input('*****\nПродолжить работу? (Y/N): ').upper() != 'Y':
        return False
    else: return True
NutritionalValue = 'Пищевая ценность на 100 г продукта: '
Calories = 'Энергетическая ценность (калорийность): '
Unit = 'ед.изм.: '
Price = 'Цена за единицу: '
PackingWeight = 'Масса упаковки: '
currency = 'руб.'
ShoppingBasket = {}
confectionery = {
'Пряники "Шоколадный вкус"': [NutritionalValue +'белков - 7.0 г; жиров - 7.0 г; углеводов - 70 г, '+
                              Calories + '380 ккал',
                              'уп.',
                              4.50,  # цена за ед.изм.
                              PackingWeight + '300 г.'],
'Печенье "Буренушка"' : [NutritionalValue +'белков - 7.5 г; жиров - 19.2 г; углеводов - 63.2 г, '+
                              Calories + '456 ккал',
                              'уп.',
                              0.80, # цена за ед.изм.
                              PackingWeight + '100 г.'],
'Вафли "Белорусские"' : [NutritionalValue +'белков - 5.5 г; жиров - 34 г; углеводов - 57 г, '+
                              Calories + '550 ккал',
                              'уп.',
                              1.20,  # цена за ед.изм.
                              PackingWeight + '100 г.'],
'Торт "Спартак"' : [NutritionalValue +'белков - 6.3 г; жиров - 45.2 г; углеводов - 42.1 г, '+
                              Calories + '596 ккал',
                              'шт.',
                              27.03,  # цена за ед.изм.
                              PackingWeight + '1000 г.'],
'Вафельный батончик "Milx"':[NutritionalValue +'белков - 5 г; жиров - 33 г; углеводов - 59 г, '+
                              Calories + '550 ккал',
                              'шт.',
                              0.65,  # цена за ед.изм.
                              PackingWeight + '35 г.']
}
print('Добро пожаловать в наш магазин кондитерских изделий!')
while True:
    print('Введите цифру: 1 - Для просмотра описания товаров')
    print('Введите цифру: 2 - Для просмотра цен на товары')
    print('Введите цифру: 3 - Для просмотра количества товара')
    print('Введите цифру: 4 - Для просмотра всей информации о товарах')
    print('Введите цифру: 5 - Что бы приступить к покупкам')
    print('Для выхода из программы введите "N"')
    request = input('Сделайте свой выбор: ')
    if request.upper() =='N':
        break
    elif request == '1':
        for k, v in  confectionery.items():
            print(f'{k}\t{v[0]}')
        if not ContinueWork(): break
        else: continue
    elif request == '2':
        for k, v in  confectionery.items():
            print(f'{k}: {v[2]} {currency} за 1 {v[1]}')
        if not ContinueWork(): break
        else: continue
    elif request == '3':
        for k, v in  confectionery.items():
            print(f'{k}: {v[1]}. {v[3]}')
        if not ContinueWork(): break
        else: continue
    elif request == '4':
        for k, v in  confectionery.items():
            print(f'{k}: {v}')
        if not ContinueWork(): break
        else: continue
    elif request == '5':
        while True:
            print('Наш ассортимент:')
            for k, v in  confectionery.items():
                print(f'{k}: {v[2]} {currency} {v[1]}')
            print('***')
            if len(ShoppingBasket):
                print(f'В настоящий момент в козине {len(ShoppingBasket)} товар(а)')
                Sum = 0
                for k, v in ShoppingBasket.items():
                    print(k, v)
                    Sum +=v[2]
                print('Для оплаты покупок введите "S" или')
            else: print('В настоящий момент в козина пуста')
            NewProduct = input('Укажите через двоеточие ":", название товара и его количество, для добаления в карзину: ')
            if NewProduct.upper() == 'S':
                if len(ShoppingBasket):
                    print(f'Товары в карзине покупок: {ShoppingBasket}')
                    print(f'Цена чека покупок: {Sum} {currency}')
                    payment = input('Оплатить покупки? (Y/N) ')
                    if payment.upper() == 'Y':
                        ShoppingBasket.clear()
                        break
                else:
                    print('В настоящий момент в козина пуста')
            else:
                Product = NewProduct.split(':')
                for key,values in confectionery.items():
                    if key.upper().find(Product[0].upper()) >= 0:
                        ShoppingBasket[key] = [Product[1], values[1].strip(),round(values[2]*int(Product[1]),2),currency]
print('Программа завершила свою работу.\nДо свидания! ')
