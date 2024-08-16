# bot_functions.py

from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
)
from telegram.error import (
    # to know what error to catch
    BadRequest,
    Forbidden,
)
from datetime import (
    datetime,
    time,
)
from zoneinfo import (
    ZoneInfo,
)
from src.button_manager import (
    # to sync the callback names with keyboard
    Control,
)
from bot_options import (
    TIME_HOUR_FIRST,
    TIME_HOUR_OFFSET,
    TIME_HOUR_SECOND,
)

from src import (
    text_responses,
    bot_keyboards,
    session_functions,
    database_functions,
)

from os import listdir


async def birthday_loop(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Initiates the bot's checking cycle with 'job_queue'.

    Returns nothing.
    Raises no errors.
    """
    # "return to sender"
    target_chat = update.effective_message.chat_id
    message = text_responses.sechude_active()

    timezone = ZoneInfo(f'Etc/GMT+{TIME_HOUR_OFFSET}')
    job_time_first = time(
        hour=TIME_HOUR_FIRST,
        tzinfo=timezone,
    )
    job_time_second = time(
        hour=TIME_HOUR_SECOND,
        tzinfo=timezone,
    )

    # check if the database already exists
    # if not, then create one
    try:
        open('databases/' + str(target_chat) + '.txt', 'r').close()

    except FileNotFoundError:
        open('databases/' + str(target_chat) + '.txt', 'w').close()

    for target_chat in listdir('databases/'):
        try:
            # prevent repeating jobs
            current_jobs = context.job_queue.get_jobs_by_name(
                f'Morning Check on {target_chat}'
            )
        # possibly casused by user blocking the bot
        # caused by chat not being found
        except Forbidden:
            continue

        if current_jobs:
            message = text_responses.sechude_active_already()
            continue

        context.job_queue.run_daily(
            # what job to run
            callback=birthday_yell,
            time=job_time_first,
            chat_id=target_chat,
            name=f'Morning Check on {target_chat}',
        )

        # 'run_daily' allows to run only a single job
        # at a time so just invoke it a second time
        context.job_queue.run_daily(
            # what job to run
            callback=birthday_yell,
            time=job_time_second,
            chat_id=target_chat,
            name=f'Evening Check on {target_chat}',
        )

    # send a reply message to the user
    await context.bot.send_message(
        chat_id=target_chat,
        text=message,
    )


async def birthday_set(
    update: Update,
    _: ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Set a birthday date.

    Takes no arguments.

    If the user is already present in a database,
    tell the user their birthday date.

    If there's no such user,
    bring up a message with a keyboard for
    the user to enter their birthday date.

    Returns nothing.
    Raises no errors.
    """
    keyboard = bot_keyboards.months()
    message = text_responses.keyboard()
    username = update.effective_user.username
    target_chat = update.effective_chat.id

    session_functions.start(username)

    birthday_date = database_functions.search_by_name(
        username,
        target_chat,
    )
    if birthday_date:
        message = birthday_date
        keyboard = None

    await update.message.reply_text(
        text=message,
        reply_markup=keyboard,
    )


async def birthday_yell(
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    """
    text_responses.Celebrate a birth day!

    Takes no arguments.

    Checks for someone's birthday today,
    sends a message if someone has a birthday,
    does nothing if nobody has a birthday this day.

    Returns nothing.
    Raises no errors.
    """
    target_chat = context.job.chat_id
    today = datetime.now()
    # '%d.%m' == 'DD.MM' == 'Day.Month', ex.: '31.12'
    today_day_and_month = today.strftime('%d.%m')

    # investigating a strange error like of
    # 'Text should be a string, got NoneType'
    try:
        birthday_people = database_functions.search_by_date(
            today_day_and_month,
            target_chat,
        )
    except AttributeError:
        pass

    if birthday_people:
        await context.bot.send_message(
            chat_id=target_chat,
            text=text_responses.celebrate(birthday_people),
        )


async def birthday_rm(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Remove a birthday.

    Takes no arguments.

    Take a USER who called this function
    and check if they are in a database.

    If they are, remove their line from
    the database and aknowledge them of this.

    If they aren't, aknowledge them of this.

    Returns nothing.
    Raises no errors.
    """
    message = text_responses.remove_fail()
    username = update.effective_user.username
    target_chat = update.effective_chat.id

    target_line = database_functions.search_by_name(username, target_chat)

    if target_line:
        database_functions.remove(target_line, target_chat)
        message = text_responses.remove_success()

    await context.bot.send_message(
        # "return to sender"
        chat_id=target_chat,
        text=message,
    )


async def birthday_btn(
    update: Update,
    _: ContextTypes.DEFAULT_TYPE
) -> None:
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
    Raises no errors.
    """
    keyboard_select_month = (
        bot_keyboards.jan_feb_mar(),
        bot_keyboards.apr_may_jun(),
        bot_keyboards.jul_aug_sep(),
        bot_keyboards.oct_nov_dec(),
    )
    keyboard_select_day = (
        bot_keyboards.day_1_to_6(),
        bot_keyboards.day_7_to_12(),
        bot_keyboards.day_13_to_18(),
        bot_keyboards.day_19_to_24(),
        bot_keyboards.day_25_to_31(),
    )
    username = update.effective_user.username
    keyboard = bot_keyboards.months()
    message = text_responses.keyboard()

    # create, get and extract the user's input
    query = update.callback_query
    await query.answer()
    data = query.data

    session_data = session_functions.extract(username)
    step = int(session_data[0])

    # '[1]' (second parameter) is the button value
    if data == Control.back()[1]:
        if step > 2:
            step = 2
            keyboard = bot_keyboards.keyboard_days()
        else:
            step = 0

    # operation is done successfully
    elif data == Control.finish()[1]:
        message = text_responses.write_success()
        keyboard = None
        target_chat = update.effective_chat.id
        database_functions.write(username, target_chat)

    # operation is cancelled
    elif data == Control.abort()[1]:
        await query.delete_message()

    # don't get confused: those conditions apply
    # AFTER the button press
    elif step == 0:
        index = int(data)
        keyboard = keyboard_select_month[index]
        step += 1

    elif step == 1:
        # month
        session_data[2] = data + '\n'
        keyboard = bot_keyboards.keyboard_days()
        step += 1

    elif step == 2:
        index = int(data)
        keyboard = keyboard_select_day[index]
        step += 1

    elif step == 3:
        # day
        session_data[1] = data + '\n'
        message = text_responses.keyboard_final(
            username,
            session_data,
        )
        keyboard = bot_keyboards.final()

    session_data[0] = str(step) + '\n'
    session_functions.write(username, session_data)

    # try-except to suppress an expexted error message
    # when the message is deleted before editing
    # from flooding the logs
    try:
        await query.edit_message_text(
            text=message,
            reply_markup=keyboard,
        )
    except BadRequest:
        pass
