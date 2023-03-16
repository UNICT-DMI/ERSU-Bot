from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from module.shared import read_md

"""/faq command"""
def faq_cmd(update: Update, context: CallbackContext) -> None:
    """Called by /faq command.
        List all the faq about ersu fellowship

        Args:
            update: update event
            context: context passed by the handler
    """
    message_text = read_md("faq")
    context.bot.send_message(chat_id=update.message.chat_id, text=message_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)