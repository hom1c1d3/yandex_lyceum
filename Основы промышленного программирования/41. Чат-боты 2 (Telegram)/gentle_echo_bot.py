import os

from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters


TOKEN = os.getenv("TOKEN")


def echo(update: Update, context: CallbackContext):
    message = f'Я получил сообщение: "{update.message.text}"'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dp.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()