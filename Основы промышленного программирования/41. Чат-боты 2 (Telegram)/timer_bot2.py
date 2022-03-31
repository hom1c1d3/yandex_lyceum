import os

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler

TOKEN = os.getenv("TOKEN")

reply_keyboard = [["/address", "/phone"],
                  ["/site", "/work_time"],
                  ["/set_timer 1", "/set_timer 5", "/set_timer 10"],
                  ["/close"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def remove_job_if_exists(name, context):
    """Удаляем задачу по имени.
    Возвращаем True если задача была успешно удалена."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


# Обычный обработчик, как и те, которыми мы пользовались раньше.
def set_timer(update, context):
    """Добавляем задачу в очередь"""
    chat_id = update.message.chat_id
    try:
        # args[0] должен содержать значение аргумента
        # (секунды таймера)
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text('Извините, не умеем возвращаться в прошлое')
            return

        # Добавляем задачу в очередь
        # и останавливаем предыдущую (если она была)
        job_removed = remove_job_if_exists(str(chat_id), context)
        context.job_queue.run_once(task, due, context=chat_id, name=str(chat_id))

        text = f'Вернусь через {due} секунд!'
        if job_removed:
            text += ' Старая задача удалена.'
        update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set <секунд>')


# Обратите внимание: сообщение мы отправляем, используя объект bot
# внутри контекста, а не updater. Это обращение к базовому API.
def task(context):
    """Выводит сообщение"""
    job = context.job
    context.bot.send_message(job.context, text='КУКУ!')


# Задачу из очереди можно отменить. Добавим для этого специальную команду:
def unset(update, context):
    """Удаляет задачу, если пользователь передумал"""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Таймер отменен!' if job_removed else 'У вас нет активных таймеров'
    update.message.reply_text(text)


def close_keyboard(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Клавиатура закрыта",
                             reply_markup=ReplyKeyboardRemove())


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


# Регистрируем обработчики. Обратите внимание на параметры
# pass_job_queue и pass_chat_data.
# По умолчанию они равны False и соответствующие параметры не передаются в обработчики.
# Сейчас же они нам нужны, мы явно задаем их значения и прописываем
# соответствующие параметры в прототипы обработчиков.
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
    dp.add_handler(CommandHandler("close", close_keyboard))

    dp.add_handler(CommandHandler("set_timer", set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset,
                                  pass_chat_data=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
