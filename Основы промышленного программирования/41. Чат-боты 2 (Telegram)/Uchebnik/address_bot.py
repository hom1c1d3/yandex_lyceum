import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler

TOKEN = os.getenv("TOKEN")

reply_keyboard = [["/address", "/phone"], ["/site", "/work_time"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="""Привет! это бот-спавочник. Что вы хотели узнать?""", reply_markup=markup)


def help_cmd(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Я бот-справочник.""")


def address(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Адрес: г. Москва Тихвинский пер. д. 3""")


def phone(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Телефон: +7(426)258-40-53""")


def site(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Сайт: https://yandex.ru/legal/lyceum""")


def work_time(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Понедельник: 18:00, четверг: 18:00""")


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_cmd))

    dp.add_handler(CommandHandler("address", address))
    dp.add_handler(CommandHandler("phone", phone))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("work_time", work_time))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
