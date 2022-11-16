"""/report command"""
from module.shared import config_map
from telegram import Update, Chat
from telegram.ext import CallbackContext


def report(update: Update, context: CallbackContext) -> None:
    """Called by the /report command.
        Use: /report <word> ...
        Allows the user to report something to the administrators
        Args:
            update: update event
            context: context passed by the handler
    """
    chat_id = update.message.chat_id
    chat_user = update.message.from_user

    if update.message.chat.type != Chat.PRIVATE:
        context.bot.sendMessage(chat_id=chat_id, text="Errore! Utilizza il comando in chat privata!")
    elif not chat_user.username:
        context.bot.sendMessage(chat_id=chat_id, text="Errore! Imposta un username!")
    else:
        if context.args:
            message = "⚠_Report_⚠\n" f"chat_id: {chat_id}\nUsername: @{chat_user.username}\n"

            if chat_user.first_name is not None:
                message += f"Nome: {chat_user.first_name}\n"
            if chat_user.last_name is not None:
                message += f"Cognome: {chat_user.last_name}\n"

            message += f"Segnalazione: {' '.join(context.args)}\n"

            context.bot.sendMessage(chat_id=config_map["admin_group"], text=message)
            context.bot.sendMessage(chat_id=chat_id, text="Segnalazione inviata!")
        else:
            context.bot.sendMessage(
                chat_id=chat_id,
                text="Errore. Invia un report con /report <messaggio>",
            )
