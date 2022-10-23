"""Tests for the commands module"""
# pylint: disable=missing-class-docstring,missing-function-docstring,too-few-public-methods,redefined-outer-name
from datetime import datetime
import pytest
from pytest_mock import MockerFixture
from telegram import Update, User, Message, Chat
from telegram.ext import CallbackContext, Updater
from module.commands import help_cmd, start, ufficio_ersu
from module.data.constants import START_CMD_TEXT, HELP_CMD_TEXT, UFFICIO_ERSU_CMD_TEXT


class FixtureRequest:
    """Fixture request class used for type hinting"""

    param: str


@pytest.fixture(scope="function")
def context(mocker: MockerFixture) -> CallbackContext:
    """Creates a Telegram CallbackContext.
    The bot is mocked, meaning every method used will not produce any effect.
    This also allows to check how many time a method has been called and with what args"""
    updater = Updater(token="1234567890:abcdefghijklmnopqrstuvwxyz123456789")
    dispatcher = updater.dispatcher
    dispatcher.bot = mocker.Mock(return_value=None)
    return CallbackContext(dispatcher)


@pytest.fixture(scope="function", params=[Chat.GROUP])
def update(request: FixtureRequest) -> Update:
    """Creates a Telegram Update object, caused by a message being sent.
    By default, the message is treated as being sent in a group chat.
    To change this behavior, use the following decorator on top of the test method:

    ```python
    @pytest.mark.parametrize("update", [Chat.PRIVATE, Chat.CHANNEL], indirect=True)
    def test_method(self, update: Update, context: CallbackContext):
        ... # test code
    ```
    """
    chat = Chat(id=0, type=request.param)
    user = User(id=0, first_name="user", is_bot=False, username="user")
    message = Message(message_id=0, from_user=user, chat=chat, date=datetime.now())
    return Update(update_id=0, message=message)


class TestCommands:
    def test_start_cmd(self, update: Update, context: CallbackContext) -> None:
        start(update, context)
        context.bot.sendMessage.assert_called_once_with(
            chat_id=update.message.chat_id, text=START_CMD_TEXT
        )

    def test_help_cmd(self, update: Update, context: CallbackContext) -> None:
        help_cmd(update, context)
        context.bot.sendMessage.assert_called_once_with(
            chat_id=update.message.chat_id, text=HELP_CMD_TEXT
        )

    def test_ufficio_ersu_cmd(self, update: Update, context: CallbackContext) -> None:
        ufficio_ersu(update, context)
        context.bot.sendMessage.assert_called_once_with(
            chat_id=update.message.chat_id, text=UFFICIO_ERSU_CMD_TEXT
        )
