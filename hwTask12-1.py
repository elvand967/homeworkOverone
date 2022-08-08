# Домашнее задание Задача №12/1
# С клавиатуры вводится 7-значное число.
# Если четных цифр в нем больше, чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 цифры.

EvenN = 0 # кол-во четных чисел
OddN = 0  # кол-во нечетных чисел
number = list(map(int,input('Введите произвольное 7-значное число: ')))
for i in number:
    if int(i) % 2:
        OddN += 1
    else:
        EvenN += 1

if EvenN > OddN:
    print(f'Четных цифр в числе больше, чем нечетных.\nсумма всех цифр числа: {sum(number)}')
else:
    print(f'Нечетных цифр в числе больше, чем четных.\n'
          f'произведение 1-ой ({number[0]}); 3-ей ({number[2]}); и 6-ой ({number[5]}) '
          f'цифры: {(number[0]) * (number[2]) * (number[5])}')
