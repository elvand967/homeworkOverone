#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Домашнее задание. Задача №38-1 (PyQT5 calculator_v2.0)
# Дополните код предыдущего модуля. Добавьте кнопки %, // и возведение в квадрат.

# Делаем необходимые импорты. Основные виджеты расположены в PyQt5.QtWidgets.
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont # для вставки иконки создаём объект шрифта
import sys

# создаем класс Calculator, который наследует класс QWidget из библиотеки PyQt5
class Calculator(QWidget):
    def __init__(self):
        super().__init__() # подключаем весь инициализатор родительского класса QWidget
        self.initUI() # метод, которому дилигируется создание UI (создание картинки, окна программы, кнопки и т.д.)
        self.my_input = [] # объявим списки фунционалов (пустой массив)
        self.operand_1 = []# объявим -/-
        self.operand_2 = []# объявим -/-
        self.m = 0.0  # объявим -/- память

    def initUI(self):
        self.setGeometry(300, 300, 280, 370)
        self.setWindowTitle("Калькулятор v2.0") # Устанавливаем название приложения, отражающееся в окне виджета
# Для работы с методами self.label в начале импортировали библиотеку QLabel
        self.setWindowIcon(QIcon('icon.png'))  # QIcon получает путь к нашей иконке для отображения
        self.font = QFont()  # создаём объект шрифта
        self.font.setFamily("Rubik")  # название шрифта
        self.font.setUnderline(False)  # подчёркивание

        self.label_story = QLabel(self)  # поле, отвечающее за вывод порядка набора кнопок
        self.label_story.setText('')  # значение поля по умолчанию
        #self.label_story.setAlignment(Qt.AlignRight)  # (Qt.AlignRight)
        self.label_story.resize(260, 95)  # задаем размер виджета  ширину и высоту в пикселях
        self.label_story.move(10, -30)  # задаем координаты положения по умолчанию виджета на монитору
        self.font.setPointSize(10)  # размер шрифта
        self.label_story.setFont(self.font)  # задаём шрифт метке

        self.label = QLabel(self) # поле, отвечающее за вывод результатов
        self.label.setText('')   # значение поля по умолчанию
        self.label.resize(260, 95) # задаем размер виджета  ширину и высоту в пикселях
        self.label.move(10, 0)    # задаем координаты положения по умолчанию виджета на монитору
        self.font.setPointSize(28)  # размер шрифта
        self.label.setFont(self.font)  # задаём шрифт метке

        self.label_M = QLabel(self) # заголовок поля памяти
        self.label_M.setText('M:')   # значение поля по умолчанию
        self.label_M.resize(225, 95) # задаем размер виджета  ширину и высоту в пикселях
        self.label_M.move(10, 35)    # задаем координаты положения по умолчанию виджета на монитору
        self.font.setPointSize(10)  # размер шрифта
        self.label_M.setFont(self.font)  # задаём шрифт метке

        self.label_m = QLabel(self) # поле, отвечающее за вывод результатов
        self.label_m.setText('0.0')
        self.label_m.resize(225, 95) # задаем размер виджета  ширину и высоту в пикселях
        self.label_m.move(25, 35)    # задаем координаты положения по умолчанию виджета на монитору
        self.label_m.setFont(self.font)  # задаём шрифт метке

