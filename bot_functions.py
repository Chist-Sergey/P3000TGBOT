# python-telegram-bot to work with Telegram api
from telegram import (
    # core
    Update,
)
from telegram.ext import (
    # core
    ContextTypes,
)

# get and set a time
from datetime import datetime

# for easier text management
from text_responses import (
    birthday_set_keyboard_text,
    celebrate,
    remove_fail,
    remove_success,
    sechude_active,
    write_exists,
    write_success,
)
# for working with keyboard's memory
from session_functions import (
    session_start,
    session_user_data_extract,
    session_user_data_write,
)
# for easier keyboard management
from bot_keyboards import (
    birthday_set_keyboard,
)
# for syncing the callback names with keyboard
from button_manager import BadKeyboard as kb
# to access database
from database_functions import (
    database_remove,
    database_search_by_date,
    database_search_by_name,
    database_write,
)


async def birthday_loop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Initiates the bot's checking cycle with 'jobQueue'.

    Returns nothing.
    Doesn't raise any errors.
    """
    # message destination is a chat where it was used
    target_chat = update.effective_message.chat_id
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
        chat_id=target_chat
    )

    # send a reply message to the user
    await context.bot.send_message(
        chat_id=target_chat,
        text=sechude_active(),
    )


async def birthday_set(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Set a birthday date.

    Takes no arguments.

    If the user is already present in a database,
    tell the user their birthday date.

    If there's no such user,
    bring up a message with a keyboard for
    the user to enter their birthday date.

    Returns nothing.
    Doesn't raise any errors.
    """
    keyboard = birthday_set_keyboard()
    message = birthday_set_keyboard_text()
    username = update.effective_user.username

    session_start(username)

    birthday_date = database_search_by_name(username)
    if birthday_date:
        message = birthday_date
        keyboard = None

    await update.message.reply_text(
        text=message,
        reply_markup=keyboard
    )


async def birthday_yell(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Celebrate a birth day!

    Takes no arguments.D
    Checks for someone's birthday today,
    sends a message if someone has a birthday,
    does nothing if there isn't.

    Returns nothing.
    Doesn't raise any errors.
    """
    today = datetime.now()

    # '%d.%m' == 'D.M' == 'Day.Month', ex.: '31.12'
    today_day_and_month = today.strftime('%d.%m')
    birthday_people = database_search_by_date(today_day_and_month)

    if birthday_people:
        await context.bot.send_message(
            # message destination is a chat where it was used
            chat_id=context.job.chat_id,
            text=celebrate(birthday_people),
        )


async def birthday_rm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Remove a birthday.

    Takes no arguments.

    Take a USER who called this function
    and check if they are in a database.

    If they are, remove their line from
    the database and aknowledge them of this.

    If they aren't, aknowledge them of this.

    Returns nothing.
    Doesn't raise any errors.
    """
    # there are two states of this message:
    # 0: the code failed
    # 1: the code succeed
    # having the initial value set as one of these states
    # allows to make one less check on the function's state
    message = remove_fail()

    username = update.effective_user.username
    target_line = database_search_by_name(username)

    if target_line:
        database_remove(target_line)
        message = remove_success()

    await context.bot.send_message(
        # message destination is a chat where it was used
        chat_id=update.effective_chat.id,
        text=message,
    )


async def birthday_btn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Input to set a birthday date.

    Takes no arguments.

    Allows the user to change their birthday date
    by pressing buttons on the inline keyboard.

    If the operation was done successfully,
    tell the user that the operation was successful.

    If the operation wasn't done successfully,
    remove this bot's message.

    Returns nothing.
    Doesn't raise any errors.
    """
    dates = (
        ['День', 31],
        ['Месяц', 12],
        ['Год', 9999],
        # a fix to an IndexError
        ['boo!', 0],
    )
    keyboard = birthday_set_keyboard()
    message = birthday_set_keyboard_text()
    username = update.effective_user.username
    # create, get and extract the user's input
    query = update.callback_query
    await query.answer()
    data = query.data

    session_data = session_user_data_extract(username)

    # session_data contains 4 elements:
    # 1     <- a day    (an integer between 1 and 31)
    # 1     <- a month  (an integer between 1 and 12)
    # 1900  <- a year   (an integer between 1 and 9999)
    # 0     <- a step   (an integer between -1 and 2)
    # '[-1]' == 'last element in list' == '4th element in list'
    step = session_data[-1]
    date_interactive = session_data[step]
    date_max = dates[step][1]

    if data == kb.button_add()[1]:
        if date_interactive < date_max:
            date_interactive += 2

    if data == kb.button_substract()[1]:
        if date_interactive > 1:
            date_interactive -= 1

    # record the result
    session_data[step] = date_interactive

    if data == kb.button_abort()[1]:
        step -= 1

    if data == kb.button_continue()[1]:
        step += 1

    # record the result
    session_data[-1] = step

    session_user_data_write(username, session_data)

    date_interactive = session_data[step]
    date = dates[step][0]
    # 'f' == 'format' == 'put variables in place of names'
    # '\n' == 'new line' == 'make the text begin below the current text'
    # 'step - 1' is for index compatibility
    # between 'session_data' and 'dates'
    interactive_text = f'\n{date}: {date_interactive}'

    # check if the user have ended their interaction
    # good ending: the user entered their birthday
    if step > 2:
        message = write_success()
        keyboard = None
        interactive_text = ''
        database_write(username)

    # main "ending" is set before the last check
    # to avoid BadRequest error due to a missing message
    await query.edit_message_text(
        text=message + interactive_text,
        reply_markup=keyboard
    )

    # bad ending: the user refused to give their birthday
    if step < 0:
        await query.delete_message()
