# Домашнее задание. Задача №6/3
# Представь, что мы пишем программу для банковских карточек.
# Человек может совершать покупки, пока у него на карте хватает на это денег.
# В начале программы вводим количество денег, а потом вводим расходы, пока они не превышают баланс на карте.
# Когда превысили, мы должны получить, сколько успели сделать покупок и сколько осталось денег на карте.

cashDeposit = 0
def deposit():
    return print(f'В настоящий момент на депозите {cashDeposit} BYN')

if cashDeposit == 0:
    deposit()
    cashDeposit = float(input('Пополнить депозит на сумму: '))
deposit()