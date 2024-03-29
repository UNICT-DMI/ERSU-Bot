"""/start command"""
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from module.data import START_CMD_TEXT, CONTACT_ERSU, HELP, REPORT, FAQ # MENU_MENSA, MENU_SETTINGS,

keyboard = [
    # [MENU_MENSA, MENU_SETTINGS],
    [CONTACT_ERSU, HELP],
    [REPORT, FAQ]
]


def start(update: Update, context: CallbackContext) -> None:
    """Called by the /start command.
    Sends a welcome message

    Args:
        update: update event
        context: context passed by the handler
    """

    reply_keyboard = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.sendMessage(
        chat_id=update.message.chat_id, text=START_CMD_TEXT, reply_markup=reply_keyboard
    )
