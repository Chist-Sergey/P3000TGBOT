import telegram.ext as tl
import os
import dotenv
import logging

import bot_functions

BOT_OPTIONS: dict = {
# _________________________________________________________
    'app language': 'RUS',
    'time zone/offset': '+7',
    'time of instance(s) in hours': (
        8, 20,
    ),
# _________________________________________________________
}

# load the bot's key from an .env file
# it now can be accessed in 'getenv'
dotenv.load_dotenv()

logging.basicConfig(filename='error_log.txt',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.ERROR)


def validate_user_options() -> None:
    """
    Check if the user have entered the right range in launch options.

    Valid options:
        ['app language']: 'RUS'
        ['time zone/offset']: '+7',
        ['time of instance(s) in hours']: (8, 20)
    
    NOT valid options:
        ['app language']: 'RU'
        ['time zone/offset']: 'Novosibirsk',
        ['time of instance(s) in hours']: (-1, 99)
    """
    # language
    lang_type = type(BOT_OPTIONS['app language'])
    lang_len = len(BOT_OPTIONS['app language'])
    assert lang_type == str, (
            'Invalid app language. Brackets (\') should stay as is.')
    assert lang_len == 3, (
            'Invalid app language. Example: ENG')

    # time offset
    time_type = type(BOT_OPTIONS['time zone/offset'])
    time_len: int = len(BOT_OPTIONS['time zone/offset'])
    time_value: str = BOT_OPTIONS['time zone/offset']
    assert time_type == str, (
            'Invalid time zone/offset. Brackets (\') should stay as is.')
    assert time_len > 1, (
            'Invalid time zone/offset. Must have at least one number.')
    assert time_len < 4 or time_value < 24, (
            'Invalid time zone/offset. Number too large.')
    try:
        int(time_value)
    except ValueError as err:
        return 'Invalid time zone/offset. Not a number.', err

    # time
    for time in BOT_OPTIONS['time of instance(s) in hours']:
        assert time < 24
        assert time >= 0


if __name__ == '__main__':
    validate_user_options()

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
