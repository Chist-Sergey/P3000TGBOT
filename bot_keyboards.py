# python-telegram-bot to work with Telegram api
from telegram import (
    # allows usage of a message attached buttons
    InlineKeyboardButton as keyboard_option,
    InlineKeyboardMarkup as keyboard_finalize,
)

# for easier text management
from button_manager import (
    ControlButton,
    MonthsButton,
)


def birthday_set_keyboard_months():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=MonthsButton.jan_feb_mar()[0],
                callback_data=MonthsButton.jan_feb_mar()[1],
            ),
            # second option
            keyboard_option(
                text=MonthsButton.apr_may_jun()[0],
                callback_data=MonthsButton.apr_may_jun()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=MonthsButton.jul_aug_sep()[0],
                callback_data=MonthsButton.jul_aug_sep()[1],
            ),
            # second option
            keyboard_option(
                text=MonthsButton.okt_nov_dec()[0],
                callback_data=MonthsButton.okt_nov_dec()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=ControlButton.abort()[0],
                callback_data=ControlButton.abort()[1],
            ),
        ]
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_jan_feb_mar():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=MonthsButton.jan()[0],
                callback_data=MonthsButton.jan()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=MonthsButton.feb()[0],
                callback_data=MonthsButton.feb()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=MonthsButton.mar()[0],
                callback_data=MonthsButton.mar()[1],
            ),
        ]
        # forth row
        [
            # first option
            keyboard_option(
                text=ControlButton.back[0],
                callback_data=ControlButton.back[1],
            ),
        ]
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_apr_may_jun():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=MonthsButton.apr()[0],
                callback_data=MonthsButton.apr()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=MonthsButton.may()[0],
                callback_data=MonthsButton.may()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=MonthsButton.jun()[0],
                callback_data=MonthsButton.jun()[1],
            ),
        ]
        # forth row
        [
            # first option
            keyboard_option(
                text=ControlButton.back[0],
                callback_data=ControlButton.back[1],
            ),
        ]
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_jul_aug_sep():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=MonthsButton.jul()[0],
                callback_data=MonthsButton.jul()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=MonthsButton.aug()[0],
                callback_data=MonthsButton.aug()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=MonthsButton.sep()[0],
                callback_data=MonthsButton.sep()[1],
            ),
        ]
        # forth row
        [
            # first option
            keyboard_option(
                text=ControlButton.back[0],
                callback_data=ControlButton.back[1],
            ),
        ]
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_oct_nov_dec():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=MonthsButton.okt()[0],
                callback_data=MonthsButton.okt()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=MonthsButton.nov()[0],
                callback_data=MonthsButton.nov()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=MonthsButton.dec()[0],
                callback_data=MonthsButton.dec()[1],
            ),
        ]
        # forth row
        [
            # first option
            keyboard_option(
                text=ControlButton.back[0],
                callback_data=ControlButton.back[1],
            ),
        ]
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup
