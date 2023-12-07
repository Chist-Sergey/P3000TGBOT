# python-telegram-bot to work with Telegram api
from telegram import (
    # allows usage of a message attached buttons 
    InlineKeyboardButton as keyboard_option,
    InlineKeyboardMarkup as keyboard_finalize,
)

def birthday_set_keyboard():
    keyboard = [
        # top row
        [
            keyboard_option(
                text='Убавить на 1',
                callback_data='substract_one',
            ),
            keyboard_option(
                text='Прибавить на 2',
                callback_data='add_two',
            ),
        ],
        # second row
        [
            keyboard_option(
                text='Продолжить',
                callback_data='continue',
            ),
            keyboard_option(
                text='Отмена',
                callback_data='abort',
            ),
        ]
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup