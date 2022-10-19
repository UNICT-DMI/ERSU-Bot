# start command

from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    """Called by the /start command.
    Sends a welcome message

    Args:
        update: update event
        context: context passed by the handler
    """
    context.bot.sendMessage(chat_id=update.message.chat_id, text=
        """Benvenuto! Questo bot è stato realizzato dagli studenti del Corso di Laurea in Informatica al fine di fornire uno strumento di supporto per chi usufruisce dei servizi ERSU. Per scoprire cosa puoi fare usa /help""")