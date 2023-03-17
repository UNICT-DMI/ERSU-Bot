"""/reply command"""
import re
from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from module.data.constants import CHAT_ID_REGEX, ANSWER_TO_REPORT_TEXT


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

    # Reply must be to a bot's message
    if update.message.reply_to_message.from_user.id != context.bot.id:
        return

    # Message must contain text
    if update.message.reply_to_message.text is None:
        context.bot.sendMessage(
            chat_id=chat_id, text="Non puoi rispondere a questo tipo di messaggio!"
        )
        return

    groups = re.search(CHAT_ID_REGEX, update.message.reply_to_message.text)
    # Message must contain an id in the message (the second group is the chat_id)
    if groups is None:
        return

    reply_chat_id = groups.group(2)
    if update.message.text.startswith("/reply"):
        if context.args:
            context.bot.sendMessage(
                chat_id=reply_chat_id,
                text=f"Messaggio dal rappresentante:\n{admin_reply_message[7:]}\n\n{ANSWER_TO_REPORT_TEXT}",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
        else:
            context.bot.sendMessage(chat_id=chat_id, text="Per rispondere ad un messaggio utilizza /reply <messaggio>.")
            return
    else:
        context.bot.sendMessage(
            chat_id=reply_chat_id,
            text=f"Messaggio dal rappresentante:\n{admin_reply_message}\n\n{ANSWER_TO_REPORT_TEXT}",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )

    context.bot.sendMessage(chat_id=chat_id, text="Risposta inoltrata con successo!")
