# Домашнее задание Задача №15-2
# Дан словарь с числовыми значениями.
# Необходимо их все перемножить и вывести на экран

while True:
    work = 0
    amount = input('Введите количество элементов словаря с числовыми значениями: ')
    if amount.isdigit():
        amount = int(amount)
        numericaldict = {a: a ** 2 for a in range(1,amount)}
        print(f'иследуемый словарь: {numericaldict}')
    else:
        print('Некорректный ввод данных')
        if input('Повторить попытку? (Y/N): ').upper() == 'Y':
            continue
        else: break
