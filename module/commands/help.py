# help command

from telegram import Update
from telegram.ext import CallbackContext

def help_cmd(update: Update, context: CallbackContext) -> None:
  context.bot.sendMessage(chat_id=update.message.chat_id, text=
    """Telegram ERSU Bot
    🍽 /menu Fornisce il menù per il prossimo pasto Mensa
    📚 /ufficioersu Fornisce informazioni sugli uffici ERSU Catania
    📬 /report Fornisce la possibilità di poter inviare una segnalazione ai Rappresentanti ERSU, riguardante qualsiasi disservizio, informazione, dubbi e domande""")