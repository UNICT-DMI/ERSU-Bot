# -*- coding: utf-8 -*-
"""Main module"""
from telegram import BotCommand, Chat
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, Filters , Dispatcher, Updater

from module.data import setup_db
from module.commands.start import start
from module.commands.help import help_cmd
from module.commands.report import report
from module.commands.reply import reply
from module.commands.ufficio_ersu import ufficio_ersu
from module.commands.menu import menu
from module.commands.menu_settings import menu_settings
from module.data.menu_settings_buttons import  set_meal_button, reset_button, close_button
from module.shared import config_map
from module.data.constants import CONTACT_ERSU, HELP, MENU_MENSA, MENU_SETTINGS, DAYS_MEAL_REGEX

def add_commands(up: Updater) -> None:
    """Adds the list of commands with their description to the bot

    Args:
        up (Updater): supplied Updater
    """
    commands = []
    if Chat.type == Chat.PRIVATE:
        commands = [
            BotCommand("start", "messaggio di benvenuto"),
            BotCommand("help ", "ricevi aiuto sui comandi"),
            BotCommand("report", "segnala un problema"),
            BotCommand("ufficioersu", "ricevi i contatti dell'Ersu"),
            BotCommand("menu", "ricevi il menù del giorno"),
            BotCommand("menu_settings", "imposta quando ricevere il menù")
        ]
    elif Chat.type == Chat.GROUP or Chat.type == Chat.SUPERGROUP:
        commands = [BotCommand("reply", "rispondi ad una segnalazione")]
    up.bot.set_my_commands(commands=commands)


def add_handlers(dp: Dispatcher) -> None:
    """Adds all the handlers the bot will react to

    Args:
        dp: supplied Dispatcher
    """

    dp.add_handler(CommandHandler('start', start, Filters.chat_type.private))
    dp.add_handler(CommandHandler('chatid', lambda u, c: u.message.reply_text(str(u.message.chat_id))))
    dp.add_handler(CommandHandler('help', help_cmd, Filters.chat_type.private))
    dp.add_handler(MessageHandler(Filters.regex(HELP) & Filters.chat_type.private, help_cmd))
    dp.add_handler(CommandHandler('report', report, Filters.chat_type.private))
    dp.add_handler(CommandHandler('ufficioersu', ufficio_ersu, Filters.chat_type.private))
    dp.add_handler(MessageHandler(Filters.regex(CONTACT_ERSU) & Filters.chat_type.private, ufficio_ersu))
    dp.add_handler(CommandHandler('menu', menu, Filters.chat_type.private))
    dp.add_handler(MessageHandler(Filters.regex(MENU_MENSA) & Filters.chat_type.private, menu))
    dp.add_handler(CommandHandler('menu_settings', menu_settings, Filters.chat_type.private))
    dp.add_handler(MessageHandler(Filters.regex(MENU_SETTINGS) & Filters.chat_type.private, menu_settings))
    dp.add_handler(CommandHandler('reply', reply, Filters.reply & Filters.chat(config_map['admin_group'])))
    dp.add_handler(MessageHandler(Filters.reply & Filters.chat(config_map['admin_group']), reply))

    dp.add_handler(CallbackQueryHandler(set_meal_button, pattern = DAYS_MEAL_REGEX))
    dp.add_handler(CallbackQueryHandler(reset_button, pattern = 'reset'))
    dp.add_handler(CallbackQueryHandler(close_button, pattern = 'close_settings'))

def main() -> None:
    """Main function"""
    updater = Updater(config_map['token'],
        request_kwargs = {'read_timeout': 20, 'connect_timeout': 20},
            use_context = True)
    add_commands(updater)
    add_handlers(updater.dispatcher)
    setup_db()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
