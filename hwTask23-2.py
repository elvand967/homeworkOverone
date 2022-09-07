# Домашнее задание Задача №23-2
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.
def is_prime (n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        limit = n**(1/2)
        i = 2
        while i <= limit:
            if n % i == 0:
                return False
            i += 1
        return True

print(f'Утверждение, что введенное число "Простое"\n'
      f'(большее 1 , и оно ни на что не делится, кроме себя и 1):  '
      f'{is_prime(int(input("Введите любое целое число  от 0 до 1000: ")))}')
