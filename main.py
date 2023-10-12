from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from menu import (
    main_menu_keyboard,
    courses_menu_keyboard
)
from key_buttons import tele_button, courses


ABOUT = tele_button[0]
COURSES = tele_button[1]
BACK = courses[4]
LOCATION = courses[2]


def start(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Добро пожаловать {update.effective_user.username}\nэтот бот поможет вам с информацией о курсах',
        reply_markup=main_menu_keyboard()
    )
    
def about(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Преимущества обучения в Codify · Обучение с нуля до Junior. Пройди обучение по авторской программе Codify и стань Junior специалистом.\nsite:\nhttps://www.codifylab.com/'
    )
    
def reply_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Choose course',
        reply_markup=courses_menu_keyboard()
    )
def main_menu(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Main menu',
        reply_markup=main_menu_keyboard()
    )

def location(update:Update, context:CallbackContext):
    msg = context.bot
    

updater = Updater(token=TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSES),
    reply_courses
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(back),
    main_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(location),
    
))


updater.start_polling()
updater.idle()