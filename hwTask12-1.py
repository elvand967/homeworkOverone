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
    if not number.isdigit(): #Состоит ли строка из цифр
        # winsound.PlaySound("Windows Foreground.wav", winsound.SND_FILENAME) # сигнал winsound об ошибке
        request = input('error! Некорректно введено число, повторить тест? (Y/N): ')
        if request == 'Y': continue
        elif request == 'y': continue
        else: break
    if len(number)!=7: #количество знаков в числе
        # winsound.PlaySound("Windows Foreground.wav", winsound.SND_FILENAME) # сигнал winsound об ошибке
        request = input('error! Число не 7-значное, повторить тест? (Y/N): ')
        if request == 'Y': continue
        elif request == 'y': continue
        else: break
    number = list(map(int,number))
    for i in number:
        if i % 2: OddN += 1
        else: EvenN += 1
    if EvenN > OddN:
        print(f'Четных цифр в числе больше, чем нечетных.\nсумма всех цифр числа: {sum(number)}')
    else:
        print(f'Нечетных цифр в числе больше, чем четных.\n'
              f'произведение 1-ой ({number[0]}); 3-ей ({number[2]}); и 6-ой ({number[5]}) '
              f'цифры: {(number[0]) * (number[2]) * (number[5])}')
    request = input('-------------\nПовторить тест? (Y/N): ')
    if request == 'Y':
        EvenN = OddN = 0
        continue
    elif request == 'y':
        EvenN = OddN = 0
        continue
    else: break
print('Программа завершила работу')