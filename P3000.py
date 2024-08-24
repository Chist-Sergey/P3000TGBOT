# P3000.py

import telegram.ext as tl

from src import bot_functions

from os import getenv
from dotenv import load_dotenv

# load the bot's key from an .env file
# it now can be accessed in 'getenv'
load_dotenv()


if __name__ == '__main__':
    bot = tl.ApplicationBuilder().token(
        getenv('TOKEN')).build()

    # tell the bot how it should react to certain things
    birthday_set_handler = tl.CommandHandler(
        'ya_rodilsa', bot_functions.birthday_set)
    birthday_loop_handler = tl.CommandHandler(
        'start', bot_functions.birthday_loop)
    birthday_remove_handler = tl.CommandHandler(
        'ya_oshibsa', bot_functions.birthday_rm)

    birthday_button_handler = tl.CallbackQueryHandler(
        bot_functions.birthday_btn)

    # POSITION MATTERS: the bot will check them in order of appearence
    bot.add_handler(birthday_button_handler)
    bot.add_handler(birthday_set_handler)
    bot.add_handler(birthday_remove_handler)
    bot.add_handler(birthday_loop_handler)

    bot.run_polling(poll_interval=2.0)
