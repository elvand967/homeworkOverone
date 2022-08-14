# Домашнее задание Задача №14
# Есть словарь песен группы Depeche Mode
# violator
# songsdict = {
# 'World in My Eyes': 4.76,
# 'Sweetest Perfection': 5.43,
# 'Personal Jesus': 4.56,
# 'Halo': 4.30,
# 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.6,
# 'Policy of Truth': 4.88,
# 'Blue Dress': 4.18,
# 'Clean': 5.68,}
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, в название которых состоит из одного слова

songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
lst_key = []
all_time = 0
new_songsdict = {}
for key, value in songsdict.items():
    all_time += value
    if value > 5:
        lst_key.append(key + ': ' + str(value))
    if key.find(' ')== -1:
        new_songsdict[key] = value
print(f'время звучания всех песен диска группы Depeche Mode: {all_time}\n'
      f'песни, время звучаниях которых больше 5 минут: {lst_key}\n'
      f'песyb, в название которых состоит из одного слова: {new_songsdict}')
