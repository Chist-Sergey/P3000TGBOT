# core libraries for the bot to function
from telegram import (
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,  # adds commands to the bot
)

# pulling up text responses individually (for safety reasons)
from text_responses import (
    greeting,
    write_success,
    write_fail,
    search_fail,
    celebrate
)

# place a day and the month of someone's birthday
from datetime import datetime

# monitoring the bot's behavior
from logging import basicConfig, INFO

# virtual enviroment for a safe key interaction
from dotenv import load_dotenv
from os import getenv

# loading the bot's key from an .env file
load_dotenv()

# enabling logging
basicConfig(
    # what it would look like
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    # how much we want to observe (INFO == all of it)
    level=INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Sends a message on a /start command (what a waste of visual
    space. I can't wait to replace all of the messages with
    a simple reaction on a message).
    Initiates the bot's living cycle with 'jobQueue'.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    #
    time = datetime.time(
        hour=12,
        minute=12,
    )
    # initiating a function to celebrate birthdays
    context.job_queue.run_daily(
        birthday_yell,
        time=time,
    )

    # the bot's respond to the 'start' command
    await context.bot.send_message(
        chat_id=update.effective_chat.id,  # recipient
        text=greeting(),
    )


def database_write(name: str, date) -> None:
    """
    Use this function to write a pair of user name
    and birthday date to a database text file.
    It's a simple open-format-write-close operation.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    database = open('database.txt', 'a')
    data_row = f'{name} {date}\n'
    database.write(data_row)
    database.close()


def database_search_by_name(target: str):
    """
    Use this function to search and retrive
    a string in a database text file.
    It's a simple O(n) search algorithm,
    checking one line at a time.

    This function returns a whole line if the
    string is matched, None if not mached.

    This function doesn't raise any errors.
    """
    with open('database.txt', 'r') as database:
        for line in database:
            if target in line:
                return line
    return None


def database_search_by_date(target: str):
    """
    Use this function to search and retrive
    all matches on the given string.
    It's a simple O(n) search algorithm,
    checking one line at a time.

    This function returns a multiline string if the
    string is matched, an empty string if not mached.

    This function doesn't raise any errors.
    """
    with open('database.txt', 'r') as database:
        for line in database:
            if target[:5] in line:
                target += line + '\n'

    # not working when target is <5 characters
    if target[:5] == target:
        target = None

    return target


async def birthday_set(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Set the user's birthday date.

    This function takes up to two optional arguments.

    Using it without any argument will
    add THIS user as the birthday person and
    set their birthday day to TODAY.

    Using it with one argument (person) will
    add THAT user as the birthday person and
    set their birthday day to TODAY.

    Using it with two arguments (person, date) will
    add THAT user as the birthday person and
    set their birthday day to that DATE.

    If the arguments are invalid,
    or the user is already present in a database,
    react to the message with a thumb down emoji.

    If the operation was done successfully,
    react to the message with a thumb up emoji.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # implementing a case where no arguments were given
    # taking a name of the person who used this command
    user_name = update.effective_user.name
    # getting the current day and month in a 'DD:MM' format
    birthday_date = datetime.now().strftime('%d.%m')

    # check for the command to have any text
    if context.args:
        # the first argument is guranteed to be there
        user_name = context.args[0]
        """
        unfortunally, 'if context.args[1]:' triggers an IndexError
        so the only easy option is a big and cluncy try/except combo
        """
        # check for the second argument
        try:
            # updating the date with the second argument
            birthday_date = context.args[1]
        except IndexError:
            pass
        # any other argument beside these two is discarded

    # negative feedback in case the user already exists
    message = write_fail()
    # check if the user is already exists
    if database_search_by_name(user_name) is None:
        # adding said user
        database_write(user_name, birthday_date)
        # giving a positive feedback on this action
        message = write_success()

    # sending feedback to the user
    await context.bot.send_message(
        chat_id=update.effective_chat.id,  # recipient
        text=message,
    )


async def birthday_get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Peek the user's birthday date.

    This function takes up to one optional argument.

    Using it without any argument will
    send a message with THIS user's birthday date.

    Using it with one argument (person) will
    send a message with THAT user's birthday date.

    Using it with one argument (date) will
    send a message with all users with matching birthday DATE.

    If the arguments are invalid,
    react to the message with a thumb down emoji.

    If the operation was done successfully,
    react to the message with a thumb up emoji.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # branchless programming isn't going to work here
    if context.args:
        # making sure we take only a single argument
        target = context.args[0]
        # check to decide which search function to use
        if target.isnumeric():
            search_result = database_search_by_date(target)
        else:  # a name can't be numeric, right?
            search_result = database_search_by_name(target)
    # using the user's own name to search a date for
    else:
        target = update.effective_user.name
        search_result = database_search_by_name(target)

    # check for a valid result
    if search_result is None:
        # replace result's "None" with a fail message
        search_result = search_fail()

    await context.bot.send_message(
        chat_id=update.effective_chat.id,  # recipient
        text=search_result,
    )


async def birthday_yell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Celebrate a birth day!

    This function is autonomous and takes no arguments.

    Checks for someone's birthday daily,
    sends a message if there are birthday,
    does nothing if there isn't.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    target = datetime.now().strftime('%d.%m')
    birthday_people = database_search_by_date(target)
    if birthday_people:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,  # recipient
            text=celebrate(birthday_people),
        )


if __name__ == '__main__':
    # setting up the bot
    application = ApplicationBuilder().token(getenv('TG_BOT_TOKEN')).build()

    # setting up the commands
    birthday_set_handler = CommandHandler('ya_rodilsa', birthday_set)
    birthday_get_handler = CommandHandler('kogda_dr', birthday_get)
    start_handler = CommandHandler('start', start)

    # applying said commands for the bot to recognize them
    # POSITION MATTERS: the bot will check them in order of appearence
    application.add_handler(start_handler)
    application.add_handler(birthday_get_handler)
    application.add_handler(birthday_set_handler)

    # asking the server for anything new every couple of seconds
    application.run_polling(poll_interval=3.0)
