# https://docs-python.ru/packages/biblioteka-python-telegram-bot-python/#create.bot
# Установка пакета python-telegram-bot в виртуальное окружение:
# # создаем виртуальное окружение, если нет
# $ python3 -m venv .telegram --prompt TelegramBot
# # активируем виртуальное окружение
# $ source .telegram/bin/activate
# # ставим модуль python-telegram-bot
# (TelegramBot):~$ python -m pip install -U python-telegram-bot
# # или установка чистого API без расширений
# (TelegramBot):~$ python -m pip install -U python-telegram-bot-raw



# sample-bot.py
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler

TOKEN = '5655341772:AAEFesP0r7MXMqPPyXYvbeCjtzZQQVnnx2A'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# функция обработки команды '/start'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")

# функция обработки текстовых сообщений
def echo(update, context):
    text = 'ECHO: ' + update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)

# функция обработки команды '/caps'
def caps(update, context):
    if context.args:
        text_caps = ' '.join(context.args).upper()
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text=text_caps)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text='No command argument')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text='send: /caps argument')

# функция обработки встроенного запроса
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Convert to UPPER TEXT',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command.")

# обработчик команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# обработчик текстовых сообщений
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# обработчик команды '/caps'
caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

# обработчик встроенных запросов
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

# обработчик не распознных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# запуск прослушивания сообщений
updater.start_polling()
# обработчик нажатия Ctrl+C
updater.idle()