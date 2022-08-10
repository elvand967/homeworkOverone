# Домашнее задание Задача №12/3
# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
# (Пример HjkLM- 1 пара нижнего, 1 пара верхнего),
# а также сколько всего букв в слове, сколько гласных и согласных.
import random
word = ''
wordList = []
capitalPairsList = []
pairsLowercaseList = []
while True:
    request = input('Введите требуемое для иследования слово или\nцифрами число букв, для его генерации: ')
    if request.isdigit(): # запрос из цифр?
        alphabet_en = []
        for i in range(65, 91):  # Значение ASCII A-Z лежит в диапазоне 65-90,
            alphabet_en.append(chr(i))
        for i in range(97, 123):  # а для a-z это значение находится в диапазоне 97 – 122.
            alphabet_en.append(chr(i))
        random.shuffle(alphabet_en)  # перемешаем список строчных и заглавных букв
        request = int(request)
        wordList = random.choices(alphabet_en, k=request) # генерация случайных значений из списка 'k' раз
        word = "".join(wordList)
        print(f'Иследуемое слово: "{word}"')
    else:
        # wordList = request.split() # строку в список строк
        wordList = list(request)
        word = request
    capitalPairsList.clear()   # очистим списки для повторного теста
    pairsLowercaseList.clear()
    capitalPairs = 0    # количество заглавных пар
    pairsLowercase = 0  # количество строчных пар
    notLetter = 0       # не буквы (кол-во)
    flagP = False # флаг заглавных букв
    flagL = False # флаг строчных букв
    ind = 0
    for i in wordList:
        if i.isupper():
            flagL = False
            if flagP:
                capitalPairs += 1
                capitalPairsList.append(wordList[ind-1]+wordList[ind])
                flagP = False
            else: flagP = True
        elif i.islower():
            flagP = False
            if flagL:
                pairsLowercase += 1
                pairsLowercaseList.append(wordList[ind-1]+wordList[ind])
                flagL = False
            else: flagL = True
        else:
            flagP = False
            flagL = False
            notLetter += 1
        ind +=1
    print(f'{capitalPairs } заглавных пары: {capitalPairsList}\n'
          f'{pairsLowercase } строчных пары: {pairsLowercaseList}')
    x = len(word)-notLetter
    print(f'В слове {x} букв')
    request = input('-------------\nПовторить тест? (Y/N): ')
    if request.upper() == 'Y':
        continue
    else: break
print('Программа завершила работу')
