# Домашнее задание Задача №30
# Два метода в классе, один принимает в себя либо строку, либо число
# Если передают строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова,
# выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа
# Длину строки и числа искать во втором методе

class Example():

    def __init__(self):
        self.f_test = True
        self.str_test = input('Введите строку, либо число: ')
        if self.str_test.isalpha():
            self.str_num = 'й строки'
            self.all_gls_ru_en = 'ауоыиэяюёеaeiouy'
            self.list_gls = []
            self.list_sgls = []
            for i in self.str_test:
                if self.all_gls_ru_en.find(i)>=0:
                    self.list_gls.append(i)
                else: self.list_sgls.append(i)
            self.mpn = len(self.list_gls) * len(self.list_sgls)
            print(f'произведение гласных и согласных букв: {self.mpn}')
            if self.mpn <= self.len_ex():
                print(f'гласные буквы: {self.list_gls}')
            else: print(f'coгласные буквы: {self.list_sgls}')

        elif self.str_test.isdigit():
            self.str_num = 'го числа'
            self.sum_even_digits = 0
            list_num = []
            for i in self.str_test:
                if not int(i) % 2:
                    list_num.append(int(i))
                    self.sum_even_digits += int(i)
            print(f'произведение суммы чётных цифр ({list_num} = {self.sum_even_digits}) на'
                  ' длину числа: ',self.sum_even_digits * self.len_ex())

        else:
            self.f_test = False
            print('Введены недопустимые символы или сочетание цифр и букв')

    # def __del__(self):
    #     print ('Объект (экземпляр класса) удален')

    def len_ex(self):
        return len(self.str_test)

def continuation():
    repeat = input('Продолжить работу (Y/N): ')
    if repeat.upper() == 'Y': return True
    else: return False

while True:
    new_test = Example()
    if new_test.f_test:
        print(f'длинна тестируемо{new_test.str_num}: {new_test.len_ex()}')
    # else: new_test.__del__()
    if not continuation(): break

print('Программа завершила свою работу.')

