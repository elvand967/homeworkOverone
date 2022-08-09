# Домашнее задание Задача №12/1
# С клавиатуры вводится 7-значное число.
# Если четных цифр в нем больше, чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 цифры.
import winsound
EvenN = OddN = 0 # кол-во четных, нечетных чисел
while True:
    #number = list(map(int,input('Введите произвольное 7-значное число: ')))
    number = input('Введите произвольное 7-значное число: ')
    # Контроль ввода
    if not number.isdigit() or int(number[0]) == 0: #Состоит ли строка из цифр, первая цифра не 0
        # winsound.PlaySound("Windows Foreground.wav", winsound.SND_FILENAME) # сигнал winsound об ошибке
        request = input('error! Некорректно введено число, повторить тест? (Y/N): ')
        if request.upper() == 'Y': continue # Str.upper() - Преобразование строки к верхнему регистру
        else: break
    if len(number)!=7: #количество знаков в числе
        # winsound.PlaySound("Windows Foreground.wav", winsound.SND_FILENAME) # сигнал winsound об ошибке
        request = input('error! Число не 7-значное, повторить тест? (Y/N): ')
        if request.upper() == 'Y': continue
        else: break
    number = list(map(int,number))
    for i in number:
        if i == 0: continue
        elif i % 2: OddN += 1
        else: EvenN += 1
    if EvenN > OddN:
        print(f'Четных цифр в числе больше, чем нечетных.\nСумма всех цифр числа: {sum(number)}')
    elif EvenN < OddN:
        print(f'Нечетных цифр в числе больше, чем четных.\n'
              f'Произведение 1-ой ({number[0]}); 3-ей ({number[2]}); и 6-ой ({number[5]}) '
              f'цифры: {(number[0]) * (number[2]) * (number[5])}')
    else:print(f'Нечетных и четных цифр в числе равное количество.\n'
              f'Сумма всех цифр числа: {sum(number)}\n'
              f'Произведение 1-ой ({number[0]}); 3-ей ({number[2]}); и 6-ой ({number[5]}) '
              f'цифры равно: {(number[0]) * (number[2]) * (number[5])}')

    request = input('-------------\nПовторить тест? (Y/N): ')
    if request.upper() == 'Y':
        EvenN = OddN = 0
        continue
    else: break
print('Программа завершила работу')