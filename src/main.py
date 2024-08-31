import telegram.ext as tl
import os
import dotenv
import logging

import bot_functions

# _________________________________________________________
# OPTIONS                            <- user attention here
LANGUAGE = 'RUS'
CHECK_BIRTHDAY_TIME_OFFSET = 7
CHECK_BIRTHDAY_TIME_HOURS = (
    8, 20,
)
# _________________________________________________________

# load the bot's key from an .env file
# it now can be accessed in 'getenv'
dotenv.load_dotenv()

logging.basicConfig(filename='error_log.txt',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.ERROR)


def validate_options(options) -> None:
    """
    Check if the user have entered the right range in launch options.

    Valid options:
        options[0] == 'RUS'
        options[1] == 7
        options[2] == (8, 20)
    
    NOT valid options:
        options[0] == 'RU'
        options[1] == Novosibirsk
        options[2] == (-1, 99)
    """
    # language
    assert len(options[0]) == 3
    # time offset / time delta / time zone
    assert type(options[1]) == int
    # time
    for time in options[2]:
        assert time < 24
        assert time >= 0


if __name__ == '__main__':
    bot_options = (LANGUAGE,
                   CHECK_BIRTHDAY_TIME_OFFSET,
                   CHECK_BIRTHDAY_TIME_HOURS)
    validate_options(bot_options)

    bot = tl.ApplicationBuilder().token(os.getenv('TOKEN')).build()

    # tell the bot how it should react to certain things
    birthday_set_handler = tl.CommandHandler(
        'ya_rodilsa', bot_functions.birthday_set)
    birthday_loop_handler = tl.CommandHandler(
        'start', bot_functions.birthday_start)
    birthday_remove_handler = tl.CommandHandler(
        'ya_oshibsa', bot_functions.birthday_remove)

    birthday_button_handler = tl.CallbackQueryHandler(
        bot_functions.birthday_button)

    # POSITION MATTERS: the bot will check them in order of appearence
    bot.add_handler(birthday_button_handler)
    bot.add_handler(birthday_set_handler)
    bot.add_handler(birthday_remove_handler)
    bot.add_handler(birthday_loop_handler)

    bot.run_polling(poll_interval=2.0)
