import os

from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler

TOKEN = os.getenv("TOKEN")


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Привет! Я эхо-бот.
     Напиши мне что-нибудь - я отвечу тебе тем же.""")


def help_cmd(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Я пока не умею помогать. Это только твое эхо!""")


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_cmd))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
