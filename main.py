# -*- coding: utf-8 -*-
"""Main module"""
from distutils.cmd import Command
from warnings import filters
from telegram import BotCommand
from telegram.ext import CommandHandler, MessageHandler, Filters , Dispatcher, Updater

from module.commands.start import start
from module.commands.help import help_cmd
from module.commands.report import report
from module.commands.ufficio_ersu import ufficio_ersu
from module.shared import config_map
from module.data.constants import kb1, kb2, kb3, kb4

def add_commands(up: Updater) -> None:
    """Adds the list of commands with their description to the bot

    Args:
        up (Updater): supplied Updater
    """
    commands = [
        BotCommand("start", "messaggio di benvenuto"),
        BotCommand("help ", "ricevi aiuto sui comandi"),
        BotCommand("report", "segnala un problema"),
        BotCommand("ufficioersu", "ricevi i contatti dell'Ersu")
    ]
    up.bot.set_my_commands(commands=commands)


def add_handlers(dp: Dispatcher) -> None:
    """Adds all the handlers the bot will react to

    Args:
        dp: supplied Dispatcher
    """
    dp.add_handler(CommandHandler('chatid', lambda u, c: u.message.reply_text(u.message.chat_id)))
    dp.add_handler(CommandHandler('help', help_cmd))
    dp.add_handler(MessageHandler(Filters.regex(kb4), help_cmd))
    dp.add_handler(CommandHandler('report', report))
    dp.add_handler(MessageHandler(Filters.regex(kb3), report))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('ufficioersu', ufficio_ersu))
    dp.add_handler(MessageHandler(Filters.regex(kb2), ufficio_ersu))

    #

def main() -> None:
    """Main function"""
    updater = Updater(config_map['token'], request_kwargs={'read_timeout': 20, 'connect_timeout': 20}, use_context=True)
    add_commands(updater)
    add_handlers(updater.dispatcher)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
