#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Домашнее задание. Задача №38-1 (two tables)
# Дополните код предыдущего модуля. Добавьте кнопки %, // и возведение в квадрат.


# Делаем необходимые импорты. Основные виджеты расположены в PyQt5.QtWidgets.
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import sys

# создаем класс Calculator, который наследует класс QWidget из библиотеки PyQt5
class Calculator(QWidget):
    def __init__(self):
        super().__init__() # подключаем весь инициализатор родительского класса QWidget
        self.initUI() # метод, которому дилигируется создание UI (создание картинки, окна программы, кнопки и т.д.)
        self.my_input = [] # объявим списки фунционалов (пустой массив)
        self.operand_1 = []# объявим -/-
        self.operand_2 = []# объявим -/-

    def initUI(self):
        self.setGeometry(300, 300, 225, 370)
        self.setWindowTitle("Калькулятор") # Устанавливаем название приложения, отражающееся в окне виджета
# Для работы с методами self.label в начале импортировали библиотеку QLabel
        self.label = QLabel(self) # поле, отвечающее за вывод результатов
        self.label.setText('0')   # значение поля по умолчанию
        self.label.resize(225, 95) # задаем размер виджета  ширину и высоту в пикселях
        self.move(300, 300)        # задаем координаты положения по умолчанию виджета на монитору
# Создаем кнопки нашего будущего калькулятора
        self.num_1 = QPushButton('1', self)
        self.num_1.resize(50, 50)
        self.num_1.move(5, 100)
        # self.num_1.clicked.connect() # В качестве параметра в будущем здесь будем указывать функцию,
        # которая будет работать на клике по кнопке

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(60, 100)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(115, 100)

        self.div = QPushButton('/', self)
        self.div.resize(50, 50)
        self.div.move(170, 100)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(5, 155)
        # self.num_1.clicked.connect()

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(60, 155)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(115, 155)

        self.mul = QPushButton('*', self)
        self.mul.resize(50, 50)
        self.mul.move(170, 155)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(5, 210)
        # self.num_1.clicked.connect()

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(60, 210)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(115, 210)

        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(170, 210)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(5, 265)
        # self.num_1.clicked.connect()

        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(60, 265)

        self.step = QPushButton('^', self)
        self.step.resize(50, 50)
        self.step.move(115, 265)

        self.sqrt = QPushButton('√', self)
        self.sqrt.resize(50, 50)
        self.sqrt.move(170, 265)

        self.ravn = QPushButton('=', self)
        self.ravn.resize(155, 50)
        self.ravn.move(5, 320)

        self.c = QPushButton('C', self)
        self.c.resize(50, 50)
        self.c.move(170, 320)

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
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.mul.clicked.connect(self.mul_1)
        self.div.clicked.connect(self.div_1)
        self.step.clicked.connect(self.step_1)
        self.sqrt.clicked.connect(self.sqrt_1)
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

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def step_1(self):
        self.operation = '^'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def sqrt_1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

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

        self.label.setText(str(self.rezult))

    def clean(self):
        self.label.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv) # создаем объект(экземпляр) класса QApplication()
    # окно виджета создается с помощью QApplication, мы вызываем его и передаем аргументы
    # командной строки
    # в случае запуска файла с кодом из командной строки
    ex = Calculator() # создаем объект класса Calculator()
    ex.show() # вызываем метод .show()  класса Calculator() для отображения картинки на мониторе
    sys.exit(app.exec()) # функция завершает работу приложения, если были какието ошибки, то сообщает о них