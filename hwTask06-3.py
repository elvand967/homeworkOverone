# Домашнее задание. Задача №6/3
# Представь, что мы пишем программу для банковских карточек.
# Человек может совершать покупки, пока у него на карте хватает на это денег.
# В начале программы вводим количество денег, а потом вводим расходы, пока они не превышают баланс на карте.
# Когда превысили, мы должны получить, сколько успели сделать покупок и сколько осталось денег на карте.
import random
cashDeposit = 0
productList = []

def deposit():
    return print(f'В настоящий момент на депозите {cashDeposit} BYN')

if cashDeposit == 0:
    deposit()
    cashDeposit = float(input('Пополнить депозит на сумму: '))
print('Welcome to shopping!\n(Добро пожаловать за покупками!)')
deposit()
print('Наш ассортимент:')
for i in  range(0,10):
    x = random.uniform(5.0,100.99)
    x = float('{:.2f}'.format(x))
    productList.insert(i,x)
    print(f'товар № {i+1}, цена: {productList[i]} BYN')

shoppingList = list(map(int, input('\nВведите номера товаров (через пробел), для помещения их в карзину: ').split()))
# print(shoppingList)

for i in range(len(shoppingList)):
    if  cashDeposit >= productList[shoppingList[i]-1]:
        cashDeposit -= productList[shoppingList[i]-1]
        print(f'Приобретен товар № {shoppingList[i]} по цене:  {productList[shoppingList[i]-1]} BYN')
    else:
        print(f'Недостаточно средст для приобретения товара № {shoppingList[i]} по цене:  {productList[shoppingList[i]-1]} BYN')
print(f"\nОстаток средств на счету {float('{:.2f}'.format(cashDeposit))} BYN")