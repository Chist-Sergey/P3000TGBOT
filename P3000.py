# P3000.py
"""
comment format - from up to down/from top to bottom.
text in round brackets is optional.

all comments are written in lowercase
except then refering to a variable name
or if it's a function or class description.

all comments are optional
and can be written multiple times.

example (newline after this colon is included):

# comment above the code
# more comment above the code
# 'variable' == 'description' == 'more description'
code below the comment
more code below the comment
"""

from telegram.ext import (
    # core
    ApplicationBuilder,
    # adds commands to the bot
    CommandHandler,
    # to use an inline buttons data
    CallbackQueryHandler,
)

# for easier function management
from bot_functions import (
    birthday_loop,
    birthday_rm,
    birthday_set,
    birthday_btn,
)

# monitor the bot's behavior
from logging import basicConfig, WARNING

# virtual enviroment for a safe key interaction
from dotenv import load_dotenv
from os import getenv

# load the bot's key from an .env file
load_dotenv()

# enable logging
basicConfig(
    # how it would look like
    # 'format' == 'replace names with their values'
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    # how much we want to observe
    # 'WARNING' == 'anything unusual'
    level=WARNING
)


if __name__ == '__main__':
    # setup the bot in a single line to prevent security vulnerabilities
    application = ApplicationBuilder().token(getenv('TOKEN')).build()

    # setup the commands
    birthday_set_handler = CommandHandler('ya_rodilsa', birthday_set)
    birthday_loop_handler = CommandHandler('rabotay', birthday_loop)
    birthday_remove_handler = CommandHandler('ya_oshibsa', birthday_rm)
    birthday_button_handler = CallbackQueryHandler(birthday_btn)

    # tell said commands to the bot for it to recognize them
    # POSITION MATTERS: the bot will check them in order of appearence
    application.add_handler(birthday_button_handler)
    application.add_handler(birthday_set_handler)
    application.add_handler(birthday_remove_handler)
    application.add_handler(birthday_loop_handler)
    # ask the server for anything new every couple of seconds
    application.run_polling(poll_interval=3.0)

"""
a template for testing functions.

usage:
copy an entire function you want
to test from the code and paste
it in a separate *.py file,
then copy and paste this template
at the bottom of that file
and edit it to your needs.

uncomment the premade functions
to save time on creating them.

if __name__ == '__main__':
    # change this to your needs
    test_function = database_remove
    test_data_auto_amount = 10
    test_data_manual = [
        'asdfg 56:78',
        'sdlfk 76:58',
        'mkgtj 98:76',
        'sdfkl 37:84',
        'tbytj 93:85',
        'lkjli 27:38',
        'ChistovBackend 09.09',
    ]

    # generates a data row
    test_data_list = []
    for number in range(test_data_auto_amount):
        test_data = '{}.{}.{}'.format(
            10 + number,
            10 + number,
            1000 + number,
        )
        test_data_list.append(test_data)

    # check the output in terminal
    print(f'\n\n{test_function}')
    print('\n\tGenerated Data\n')
    for test_data in test_data_list:
        print(
            f'{test_data} -> '
            f'{test_function(test_data)}'
        )
    print('\n\tManual Data\n')
    for test_data in test_data_manual:
        print(
            f'{test_data} -> '
            f'{test_function(test_data)}'
        )
"""
