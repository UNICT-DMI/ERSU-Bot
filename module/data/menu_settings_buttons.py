from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, ContextTypes
from module.data.user_settings import UserSettings

from module.data.constants import CROSS, CHECK

def generate_keyboard(settings: list) -> list:
    keyboard = [
        [
            InlineKeyboardButton("Giorni", callback_data = "0"),
            InlineKeyboardButton("Pranzo", callback_data = "0"),
            InlineKeyboardButton("Cena", callback_data = "0")
        ],

        [
            InlineKeyboardButton("Lunedì", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[1] == 0 else CHECK, callback_data = "monday_lunch"),
            InlineKeyboardButton(CROSS if settings[2] == 0 else CHECK, callback_data = "monday_dinner")
        ],

        [
            InlineKeyboardButton("Martedì", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[3] == 0 else CHECK, callback_data = "tuesday_lunch"),
            InlineKeyboardButton(CROSS if settings[4] == 0 else CHECK, callback_data = "tuesday_dinner")
        ],

        [
            InlineKeyboardButton("Mercoledì", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[5] == 0 else CHECK, callback_data = "wednesday_lunch"),
            InlineKeyboardButton(CROSS if settings[6] == 0 else CHECK, callback_data = "wednesday_dinner")
        ],

        [
            InlineKeyboardButton("Giovedì", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[7] == 0 else CHECK, callback_data = "thursday_lunch"),
            InlineKeyboardButton(CROSS if settings[8] == 0 else CHECK, callback_data = "thursday_dinner")
        ],

        [
            InlineKeyboardButton("Venerdì", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[9] == 0 else CHECK, callback_data = "friday_lunch"),
            InlineKeyboardButton(CROSS if settings[10] == 0 else CHECK, callback_data = "friday_dinner")
        ],

        [
            InlineKeyboardButton("Sabato", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[11] == 0 else CHECK, callback_data = "saturday_lunch"),
            InlineKeyboardButton(CROSS if settings[12] == 0 else CHECK, callback_data = "saturday_dinner")
        ],

        [
            InlineKeyboardButton("Domenica", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[13] == 0 else CHECK, callback_data = "sunday_lunch"),
            InlineKeyboardButton(CROSS if settings[14] == 0 else CHECK, callback_data = "sunday_dinner")
        ],

        [
            InlineKeyboardButton("Azzera", callback_data = "reset"),
            InlineKeyboardButton("Chiudi", callback_data = "close_settings")
        ]
    ]
    return keyboard

def set_meal_button(update: Update, context: CallbackContext) -> None:
    menu_set = UserSettings()
    query = update.callback_query

    day_menu = (update.callback_query.data).split("_")
    menu_set.set_meal(query.message.chat_id, day_menu[0], day_menu[1])
    settings = menu_set.get_user_settings(query.message.chat_id)

    keyboard = generate_keyboard(settings)
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_reply_markup(chat_id = query.message.chat_id,
                                    message_id = query.message.message_id,
                                    reply_markup = reply_markup)

def reset_button(update: Update, context: CallbackContext) -> None:
    menu_set = UserSettings()
    query = update.callback_query

    menu_set.reset_user_settings(query.message.chat_id)
    settings = menu_set.get_user_settings(query.message.chat_id)

    keyboard = generate_keyboard(settings)
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_reply_markup(chat_id = query.message.chat_id,
                                    message_id = query.message.message_id,
                                    reply_markup = reply_markup)

def close_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    context.bot.deleteMessage(chat_id = query.message.chat_id,
                                    message_id = query.message.message_id)