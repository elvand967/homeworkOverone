# Задача№11-1
# Создайте кортеж с цифрами от 0 до 9 и посчитайте сумму

MyTuple = tuple(i for i in range(10))
print(f'Искомый кортеж: {MyTuple}')
print(f'Сумма чисел в кортежe: {sum(MyTuple)}')