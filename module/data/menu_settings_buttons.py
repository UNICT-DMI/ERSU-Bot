"""All keyboard utils for /menu_settings command"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext
from .user_settings import UserSettings
from .constants import SYMBOLS, EMPTY, USER_EMPTY_SETTINGS, VALID_DAYS, DAYS_TRANSLATION


def generate_keyboard(settings: list[int]) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Giorni", callback_data=EMPTY),
            InlineKeyboardButton("Pranzo", callback_data=EMPTY),
            InlineKeyboardButton("Cena", callback_data=EMPTY),
        ],
        *[
            [
                InlineKeyboardButton(DAYS_TRANSLATION[day], callback_data=EMPTY),
                InlineKeyboardButton(SYMBOLS[settings[2 * i]], callback_data=f"{day}_lunch"),
                InlineKeyboardButton(SYMBOLS[settings[2 * i + 1]], callback_data=f"{day}_dinner"),
            ]
            for i, day in enumerate(VALID_DAYS)
        ],
        [
            InlineKeyboardButton("Azzera", callback_data="reset"),
            InlineKeyboardButton("Chiudi", callback_data="close_settings"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def set_meal_button(update: Update, context: CallbackContext) -> None:
    menu_set = UserSettings()
    query = update.callback_query
    context.bot.answer_callback_query(callback_query_id=query.id)

    day, meal = (update.callback_query.data).split("_")
    menu_set.set_meal(query.message.chat_id, day, meal)  # type: ignore
    settings = menu_set.get_user_settings(query.message.chat_id)

    if not any(value > 0 for value in settings):
        menu_set.delete_user(query.message.chat_id)

    keyboard = generate_keyboard(settings)
    context.bot.edit_message_reply_markup(
        chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=keyboard
    )


def reset_button(update: Update, context: CallbackContext) -> None:
    menu_set = UserSettings()
    query = update.callback_query
    context.bot.answer_callback_query(callback_query_id=query.id)

    menu_set.delete_user(query.message.chat_id)

    keyboard = generate_keyboard(USER_EMPTY_SETTINGS)
    context.bot.edit_message_reply_markup(
        chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=keyboard
    )


def close_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    context.bot.answer_callback_query(callback_query_id=query.id)

    context.bot.deleteMessage(chat_id=query.message.chat_id, message_id=query.message.message_id)
