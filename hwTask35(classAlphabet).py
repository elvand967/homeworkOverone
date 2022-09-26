# Домашнее задание Задача №35
# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены
# два динамических свойства: 1) lang - язык и 2) letters - список букв.
# Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка,
# состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
# относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе
# он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке
# Тесты:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке

class Alphabet():
    default_lang = ['en','ru']
    default_letters = None
    def __init__(self, lang = None, letters = default_letters):
        self.lang  = lang
        if self.lang is None:
            self.lang = input(f'Введите язык тестируемого алфавита (варианты {self.default_lang}): ')
        self.letters = letters
        if self.letters is None:
            self.letters = self.generator_alph(self.lang)

    @staticmethod
    def generator_alph(language):
        capital_letter_en = [65,91] # Значение ASCII A-Z лежит в диапазоне 65-90 (таблица кодов символов Windows (Win-1251))
        letter_en = [97,123]        # Значение ASCII a-z находится в диапазоне 97 – 122
        # capital_letter_ru = [192,224]  # ???-Значение ASCII А-Я находится в диапазоне 192 – 223 !!!проблемы с кодировкой
        # letter_ru = [224,256]          # ???-Значение ASCII а-я находится в диапазоне 224 – 255 !!!проблемы с кодировкой
        capital_letter_ru = [1040,1072]  # Значение Chr(А-Я) находится в диапазоне 1040 - 1071
        letter_ru = [1072,1103]          # Значение Chr(а-я) находится в диапазоне 1072 - 1102
        letters = []
        if language == 'en':
            n = letter_en[0] - capital_letter_en[0]
            for i in range(capital_letter_en[0],capital_letter_en[1]):
                letters.append(chr(i)+chr(i+n))
        elif language == 'ru':
            n = letter_ru[0] - capital_letter_ru[0]
            for i in range(capital_letter_ru[0],capital_letter_ru[1]):
                letters.append(chr(i)+chr(i+n))
                if chr(i) == 'Е':
                    letters.append('Ёё')
        # elif  language == 'ru':
        #     for i in range(ord('А'), ord('Я')):
        #         letters.append([chr(i),i])
        else: letters = 'неизвестный язык'
        return letters

    def print(self):
        print(f'алфавит: {self.letters}')

    def letters_num(self):
        return len(self.letters)

    def letter_en_control(self, s):
        if self.lang != 'en':
            return f'Согласно задания метод контролирует только английский алфавит\n' \
                   f'поиск буквы "{s}" отменен'
        flag = False
        if self.letters.count(s.upper()+s.lower())>0:
            flag = True

        return (flag and f'Искомая буква "{s}" относится к английскому алфавиту') \
               or f'Искомая буква "{s}" не относится к английскому алфавиту'


Alph = Alphabet()
Alph.print()
print(f'букв в алфавите: {Alph.letters_num()}')
# print(Alph.letter_en_control(input('Введите искомую букву: ')))
print(Alph.letter_en_control('F'))
print(Alph.letter_en_control('Щ'))