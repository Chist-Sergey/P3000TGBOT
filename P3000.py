# P3000.py

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    # allows using inline buttons data
    CallbackQueryHandler,
)

# line is too long when using google style of import
from src.bot_functions import (
    birthday_loop,
    birthday_rm,
    birthday_set,
    birthday_btn,
)

# virtual enviroment for a safe key interaction
from os import getenv
from dotenv import load_dotenv

# load the bot's key from an .env file
load_dotenv()


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

    application.run_polling(poll_interval=2.0)
