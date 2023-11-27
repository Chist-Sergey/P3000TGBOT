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
    sechude_active,
    write_success,
    write_exists,
    write_fail,
    search_fail,
    celebrate,
    remove_success,
    remove_fail,
)

# set the day and the month of someone's birthday
from datetime import datetime

from re import (
    sub,
    search,
)

# monitoring the bot's behavior
from logging import basicConfig, WARNING

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
    level=WARNING
)


async def birthday_loop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Initiates the bot's checking cycle with 'jobQueue'.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    chat_id = update.effective_message.chat_id
    # tell the bot to run a job repeatedly
    context.job_queue.run_repeating(
        # which job
        callback=birthday_yell,
        # at what interval (in seconds)
        # '42300 seconds' == '12 hours' == 'twice a day'
        interval=42300,
        # when it should start from now (in seconds)
        # '60 seconds' == '1 minute'
        first=60,
        # where the text will be sent
        chat_id=chat_id
    )

    # send a reply message to the user
    await context.bot.send_message(
        chat_id=chat_id,  # recipient
        text=sechude_active(),
    )


def database_write(name: str, date) -> None:
    """
    Use this function to write a pair of user name
    and birthday date to a database text file.

    It's a simple open-format-write-close operation.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # 'a' == 'append' == 'apply at the end'
    with open('database.txt', 'a') as database:
        # 'f' == 'format' == 'replace names with their values'
        # '\n' == 'new line'
        data_row = f'{name} {date}\n'
        database.write(data_row)


def database_remove(target_line: str) -> None:
    """
    Use this function to remove a line of user name
    and birthday date from a database text file.

    It's a simple open-find-remove-close operation,
    horever, it's actually replaces a target line with nothing.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # 'r+' == 'reading and writing'
    with open('database.txt', 'r+') as database:
        content = database.read()
        # 'sub' == 'find and replace' (this, that, there)
        # '' == 'Nothing'
        content_new = sub(target_line, '', content)
        # 'seek' == 'move a coursor' == 'set a writing point'
        database.seek(0)
        database.write(content_new)


def database_search_by_name(target: str):
    """
    Use this function to search and retrive
    a string from a database text file.

    It's a simple O(n) search algorithm,
    checking one line at a time.

    This function returns a whole line if the
    string is matched, None if not mached.
    This function doesn't raise any errors.
    """
    with open('database.txt', 'r') as database:
        content = database.read()
        target = r'[target] [numbers]'
        found = search(target, content)

    return None


def database_search_by_date(target: str):
    """
    Use this function to search and retrive
    all matches on the given string.

    It's a simple O(n) search algorithm,
    checking the database contents line by line.

    This function returns a multiline string
    if the strings are found, or None if not.
    This function doesn't raise any errors.
    """
    # an empty sting is equal to False
    data = ''

    with open('database.txt', 'r') as database:
        for line in database:
            # the last 5 chracters are the day and month
            if target[:5] in line:
                data += line + '\n'

    # check for any changes in the data
    if data == '':
        data = None

    return data


async def birthday_set(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Set a birthday date.

    This function takes one reuqired argument.

    Using it without any argument will
    tell the user to use this command with a DATE.

    Using it with one argument (DATE) will
    add THIS user as the birthday person
    and set their birthday up to DATE.

    If the user is already present in a database,
    tell the user that they are already on a list.

    If the operation was done successfully,
    tell the user that the operation was successful.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # any further check will replace the 'fail' text
    message = write_fail()

    # what the user wrote with this command
    arguments = context.args
    # their user name to check on it in a database
    user_name = update.effective_user.name
    # check and remember if the user is already in there
    user_exists = database_search_by_name(user_name)

    # check for the presence of the user in a database
    if user_exists:
        # replace the 'fail' text with 'user_exists' one
        message = write_exists()

    # check for the arguments
    if arguments and user_exists is None:
        # the first argument should be a date
        birthday_date = arguments[0]
        # see if the date entered is valid
        if date_validate(birthday_date):
            # write a user name and a date to a database
            database_write(user_name, birthday_date)
            # replace the 'fail' message to a 'success' one
            message = write_success()
        
        approximate_birthday_date = date_guess(birthday_date)
        if date_validate(approximate_birthday_date):
            database_write(user_name, approximate_birthday_date)
            message=write_success()


    # sending feedback to the user
    await context.bot.send_message(
        chat_id=update.effective_chat.id,  # recipient
        text=message,
    )


def date_guess(data: str) -> str:
    numbers_buffer = ''
    numbers_extracted = []
    numbers_valid = []
    limit_search = 31

    if len(data) > limit_search:
        data = data[:limit_search]

    for character in data:
        if character.isnumeric():
            numbers_buffer += character
        else:
            numbers_extracted.append(numbers_buffer)
            numbers_buffer = ''

    dates = list(map(int, dates))

    for number in dates:
        if (number >= 1 and number <= 31):
            numbers_valid.append(number)

    final_string = ' '.join(numbers_valid)
    return final_string


def date_validate(date: str) -> bool:
    try:
        datetime.strptime(date, '%d.%m')
    except ValueError:
        return False
    return True


async def birthday_get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Peek a birthday date.

    This function takes up to one optional argument.

    Using it without any argument will
    send a message with THIS user's birthday date.

    Using it with one argument (USER) will
    send a message with THAT user's birthday date.

    Using it with one argument (DATE) will
    send a message with all users whose birthday
    is matching DATE.

    If USER is not in the database,
    tell the user that there's no such USER
    in the database.

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
        # replace result's 'None' with a fail message
        search_result = search_fail()

    await context.bot.send_message(
        chat_id=update.effective_chat.id,  # recipient
        text=search_result,
    )


async def birthday_yell(context: ContextTypes.DEFAULT_TYPE) -> None:
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
            chat_id=context.job.chat_id,  # recipient
            text=celebrate(birthday_people),
        )


async def birthday_rm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Remove a birthday.

    This function takes no arguments.

    Take a USER who called this function
    and check if they are in a database.
    If they are, remove their line from
    the database and aknowledge them of this.
    If they aren't, aknowledge them of this.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    message = remove_fail()
    username = update.effective_user.name
    target_line = database_search_by_name(username)
    if target_line:
        message = remove_success()
        database_remove(target_line)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
    )


if __name__ == '__main__':
    # setting up the bot
    application = ApplicationBuilder().token(getenv('TG_BOT_TOKEN')).build()

    # setting up the commands
    birthday_set_handler = CommandHandler('ya_rodilsa', birthday_set)
    birthday_get_handler = CommandHandler('kogda_dr', birthday_get)
    birthday_loop_handler = CommandHandler('rabotay', birthday_loop)
    birthday_remove_handler = CommandHandler('ya_oshibsa', birthday_rm)

    # telling said commands for the bot to recognize them
    # POSITION MATTERS: the bot will check them in order of appearence
    application.add_handler(birthday_set_handler)
    application.add_handler(birthday_get_handler)
    application.add_handler(birthday_remove_handler)
    application.add_handler(birthday_loop_handler)
    # asking the server for anything new every couple of seconds
    application.run_polling(poll_interval=3.0)
