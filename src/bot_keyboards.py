from telegram import (
    # inline keyboard is located on the message, as opposed to
    # a regular keyboard that located on top of a regular one
    InlineKeyboardButton as button,
    InlineKeyboardMarkup as finalize,
)

from button_manager import (
    Control,
    Months,
    Days,
)


def months():
    keyboard = [
        # top row
        [
            # left
            button(
                text=Months.jan_feb_mar()[0],
                callback_data=Months.jan_feb_mar()[1],
            ),
            # right
            button(
                text=Months.apr_may_jun()[0],
                callback_data=Months.apr_may_jun()[1],
            ),
        ],
        # middle row
        [
            # left
            button(
                text=Months.jul_aug_sep()[0],
                callback_data=Months.jul_aug_sep()[1],
            ),
            # right
            button(
                text=Months.okt_nov_dec()[0],
                callback_data=Months.okt_nov_dec()[1],
            ),
        ],
        # bottom row
        [
            button(
                text=Control.abort()[0],
                callback_data=Control.abort()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def jan_feb_mar():
    keyboard = [
        # first row
        [
            button(
                text=Months.jan()[0],
                callback_data=Months.jan()[1],
            ),
        ],
        # second row
        [
            button(
                text=Months.feb()[0],
                callback_data=Months.feb()[1],
            ),
        ],
        # third row
        [
            button(
                text=Months.mar()[0],
                callback_data=Months.mar()[1],
            ),
        ],
        # bottom row
        [
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def apr_may_jun():
    keyboard = [
        # first row
        [
            button(
                text=Months.apr()[0],
                callback_data=Months.apr()[1],
            ),
        ],
        # second row
        [
            button(
                text=Months.may()[0],
                callback_data=Months.may()[1],
            ),
        ],
        # third row
        [
            button(
                text=Months.jun()[0],
                callback_data=Months.jun()[1],
            ),
        ],
        # bottom row
        [
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def jul_aug_sep():
    keyboard = [
        # first row
        [
            button(
                text=Months.jul()[0],
                callback_data=Months.jul()[1],
            ),
        ],
        # second row
        [
            button(
                text=Months.aug()[0],
                callback_data=Months.aug()[1],
            ),
        ],
        # third row
        [
            button(
                text=Months.sep()[0],
                callback_data=Months.sep()[1],
            ),
        ],
        # bottom row
        [
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def oct_nov_dec():
    keyboard = [
        # first row
        [
            button(
                text=Months.okt()[0],
                callback_data=Months.okt()[1],
            ),
        ],
        # second row
        [
            button(
                text=Months.nov()[0],
                callback_data=Months.nov()[1],
            ),
        ],
        # third row
        [
            button(
                text=Months.dec()[0],
                callback_data=Months.dec()[1],
            ),
        ],
        # bottom row
        [
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def keyboard_days():
    keyboard = [
        # first row
        [
            # left
            button(
                text=Days.one_to_six()[0],
                callback_data=Days.one_to_six()[1],
            ),
            # right
            button(
                text=Days.seven_to_twelve()[0],
                callback_data=Days.seven_to_twelve()[1],
            ),
        ],
        # second row
        [
            # left
            button(
                text=Days.thirteen_to_eighteen()[0],
                callback_data=Days.thirteen_to_eighteen()[1],
            ),
            # right
            button(
                text=Days.nineteen_to_twentyfour()[0],
                callback_data=Days.nineteen_to_twentyfour()[1],
            ),
        ],
        # bottom row
        [
            # left
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
            # right
            button(
                text=Days.twentyfive_to_thirtyone()[0],
                callback_data=Days.twentyfive_to_thirtyone()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def day_1_to_6():
    keyboard = [
        # first row
        [
            # left
            button(
                text=Days.one()[0],
                callback_data=Days.one()[1],
            ),
            # right
            button(
                text=Days.two()[0],
                callback_data=Days.two()[1],
            ),
        ],
        # second row
        [
            # left
            button(
                text=Days.three()[0],
                callback_data=Days.three()[1],
            ),
            # right
            button(
                text=Days.four()[0],
                callback_data=Days.four()[1],
            ),
        ],
        # third row
        [
            # left
            button(
                text=Days.five()[0],
                callback_data=Days.five()[1],
            ),
            # right
            button(
                text=Days.sex()[0],
                callback_data=Days.sex()[1],
            ),
        ],
        # bottom row
        [
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def day_7_to_12():
    keyboard = [
        # first row
        [
            # left
            button(
                text=Days.seven()[0],
                callback_data=Days.seven()[1],
            ),
            # right
            button(
                text=Days.eight()[0],
                callback_data=Days.eight()[1],
            ),
        ],
        # second row
        [
            # left
            button(
                text=Days.nine()[0],
                callback_data=Days.nine()[1],
            ),
            # right
            button(
                text=Days.ten()[0],
                callback_data=Days.ten()[1],
            ),
        ],
        # third row
        [
            # left
            button(
                text=Days.eleven()[0],
                callback_data=Days.eleven()[1],
            ),
            # right
            button(
                text=Days.twelve()[0],
                callback_data=Days.twelve()[1],
            ),
        ],
        # bottom row
        [
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def day_13_to_18():
    keyboard = [
        # first row
        [
            # left
            button(
                text=Days.thirteen()[0],
                callback_data=Days.thirteen()[1],
            ),
            # right
            button(
                text=Days.fourteen()[0],
                callback_data=Days.fourteen()[1],
            ),
        ],
        # second row
        [
            # left
            button(
                text=Days.fifteen()[0],
                callback_data=Days.fifteen()[1],
            ),
            # right
            button(
                text=Days.sixteen()[0],
                callback_data=Days.sixteen()[1],
            ),
        ],
        # third row
        [
            # left
            button(
                text=Days.seventeen()[0],
                callback_data=Days.seventeen()[1],
            ),
            # right
            button(
                text=Days.eighteen()[0],
                callback_data=Days.eighteen()[1],
            ),
        ],
        # bottom row
        [
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def day_19_to_24():
    keyboard = [
        # first row
        [
            # left
            button(
                text=Days.nineteen()[0],
                callback_data=Days.nineteen()[1],
            ),
            # right
            button(
                text=Days.twenty()[0],
                callback_data=Days.twenty()[1],
            ),
        ],
        # second row
        [
            # left
            button(
                text=Days.twenty_one()[0],
                callback_data=Days.twenty_one()[1],
            ),
            # right
            button(
                text=Days.twenty_two()[0],
                callback_data=Days.twenty_two()[1],
            ),
        ],
        # third row
        [
            # left
            button(
                text=Days.twenty_three()[0],
                callback_data=Days.twenty_three()[1],
            ),
            # right
            button(
                text=Days.twenty_four()[0],
                callback_data=Days.twenty_four()[1],
            ),
        ],
        # bottom row
        [
            # left
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def day_25_to_31():
    keyboard = [
        # first row
        [
            # left
            button(
                text=Days.twenty_five()[0],
                callback_data=Days.twenty_five()[1],
            ),
            # right
            button(
                text=Days.twenty_six()[0],
                callback_data=Days.twenty_six()[1],
            ),
        ],
        # second row
        [
            # left
            button(
                text=Days.twenty_seven()[0],
                callback_data=Days.twenty_seven()[1],
            ),
            # right
            button(
                text=Days.twenty_eight()[0],
                callback_data=Days.twenty_eight()[1],
            ),
        ],
        # third row
        [
            # left
            button(
                text=Days.twenty_nine()[0],
                callback_data=Days.twenty_nine()[1],
            ),
            # right
            button(
                text=Days.thirty()[0],
                callback_data=Days.thirty()[1],
            ),
        ],
        # bottom row
        [
            # left
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
            # right
            button(
                text=Days.thirty_one()[0],
                callback_data=Days.thirty_one()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup


def final():
    keyboard = [
        [
            # left
            button(
                text=Control.back()[0],
                callback_data=Control.back()[1],
            ),
            # right
            button(
                text=Control.finish()[0],
                callback_data=Control.finish()[1],
            ),
        ],
    ]

    reply_markup = finalize(keyboard)

    return reply_markup
