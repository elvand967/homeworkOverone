# 5655341772:AAEFesP0r7MXMqPPyXYvbeCjtzZQQVnnx2A

import telebot  # импортируем библиотеку
from telebot import types

token = '5655341772:AAEFesP0r7MXMqPPyXYvbeCjtzZQQVnnx2A'
bot = telebot.TeleBot(token)  # подключаем токен бота
first_name = ''
name = ''
surname = ''
age = 0
profession = ''

keyboard_whats_next = types.InlineKeyboardMarkup(row_width=2)  # наша клавиатура «Что дальше»
# добавляем кнопки в клавиатуру
About_myself = types.InlineKeyboardButton(text="О себе", callback_data='About_myself')
Homework = types.InlineKeyboardButton(text="Домашнее задание", callback_data='Homework')
keyboard_whats_next.add(About_myself, Homework)

keyboard_yes_no = types.InlineKeyboardMarkup(row_width=2)  # наша клавиатура «Да»-«Нет»
# добавляем кнопки в клавиатуру
key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
keyboard_yes_no.add(key_yes, key_no)

keyboard_Homework = types.InlineKeyboardMarkup()  # наша клавиатура «Домашнее задание»
# keyboard_Homework = types.InlineKeyboardMarkup()  # наша клавиатура «Домашнее задание»
key_drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='drink')  # кнопка «Хочу пить»
key_eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='eat')
key_walk_btn = types.InlineKeyboardButton(text="Хочу гулять", callback_data='walk')
key_sleep_btn = types.InlineKeyboardButton(text="Хочу спать", callback_data='sleep')
key_joke_btn = types.InlineKeyboardButton(text="Хочу шутку", callback_data='joke')
keyboard_Homework.add(key_drink_btn, key_eat_btn, key_walk_btn, key_sleep_btn, key_joke_btn)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # global keyboard_bot
    try:
        if call.message:
            if call.data == 'About_myself':  # call.data это callback_data, которую мы указали при объявлении кнопки....
                # keyboard_bot = 'About_myself'
                bot.send_message(call.message.chat.id, 'Как тебя зовут?')

            if call.data == 'Homework':
                global name
                global surname
                global age
                global profession
                txt = ''
                if name == '' or surname == '' or age == 0 or profession == '':
                    txt += 'Жаль, что я так мало узнал о тебе.  : ('
                txt += "\n\nПросмотр домашнего задания:"
                bot.send_message(call.message.chat.id, txt, reply_markup=keyboard_Homework)

            if call.data == "yes":
                # код сохранения данных, или их обработки
                bot.send_message(call.message.chat.id,
                                 'Запомню : )\n\nТеперь можно посмотреть домашнее задание:',
                                 reply_markup=keyboard_Homework)

            if call.data == "no":
                # код сохранения данных, или их обработки
                # переспрашиваем ??????
                bot.send_message(call.message.chat.id,
                                 f'Запишем, что так сказал {first_name}   : (\n\nПосмотрим домашнее задание',
                                 reply_markup=keyboard_Homework)

            if call.data == 'drink':
                img = open('water.jpg', 'rb')
                bot.send_photo(
                    chat_id=call.message.chat.id,
                    photo=img,
                    caption="Картинка воды",
                    reply_markup=keyboard_Homework)
                img.close()
            if call.data == 'eat':
                img = open('vegetables.jpg', 'rb')
                bot.send_photo(
                    chat_id=call.message.chat.id,
                    photo=img,
                    caption="Картинка еда",
                    reply_markup=keyboard_Homework)
                img.close()
            if call.data == 'walk':
                img = open('walk.jpg', 'rb')
                bot.send_photo(
                    chat_id=call.message.chat.id,
                    photo=img,
                    caption="Картинка гулять",
                    reply_markup=keyboard_Homework)
                img.close()
            if call.data == 'sleep':
                img = open('sleep.jpg', 'rb')
                bot.send_photo(
                    chat_id=call.message.chat.id,
                    photo=img,
                    caption="Картинка спать",
                    reply_markup=keyboard_Homework)
                img.close()
            if call.data == 'joke':
                img = open('joke.jpg', 'rb')
                bot.send_photo(
                    chat_id=call.message.chat.id,
                    photo=img,
                    caption="Картинка шутка",
                    reply_markup=keyboard_Homework)
                img.close()

    except Exception as e:
        print(repr(e))
    return


# объявляем метод для получения текстовых сообщений
@bot.message_handler(content_types=['text'])
def start(message):
    global first_name
    first_name = message.chat.first_name
    if message.text == 'Привет':
        bot.send_message(message.from_user.id,
                         f"Привет {first_name}!\n"
                         f"Расскажешь о себе (Кто ты, как ты?)\n"
                         f"или сразу будем смотреть домашнее задание?",
                         reply_markup=keyboard_whats_next)
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши "Привет"')


def get_name(message):  # получаем имя
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):  # получаем фамилию
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

    if age >= 18:
        bot.send_message(message.from_user.id, 'Какая у тебя профессия?')
    else:
        bot.send_message(message.from_user.id, 'Где ты учишься?')
    bot.register_next_step_handler(message, get_profession)


def get_profession(message):
    global profession
    if age < 18:
        profession = 'учащийся '
    profession += message.text
    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ', ты ' + profession + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard_yes_no)


if __name__ == "__main__":
    bot.polling(none_stop=True)
