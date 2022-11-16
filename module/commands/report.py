# pylint: skip-file
"""/report command"""

from telegram import Update, User
from telegram.ext import CallbackContext

def report(update: Update, context: CallbackContext) -> None:
    """Called by the /report command.
    Use: /report <word> ...
    Allows the user to report something to the administrators
    Args:
        update: update event
        context: context passed by the handler
    """
    #getting chat_id and User object of the sender
    chat_id = update.message.chat_id
    chat_user = update.message.from_user

    if not chat_user.username:
        context.bot.sendMessage(chat_id=chat_id, text = "")
    else:
        if context.args:
            message = "⚠ Report ⚠\n"\
                        f"Username: @{chat_user.username}\n"
#
#            if chat_user.first_name is not None:
#                message += f"Nome/Name: {chat_user.first_name}\n"
#            if chat_user.last_name is not None:
#                message += f"Cognome/Surname: {chat_user.last_name}\n"
#
#            message += f"Segnalazione/Content: {' '.join(context.args)}\n"
#
#            context.bot.sendMessage(chat_id=config_map['representatives_group'], text=message)
#            context.bot.sendMessage(chat_id=chat_id,
#                                    text=get_locale(locale, TEXT_IDS.REPORT_RESPONSE_TEXT_ID).replace(PLACE_HOLDER, message))
#        else:
#            context.bot.sendMessage(chat_id=chat_id,
#                                    text=get_locale(locale, TEXT_IDS.REPORT_WARNING_TEXT_ID))
