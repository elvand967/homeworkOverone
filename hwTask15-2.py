# Домашнее задание Задача №15-2
# Дан словарь с числовыми значениями.
# Необходимо их все перемножить и вывести на экран
while True:
    work = 1
    amount = input('Введите количество элементов словаря с числовыми значениями: ')
    if amount.isdigit():
        amount = int(amount)
        numericaldict = {a: (a+1) ** 2 for a in range(amount)}
        print(f'Иследуемый словарь: {numericaldict}')
    else:
        print('Некорректный ввод данных')
        if input('Повторить попытку? (Y/N): ').upper() == 'Y':
            continue
        else: break
    for k, v in numericaldict.items():
        work *= v
    print(f'Произведение всех значений словаря: {work}')
    if input('-------------\nПовторить тест? (Y/N): ').upper() == 'Y':
        continue
    else:
        break
print('Программа завершила работу')