# Создаем кнопки нашего будущего калькулятора
        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(5, 95)
        # self.num_1.clicked.connect() # В качестве параметра в будущем здесь будем указывать функцию,
        # которая будет работать на клике по кнопке
        self.font.setPointSize(22)  # размер шрифта
        self.num_7.setFont(self.font)  # задаём шрифт метке


        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(60, 95)
        self.num_8.setFont(self.font)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(115, 95)
        self.num_9.setFont(self.font)

        self.rem_div = QPushButton("'%", self)
        self.rem_div.resize(50, 50)
        self.rem_div.move(170, 95)
        self.rem_div.setFont(self.font)
        self.rem_div.setToolTip('Остаток от деления')  # всплывающая подсказка

        self.int_div = QPushButton('//', self)
        self.int_div.resize(50, 50)
        self.int_div.move(225, 95)
        self.int_div.setFont(self.font)
        self.int_div.setToolTip('Получение целой части от деления')  # всплывающая подсказка

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(5, 150)
        self.num_4.setFont(self.font)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(60, 150)
        self.num_5.setFont(self.font)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(115, 150)
        self.num_6.setFont(self.font)

        self.mul = QPushButton('*', self)
        self.mul.resize(50, 50)
        self.mul.move(170, 150)
        self.mul.setFont(self.font)

        self.div = QPushButton('÷', self)
        self.div.resize(50, 50)
        self.div.move(225, 150)
        self.div.setFont(self.font)

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(50, 50)
        self.num_1.move(5, 205)
        self.num_1.setFont(self.font)

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(60, 205)
        self.num_2.setFont(self.font)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(115, 205)
        self.num_3.setFont(self.font)

        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(170, 205)
        self.plus.setFont(self.font)

        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(225, 205)
        self.minus.setFont(self.font)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(5, 260)
        self.num_0.setFont(self.font)

        self.point = QPushButton('.', self)
        self.point.resize(50, 50)
        self.point.move(60, 260)
        self.point.setFont(self.font)
        self.point.setToolTip('вещественное число')  # всплывающая подсказка

        self.step = QPushButton('^', self)
        self.step.resize(50, 50)
        self.step.move(115, 260)
        self.step.setFont(self.font)
        self.step.setToolTip('Возведение в n степень')  # всплывающая подсказка

        self.sqrt = QPushButton('√', self)
        self.sqrt.resize(50, 50)
        self.sqrt.move(170, 260)
        self.sqrt.setFont(self.font)
        self.sqrt.setToolTip('Корень n степени')  # всплывающая подсказка

        self.ravn = QPushButton('=', self)
        self.ravn.resize(50, 105)
        self.ravn.move(225, 260)
        self.ravn.setFont(self.font)

        self.c = QPushButton('C', self)
        self.c.resize(50, 50)
        self.c.move(5, 315)
        self.c.setFont(self.font)

        self.m = QPushButton('M', self)
        self.m.resize(50, 50)
        self.m.move(60, 315)
        self.m.setFont(self.font)

        self.m_plus = QPushButton('M+', self)
        self.m_plus.resize(50, 50)
        self.m_plus.move(115, 315)
        self.m_plus.setFont(self.font)

        self.m_minus = QPushButton('M-', self)
        self.m_minus.resize(50, 50)
        self.m_minus.move(170, 315)
        self.m_minus.setFont(self.font)

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.point.clicked.connect(self.point_)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.mul.clicked.connect(self.mul_1)
        self.div.clicked.connect(self.div_1)
        self.step.clicked.connect(self.step_1)
        self.sqrt.clicked.connect(self.sqrt_1)
        self.rem_div.clicked.connect(self.rem_div_1)
        self.int_div.clicked.connect(self.int_div_1)
        self.m.clicked.connect(self.m_1)
        # self.m.doubleClicked.connect(self.m_2)
        self.m_plus.clicked.connect(self.m_plus_1)
        self.m_minus.clicked.connect(self.m_minus_1)


        self.ravn.clicked.connect(self.ravno)
        self.c.clicked.connect(self.clean) # очищение .label

    def enterValue(self):  # функция отвечающая за ввод данных (кнопки). Слушает событие нажатия кнопок
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def point_(self):
        self.my_input = '.'
        self.enterValue()

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label_story.setText(f'{self.operand_1} +')
        self.label.setText('')

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label_story.setText(f'{self.operand_1} -')
        self.label.setText('')

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label_story.setText(f'{self.operand_1} *')
        self.label.setText('')

    def div_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label_story.setText(f'{self.operand_1} /')
        self.label.setText('')

    def step_1(self):
        self.operation = '^'
        self.operand_1 = float(self.label.text())
        self.label_story.setText(f'{self.operand_1} ^')
        self.label.setText('')

    def sqrt_1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label_story.setText(f'√{self.operand_1} (n=?)')
        self.label.setText('')

    def rem_div_1(self):
        self.operation = "'%"
        self.operand_1 = float(self.label.text())
        self.label_story.setText(f'{self.operand_1} %')
        self.label.setText('')

    def int_div_1(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label_story.setText(f'{self.operand_1} //')
        self.label.setText('')

    def m_1(self):
        self.label.setText(str(self.m))

    def m_2(self):
        self.label.setText(str(self.m))
        self.m = 0.0
        self.label_m.setText(str(self.m))

    def m_plus_1(self):
        self.m = self.m + float(self.label.text())
        self.label_m.setText(str(self.m))

    def m_minus_1(self):
        self.m = self.m - float(self.label.text())
        self.label_m.setText(str(self.m))


    def ravno(self):
        self.operand_2 = float(self.label.text())
        if self.operation == '+':
            self.rezult = self.operand_1 + self.operand_2
        elif self.operation == '-':
            self.rezult = self.operand_1 - self.operand_2
        elif self.operation == '*':
            self.rezult = self.operand_1 * self.operand_2
        elif self.operation == '/':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 / self.operand_2
        elif self.operation == '^':
            self.rezult = self.operand_1 ** self.operand_2

        elif self.operation == '√':
            self.rezult = self.operand_1 ** (1 / self.operand_2)

        elif self.operation == "'%":
            self.rezult = self.operand_1 % self.operand_2

        elif self.operation == '//':
            self.rezult = self.operand_1 // self.operand_2

        self.rezult =round(self.rezult,10)

        self.label_story.setText('')
        self.label.setText(str(self.rezult))

    def clean(self):
        self.label.setText('')
        self.m = 0.0
        self.label_m.setText(str(self.m))

if __name__ == '__main__':
    app = QApplication(sys.argv) # создаем объект(экземпляр) класса QApplication()
    # окно виджета создается с помощью QApplication, мы вызываем его и передаем аргументы
    # командной строки
    # в случае запуска файла с кодом из командной строки
    ex = Calculator() # создаем объект класса Calculator()
    ex.show() # вызываем метод .show()  класса Calculator() для отображения картинки на мониторе
    sys.exit(app.exec()) # функция завершает работу приложения, если были какието ошибки, то сообщает о них