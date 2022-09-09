# Домашнее задание Задача №26-1
# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

def f_sum(mylist):
    return float(mylist[0]) + float(mylist[1])
def f_sub(mylist):
    return float(mylist[0]) - float(mylist[1])
def f_mult(mylist):
    return float(mylist[0]) * float(mylist[1])
def f_div(mylist):
    if float(mylist[1]) == 0:
        return 'Деление на "0" недопустимо!'
    return float(mylist[0]) / float(mylist[1])
while True:
    mo = input('Для выхода из программы введите "0"\n'
               'или введите необходимую математическую операцию (число + - * / второе число): ')
    if mo == '0':
        break
    elif mo.find('+')>=0:
        mylist = mo.split('+')
        print(f'{mo} = {f_sum(mylist)}')
    elif  mo.find('-')>=0:
        mylist = mo.split('-')
        print(f'{mo} = {f_sub(mylist)}')
    elif  mo.find('*')>=0:
        mylist = mo.split('*')
        print(f'{mo} = {f_mult(mylist)}')
    elif  mo.find('/')>=0:
        mylist = mo.split('/')
        print(f'{mo} = {f_div(mylist)}')
    else: print('Некорректный ввод данных')
print('Программа завершила свою работу')

