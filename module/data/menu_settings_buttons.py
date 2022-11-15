from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, ContextTypes
from module.data.user_settings import UserSettings

from module.data.constants import SYMBOLS, EMPTY

def generate_keyboard(settings: list) -> list:
    keyboard = [
        [
            InlineKeyboardButton("Giorni", callback_data = EMPTY),
            InlineKeyboardButton("Pranzo", callback_data = EMPTY),
            InlineKeyboardButton("Cena", callback_data = EMPTY)
        ],

        [
            InlineKeyboardButton("Lunedì", callback_data = EMPTY),
            InlineKeyboardButton(SYMBOLS[settings[0]], callback_data = "monday_lunch"),
            InlineKeyboardButton(SYMBOLS[settings[1]], callback_data = "monday_dinner")
        ],

        [
            InlineKeyboardButton("Martedì", callback_data = EMPTY),
            InlineKeyboardButton(SYMBOLS[settings[2]], callback_data = "tuesday_lunch"),
            InlineKeyboardButton(SYMBOLS[settings[3]], callback_data = "tuesday_dinner")
        ],

        [
            InlineKeyboardButton("Mercoledì", callback_data = EMPTY),
            InlineKeyboardButton(SYMBOLS[settings[4]], callback_data = "wednesday_lunch"),
            InlineKeyboardButton(SYMBOLS[settings[5]], callback_data = "wednesday_dinner")
        ],

        [
            InlineKeyboardButton("Giovedì", callback_data = EMPTY),
            InlineKeyboardButton(SYMBOLS[settings[6]], callback_data = "thursday_lunch"),
            InlineKeyboardButton(SYMBOLS[settings[7]], callback_data = "thursday_dinner")
        ],

        [
            InlineKeyboardButton("Venerdì", callback_data = EMPTY),
            InlineKeyboardButton(SYMBOLS[settings[8]], callback_data = "friday_lunch"),
            InlineKeyboardButton(SYMBOLS[settings[9]], callback_data = "friday_dinner")
        ],

        [
            InlineKeyboardButton("Sabato", callback_data = EMPTY),
            InlineKeyboardButton(SYMBOLS[settings[10]], callback_data = "saturday_lunch"),
            InlineKeyboardButton(SYMBOLS[settings[11]], callback_data = "saturday_dinner")
        ],

        [
            InlineKeyboardButton("Domenica", callback_data = EMPTY),
            InlineKeyboardButton(SYMBOLS[settings[12]], callback_data = "sunday_lunch"),
            InlineKeyboardButton(SYMBOLS[settings[13]], callback_data = "sunday_dinner")
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