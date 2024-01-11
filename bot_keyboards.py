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
    DaysButton,
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
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.abort()[0],
                callback_data=ControlButton.abort()[1],
            ),
        ],
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
        ],
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
        ],
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
        ],
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
        ],
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
        ],
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
        ],
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
        ],
        # forth row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
        ],
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_days():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=DaysButton.one_to_six()[0],
                callback_data=DaysButton.one_to_six()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.seven_to_twelve()[0],
                callback_data=DaysButton.seven_to_twelve()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=DaysButton.thirteen_to_eighteen()[0],
                callback_data=DaysButton.thirteen_to_eighteen()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.nineteen_to_twentyfour()[0],
                callback_data=DaysButton.nineteen_to_twentyfour()[1],
            ),
        ],
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.twentyfive_to_thirtyone()[0],
                callback_data=DaysButton.twentyfive_to_thirtyone()[1],
            ),
        ],
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_day_1_to_6():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=DaysButton.one()[0],
                callback_data=DaysButton.one()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.two()[0],
                callback_data=DaysButton.two()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=DaysButton.three()[0],
                callback_data=DaysButton.three()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.four()[0],
                callback_data=DaysButton.four()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=DaysButton.five()[0],
                callback_data=DaysButton.five()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.sex()[0],
                callback_data=DaysButton.sex()[1],
            ),
        ],
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
        ],
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_day_7_to_12():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=DaysButton.seven()[0],
                callback_data=DaysButton.seven()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.eight()[0],
                callback_data=DaysButton.eight()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=DaysButton.nine()[0],
                callback_data=DaysButton.nine()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.ten()[0],
                callback_data=DaysButton.ten()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=DaysButton.eleven()[0],
                callback_data=DaysButton.eleven()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.twelve()[0],
                callback_data=DaysButton.twelve()[1],
            ),
        ],
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
        ],
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_day_13_to_18():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=DaysButton.thirteen()[0],
                callback_data=DaysButton.thirteen()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.fourteen()[0],
                callback_data=DaysButton.fourteen()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=DaysButton.fifteen()[0],
                callback_data=DaysButton.fifteen()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.sixteen()[0],
                callback_data=DaysButton.sixteen()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=DaysButton.seventeen()[0],
                callback_data=DaysButton.seventeen()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.eighteen()[0],
                callback_data=DaysButton.eighteen()[1],
            ),
        ],
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
        ],
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_day_19_to_24():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=DaysButton.nineteen()[0],
                callback_data=DaysButton.nineteen()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.twenty()[0],
                callback_data=DaysButton.twenty()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=DaysButton.twenty_one()[0],
                callback_data=DaysButton.twenty_one()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.twenty_two()[0],
                callback_data=DaysButton.twenty_two()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=DaysButton.twenty_three()[0],
                callback_data=DaysButton.twenty_three()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.twenty_four()[0],
                callback_data=DaysButton.twenty_four()[1],
            ),
        ],
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
        ],
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_day_25_to_31():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=DaysButton.twenty_five()[0],
                callback_data=DaysButton.twenty_five()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.twenty_six()[0],
                callback_data=DaysButton.twenty_six()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=DaysButton.twenty_seven()[0],
                callback_data=DaysButton.twenty_seven()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.twenty_eight()[0],
                callback_data=DaysButton.twenty_eight()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=DaysButton.twenty_nine()[0],
                callback_data=DaysButton.twenty_nine()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.thirty()[0],
                callback_data=DaysButton.thirty()[1],
            ),
        ],
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
            # second option
            keyboard_option(
                text=DaysButton.thirty_one()[0],
                callback_data=DaysButton.thirty_one()[1],
            ),
        ],
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


def birthday_set_keyboard_final():
    keyboard = [
        # bottom row
        [
            # first option
            keyboard_option(
                text=ControlButton.back()[0],
                callback_data=ControlButton.back()[1],
            ),
            # second option
            keyboard_option(
                text=ControlButton.finish()[0],
                callback_data=ControlButton.finish()[1],
            ),
        ],
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup
