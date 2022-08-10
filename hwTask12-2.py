# Домашнее задание Задача №12/2
# Посчитать, сколько раз встречается определенная цифра(цифра – это от 0 до 9) в списке чисел.
# Количество введенных чисел в список и искомая цифра задаются с клавиатуры.
# Числа выбираются рандомно.
import random
DigitGuantity = 0
NumberDigits = int(input('Введите количество цифр в исходном числе: '))
DesiredFigure = int(input('Введите искомую цифру (от 0 до 9): '))
NumberList = [random.randint(0,9) for i in range(NumberDigits)]
Number = int(''.join(map(str, NumberList)))
for i in NumberList:
    if i == DesiredFigure:
        DigitGuantity += 1
print(f'В числе {Number} цифра {DesiredFigure} встречается: {DigitGuantity} раз(а)')

