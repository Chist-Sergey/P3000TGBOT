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
    sechude_active,
    search_fail,
    celebrate,
    remove_fail,
    remove_success,
    birthday_set_keyboard_text,
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
from callback_manager import (
    callback_add,
    callback_abort,
    callback_continue,
    callback_substract,
)
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

    If the operation was done successfully,
    tell the user that the operation was successful.

    If the operation wasn't done successfully,
    remove this bot's message.

    Returns nothing.
    Doesn't raise any errors.
    """
    username = update.effective_user.username
    # start the user session
    session_start(username)

    await update.message.reply_text(
        text=birthday_set_keyboard_text(),
        reply_markup=birthday_set_keyboard()
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
    query = update.callback_query
    await query.answer()
    # take the callback data from the keyboard button
    data = query.data

    username = update.effective_user.username
    session_data = session_user_data_extract(username)
    # session_data contains 4 elements:
    # 1     <- a step   (an integer between 0 and 2)
    # 1     <- a day    (an integer between 1 and 31)
    # 1     <- a month  (an integer between 1 and 12)
    # 1900  <- a year   (an integer between 0 and 9999)
    # '[3]' == '4th element in list'
    step = session_data[0]
    # IndexError fix
    fix = 0
    if step >= 4:
        fix -= 1
    # the date that will be changed in this function
    interactive_date = session_data[step + fix]

    # main function of this button
    # looks bad, but sometimes simpler is better
    if data == callback_add():
        interactive_date += 2

    if data == callback_substract():
        interactive_date -= 1

    # record the result, even if nothing has changed
    session_data[step] = interactive_date

    if data == callback_abort():
        step -= 1

    if data == callback_continue():
        step += 1

    # record the result, even if nothing has changed
    session_data[0] = step

    # write the results back in the user file
    session_user_data_write(username, session_data)

    dates = ('day', 'month', 'year', '(',)
    interactive_date = session_data[step + fix]
    # 'f' == 'format' == 'put variables in place of names'
    # '\n' == 'new line' == 'make the text begin below the current text'
    # 'step - 1' is for index compatibility
    # between 'session_data' and 'dates'
    interactive_text = f'\n{dates[step - 1]}: {interactive_date}'

    # I'm afraid of making any early return
    # in this function, so I placed this code
    # before the step checks so this message text
    # would be overriden by the step checks
    await query.edit_message_text(
        text=birthday_set_keyboard_text() + interactive_text,
        reply_markup=birthday_set_keyboard()
    )

    # check if the user have ended their interaction
    # bad ending: the user refused to give their birthday
    if step < 1:
        await query.edit_message_text(
            text='over',
        )
    # good ending: the user gave their birthday
    if step > 3:
        await query.edit_message_text(
            text='done',
        )
