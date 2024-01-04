# python-telegram-bot to work with Telegram api
from telegram import (
    # allows usage of a message attached buttons
    InlineKeyboardButton as keyboard_option,
    InlineKeyboardMarkup as keyboard_finalize,
)

# for easier text management
from button_manager import (
    GeneralButtons,
    Months,
)

def birthday_set_keyboard_months():
    keyboard = [
        # top row
        [
            # first option
            keyboard_option(
                text=Months.jan_feb_mar()[0],
                callback_data=Months.jan_feb_mar()[1],
            ),
            # second option
            keyboard_option(
                text=Months.apr_may_jun()[0],
                callback_data=Months.apr_may_jun()[1],
            ),
        ],
        # second row
        [
            # first option
            keyboard_option(
                text=Months.jul_aug_sep()[0],
                callback_data=Months.jul_aug_sep()[1],
            ),
            # second option
            keyboard_option(
                text=Months.okt_nov_dec()[0],
                callback_data=Months.okt_nov_dec()[1],
            ),
        ],
        # third row
        [
            # first option
            keyboard_option(
                text=GeneralButtons.button_abort()[0],
                callback_data=GeneralButtons.button_abort()[1],
            ),
            # second option
            keyboard_option(
                text=GeneralButtons.button_continue()[0],
                callback_data=GeneralButtons.button_continue()[1],
            ),
        ]
    ]

    reply_markup = keyboard_finalize(keyboard)

    return reply_markup


# def birthday_year_1_keyboard():
#     keyboard = [
#         # first row
#         [
#             # first option
#             keyboard_option(
#                 text=key_y1_r1_o1(),
#                 callback_data=callback_k1_r1_o1(),
#             ),
#             # second option
#             keyboard_option(
#                 text=key_y1_r1_o2(),
#                 callback_data=callback_k1_r1_o2(),
#             ),
#             # third option
#             keyboard_option(
#                 text=key_y1_r1_o3(),
#                 callback_data=callback_k1_r1_o3(),
#             ),
#         ],
#         # second row
#         [
#             # first option
#             keyboard_option(
#                 text=key_y1_r2_o1(),
#                 callback_data=callback_k1_r2_o1(),
#             ),
#             # second option
#             keyboard_option(
#                 text=key_y1_r2_o2(),
#                 callback_data=callback_k1_r2_o2(),
#             ),
#             # third option
#             keyboard_option(
#                 text=key_y1_r2_o3(),
#                 callback_data=callback_k1_r2_o3(),
#             ),
#         ],
#         # third row
#         [
#             # first option
#             keyboard_option(
#                 text=key_y1_r3_o1,
#                 callback_data=callback_k1_r3_o1(),
#             ),
#             # second option
#             keyboard_option(
#                 text=key_y1_r3_o2,
#                 callback_data=callback_k1_r3_o2(),
#             ),
#             # third option
#             keyboard_option(
#                 text=key_y1_r3_o3(),
#                 callback_data=callback_k1_r3_o3(),
#             ),
#         ],
#         # forth row
#         [
#             # first option
#             keyboard_option(
#                 text=key_abort(),
#                 callback_data=callback_abort(),
#             ),
#             # second option
#             keyboard_option(
#                 text=key_y1_r4_o2(),
#                 callback_data=callback_k1_r4_o2(),
#             ),
#         ],
#     ]

#     reply_markup = keyboard_finalize(keyboard)

#     return reply_markup
