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
Unit = 'Единица измерения: '
Price = 'Цена за единицу: '
PackingWeight = 'Масса упаковки: '
confectionery = {
'Пряники «Шоколадный вкус»': [NutritionalValue +'белков - 7.0 г; жиров - 7.0 г; углеводов - 70 г, '+
                              Calories + '380 ккал',
                              Unit + 'упаковка',
                              Price + '4.50',
                              PackingWeight + '300 г.'],
'Печенье «Буренушка»' : [NutritionalValue +'белков - 7.5 г; жиров - 19.2 г; углеводов - 63.2 г, '+
                              Calories + '456 ккал',
                              Unit + 'упаковка',
                              Price + '0.80',
                              PackingWeight + '100 г.'],
'Вафли «Белорусские»' : [NutritionalValue +'белков - 5.5 г; жиров - 34 г; углеводов - 57 г, '+
                              Calories + '550 ккал',
                              Unit + 'упаковка',
                              Price + '1.20',
                              PackingWeight + '100 г.'],
'Торт «Спартак»' : [NutritionalValue +'белков - 6.3 г; жиров - 45.2 г; углеводов - 42.1 г, '+
                              Calories + '596 ккал',
                              Unit + 'шт',
                              Price + '27.03',
                              PackingWeight + '1000 г.'],
'Вафельный батончик «Milx»':[NutritionalValue +'белков - 5 г; жиров - 33 г; углеводов - 59 г, '+
                              Calories + '550 ккал',
                              Unit + 'шт',
                              Price + '0.65',
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
            print(f'{k} - {v[0]}')
        if not ContinueWork(): break
        else: continue
    elif request == '2':
        for k, v in  confectionery.items():
            print(f'{k}: {v[2]} руб. {v[1]}')
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

print('Программа завершила свою работу.\nДо свидания! ')
