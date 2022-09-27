# Домашнее задание Задача №26-2
# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями.
import random
def fun(x):
    if type(x) == tuple: # принят кротеж ( ) – последовательность неизменяемых объектов.
        n = 0
        for i in x:
            n += len(str(i))
        print(f'принят кортеж {x}, в котором,\nслов (элементов) всего: {len(x)}; длина их всех: {n} символа\n')
    elif type(x) == list: # принят список [ ]- упорядоченные изменяемые коллекции объектов произвольных типов
        n = 0
        for i in x:
            if type(i) == str:
                n += len(''.join(filter(str.isalnum, i))) # удаляя все не буквенно-цифровых символы в строке Python
        print(f'принят список {x}, в котором,\n'
              f'слов: {len(list(filter(lambda x: type(x) == str, x)))}, '
              f'в том числе букв: {n}; '
              f'чисел: {len(list(filter(lambda x: type(x) in (int, float), x)))}\n')
    elif type(x) == int:
        n = 0
        mylist = []
        for i in str(x):
            if int(i)%2:
                n +=1
                mylist.append(int(i))
        print(f'принято число "{x}", в котором нечётных цифр: {n} - {mylist}\n')
    elif type(x) == str: # принята строка
        print(f'принята строка "{x}", в которой букв: {len("".join(filter(str.isalnum, x)))}')
    else:
        print('Неизвестный тип')

fun(('зима','весна','лето','осень',2022))
fun([220013,'г. Минск','ул. Сурганова',43,508])
fun(random.randint((2**10),(10**10)))
fun('Общество с ограниченной ответственностью «ОВЕРВАН»')

# принят кортеж ('зима', 'весна', 'лето', 'осень', 2022), в котором,
# слов (элементов) всего: 5; длина их всех: 22 символа

# принят список [220013, 'г. Минск', 'ул. Сурганова', 43, 508], в котором,
# слов: 2, в том числе букв: 17; чисел: 3

# принято число "6583044983", в котором нечётных цифр: 4 - [5, 3, 9, 3]

# принята строка "Общество с ограниченной ответственностью «ОВЕРВАН»", в которой букв: 44
