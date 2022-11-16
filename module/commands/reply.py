"""/reply command"""
from module.shared import config_map
import re
from telegram import Update, Chat, Message
from telegram.ext import CallbackContext

def reply(update: Update, context: CallbackContext) -> None:
    """Called by the /reply command.
        Use: to a report message reply -> /reply <word> ...
        Allows the administrators to respond to users who have reported something
        Args:
            update: update event
            context: context passed by the handler
    """

    chat_id = update.message.chat_id
    reply_chat_id = (re.search(r'(chat_id: )([0-9]+)', update.message.reply_to_message.text)).group(2)

    if update.message.chat.type == Chat.PRIVATE:
        context.bot.sendMessage(chat_id=chat_id, text="Errore! Utilizza il comando in un gruppo!")
    elif chat_id != config_map["admin_group"]:
        context.bot.sendMessage(chat_id=chat_id, text="Errore! Solo gli amministratori possono rispondere ai messaggi!")
    else:
        if context.args:
            context.bot.sendMessage(chat_id=reply_chat_id, text="Messaggio dal rappresentante:")
            context.bot.sendMessage(chat_id=reply_chat_id, text=(' '.join(context.args)))
        else:
            context.bot.sendMessage(
                chat_id=chat_id,
                text="Errore. Invia una risposta rispondendo al messaggio con /reply <messaggio>",
            )
