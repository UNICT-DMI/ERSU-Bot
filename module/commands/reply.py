"""/reply command"""
import re
from telegram import Update
from telegram.ext import CallbackContext
from module.data.constants import CHAT_ID_REGEX

def reply(update: Update, context: CallbackContext) -> None:
    """Called by the /reply command.
    Use: to a report message reply -> /reply <word> ...
    Allows the administrators to respond to users who have reported something
    Args:
        update: update event
        context: context passed by the handler
    """

    chat_id = update.message.chat_id
    admin_reply_message = update.message.text

    if update.message.reply_to_message.text is None:
        context.bot.sendMessage(
                chat_id=chat_id, text="Non puoi rispondere a questo tipo di messaggio!")
        return

    groups = re.search(CHAT_ID_REGEX, update.message.reply_to_message.text)
    if groups is None:
        return

    reply_chat_id = groups.group(2)
    if context.args:
        context.bot.sendMessage(
            chat_id=reply_chat_id,
            text=f"Messaggio dal rappresentante:\n{admin_reply_message[7:]}",
        )
    else:
        context.bot.sendMessage(
            chat_id=reply_chat_id,
            text=f"Messaggio dal rappresentante:\n{admin_reply_message}",
        )

    context.bot.sendMessage(chat_id=chat_id, text="Risposta inoltrata con successo!")
