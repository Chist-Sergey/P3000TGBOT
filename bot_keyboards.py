# python-telegram-bot to work with Telegram api
from telegram import (
    # allows usage of a message attached buttons
    InlineKeyboardButton as keyboard_option,
    InlineKeyboardMarkup as keyboard_finalize,
)

# for easier text management
from button_text import (
    key_add,
    key_abort,
    key_continue,
    key_substract,
)
# for syncing the callback data
from callback_manager import (
    callback_substract,
    callback_abort,
    callback_add,
    callback_continue,
)

def birthday_set_keyboard():
    keyboard = [
        # top row
        [
            keyboard_option(
                text=key_substract(),
                callback_data=callback_substract(),
            ),
            keyboard_option(
                text=key_add(),
                callback_data=callback_add(),
            ),
        ],
        # second row
        [
            keyboard_option(
                text=key_continue(),
                callback_data=callback_continue(),
            ),
            keyboard_option(
                text=key_abort(),
                callback_data=callback_abort(),
            ),
        ]
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup
