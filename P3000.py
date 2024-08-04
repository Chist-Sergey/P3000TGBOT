# P3000.py

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    # to use inline buttons data
    CallbackQueryHandler,
)

from src.bot_functions import (
    birthday_loop,
    birthday_rm,
    birthday_set,
    birthday_btn,
)

from logging import basicConfig, WARNING

# virtual enviroment for a safe key interaction
from dotenv import load_dotenv
from os import getenv

# load the bot's key from an .env file
load_dotenv()

# enable logging
basicConfig(
    # how it would look like
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    # how much we want to observe
    # 'WARNING' == 'anything unusual'
    level=WARNING
)


if __name__ == '__main__':
    # making it all in one line to prevent security vulnerabilities
    application = ApplicationBuilder().token(getenv('TOKEN')).build()

    birthday_set_handler = CommandHandler('ya_rodilsa', birthday_set)
    birthday_loop_handler = CommandHandler('start', birthday_loop)
    birthday_remove_handler = CommandHandler('ya_oshibsa', birthday_rm)

    birthday_button_handler = CallbackQueryHandler(birthday_btn)

    # POSITION MATTERS: the bot will check them in order of appearence
    application.add_handler(birthday_button_handler)
    application.add_handler(birthday_set_handler)
    application.add_handler(birthday_remove_handler)
    application.add_handler(birthday_loop_handler)

    # catching errors to reduce logging pollution
    try:
        # start up the bot
        application.run_polling(poll_interval=2.0)
    # TODO: specify the error
    except EOFError:
        application.run_polling(poll_interval=2.0)
