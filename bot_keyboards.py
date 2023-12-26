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
    key_k1_r1_o1,
    key_k1_r1_o2,
    key_k1_r1_o3,
    key_k1_r2_o1,
    key_k1_r2_o2,
    key_k1_r2_o3,
    key_k1_r3_o1,
    key_k1_r3_o2,
    key_k1_r3_o3,
    key_k1_r4_o2,
)
# for syncing the callback data
from callback_values import (
    callback_substract,
    callback_abort,
    callback_add,
    callback_continue,
    callback_k1_r1_o1,
    callback_k1_r1_o2,
    callback_k1_r1_o3,
    callback_k1_r2_o1,
    callback_k1_r2_o2,
    callback_k1_r2_o3,
    callback_k1_r3_o1,
    callback_k1_r3_o2,
    callback_k1_r3_o3,
    callback_k1_r4_o2,
)

def birthday_set_keyboard():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=key_substract(),
                callback_data=callback_substract(),
            ),
            # second option
            keyboard_option(
                text=key_add(),
                callback_data=callback_add(),
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=key_abort(),
                callback_data=callback_abort(),
            ),
            # second option
            keyboard_option(
                text=key_continue(),
                callback_data=callback_continue(),
            ),
        ]
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_year_1_keyboard():
    keyboard = [
        # first row
        [
            # first option
            keyboard_option(
                text=key_k1_r1_o1(),
                callback_data=callback_k1_r1_o1(),
            ),
            # second option
            keyboard_option(
                text=key_k1_r1_o2(),
                callback_data=callback_k1_r1_o2(),
            ),
            # third option
            keyboard_option(
                text=key_k1_r1_o3(),
                callback_data=callback_k1_r1_o3(),
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=key_k1_r2_o1(),
                callback_data=callback_k1_r2_o1(),
            ),
            # second option
            keyboard_option(
                text=key_k1_r2_o2(),
                callback_data=callback_k1_r2_o2(),
            ),
            # third option
            keyboard_option(
                text=key_k1_r2_o3(),
                callback_data=callback_k1_r2_o3(),
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=key_k1_r3_o1,
                callback_data=callback_k1_r3_o1(),
            ),
            # second option
            keyboard_option(
                text=key_k1_r3_o2,
                callback_data=callback_k1_r3_o2(),
            ),
            # third option
            keyboard_option(
                text=key_k1_r3_o3(),
                callback_data=callback_k1_r3_o3(),
            ),
        ],
        # forth row
        [
            # first option
            keyboard_option(
                text=key_abort(),
                callback_data=callback_abort(),
            ),
            # second option
            keyboard_option(
                text=key_k1_r4_o2(),
                callback_data=callback_k1_r4_o2(),
            ),
        ],
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup
