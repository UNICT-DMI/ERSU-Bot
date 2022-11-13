""" /menu command """
from module.data.constants import DB_PATH
from module.data.user_settings import UserSettings
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, ContextTypes

def menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Imposta quando ricevere il menù con /menu_settings")
    return

def menu_settings(update: Update, context: CallbackContext) -> None:
    menu_set = UserSettings()

#    keyboard = [
#        GIORNI_PRANZO_CENA,
#        [
#            InlineKeyboardButton("Lunedì", callback_data="0"),
#            InlineKeyboardButton("❌", callback_data="1"),
#            InlineKeyboardButton("❌", callback_data="2")
#        ],
#        [
#            InlineKeyboardButton("Martedì", callback_data="0"),
#            InlineKeyboardButton("❌", callback_data="3"),
#            InlineKeyboardButton("❌", callback_data="4")
#        ],
#        [
#            InlineKeyboardButton("Mercoledì", callback_data="0"),
#            InlineKeyboardButton("❌", callback_data="5"),
#            InlineKeyboardButton("❌", callback_data="6")
#        ],
#        [
#            InlineKeyboardButton("Giovedì", callback_data="0"),
#            InlineKeyboardButton("❌", callback_data="7"),
#            InlineKeyboardButton("❌", callback_data="8")
#        ],
#        [
#            InlineKeyboardButton("Venerdì", callback_data="0"),
#            InlineKeyboardButton("❌", callback_data="9"),
#            InlineKeyboardButton("❌", callback_data="10")
#        ],
#        [
#            InlineKeyboardButton("Sabato", callback_data="0"),
#            InlineKeyboardButton("❌", callback_data="11"),
#            InlineKeyboardButton("❌", callback_data="12")
#        ],
#        [
#            InlineKeyboardButton("Domenica", callback_data="0"),
#            InlineKeyboardButton("❌", callback_data="13"),
#            InlineKeyboardButton("❌", callback_data="14")
#        ],
#    ]
#    
#
#    reply_markup = InlineKeyboardMarkup(keyboard)
#
#    update.message.reply_text("Imposta quando ricevere il menù:", reply_markup=reply_markup)