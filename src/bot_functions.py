import telegram
import datetime
import zoneinfo
import os

import text_responses
import bot_keyboards
import session_functions
import database_functions
import button_manager
from main import BOT_OPTIONS


async def birthday_start(
    update: telegram.Update,
    context: telegram.ext.ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Initiates the bot's checking cycle with 'job_queue'.
    The bot then tries to resume any jobs it already has.

    Sends a message to the user, telling them the state of the job.

    The job has two states:
    1. Running first time - the chat was added to a database
    and the job have begun.
    2. Running already - nothing has changed.
    """
    target_chat = update.effective_message.chat_id
    message = text_responses.sechude_active()
    tz_offset = BOT_OPTIONS['time zone/offset']
    time_instances = BOT_OPTIONS['time of instance(s) in hours']
    tzinfo = zoneinfo.ZoneInfo(f'Etc/GMT{tz_offset}')
    job_times = [
        datetime.time(hour=x, tzinfo=tzinfo) for x in time_instances
    ]
    active_chats = os.listdir('databases/')

    try:
        open('databases/' + str(target_chat) + '.txt', 'r').close()
    except FileNotFoundError:
        open('databases/' + str(target_chat) + '.txt', 'w').close()

    for chat_id in active_chats:
        # guard: repeating jobs
        current_jobs = context.job_queue.get_jobs_by_name(chat_id)
        if current_jobs:
            message = text_responses.sechude_active_already()
            continue

        for time in job_times:
            context.job_queue.run_daily(
                # what job to run
                callback=birthday_tell,
                time=time,
                chat_id=target_chat,
                name=chat_id,
            )

    await context.bot.send_message(
        chat_id=target_chat,
        text=message,
    )


async def birthday_set(
    update: telegram.Update,
    _: telegram.ext.ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Set a birthday date.

    If the user is already present in a database,
    tell the user their birthday date.

    If there's no such user,
    bring up a message with a keyboard for
    the user to enter their birthday date.
    """
    target_chat = update.effective_chat.id
    username = update.effective_user.username
    message = text_responses.keyboard()
    keyboard = bot_keyboards.months()

    session_functions.start(username)

    birthday_date = database_functions.search_by_name(
        username, target_chat
    )
    if birthday_date:
        message = birthday_date
        keyboard = None

    await update.message.reply_text(
        text=message,
        reply_markup=keyboard,
    )


async def birthday_tell(
    context: telegram.ext.ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Celebrate a birth day!

    Checks for someone's birthday today.
    Sends a message if someone has a birthday.

    Does nothing if nobody have birthday this day.
    """
    target_chat = context.job.chat_id
    message = text_responses.celebrate(birthday_people)
    today = datetime.time.now()
    # '%d.%m' == 'DD.MM' == 'Day.Month', ex.: '31.12'
    today_day_and_month = today.strfdatetime.time('%d.%m')
    birthday_people = database_functions.search_by_date(
        today_day_and_month, target_chat)

    if birthday_people:
        await context.bot.send_message(
            chat_id=target_chat,
            text=message,
        )


async def birthday_remove(
    update: telegram.Update,
    context: telegram.ext.ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Remove a birthday.

    Take a USER who called this function
    and check if they are in a database.

    If they are, remove their line from
    the database and aknowledge them of this.

    If they aren't, aknowledge them of this.
    """
    target_chat = update.effective_chat.id
    username = update.effective_user.username
    message = text_responses.remove_fail()

    target_line = database_functions.search_by_name(
        username, target_chat)

    if target_line:
        database_functions.remove(target_line, target_chat)
        message = text_responses.remove_success()

    await context.bot.send_message(
        chat_id=target_chat,
        text=message,
    )


async def birthday_button(
    update: telegram.Update,
    _: telegram.ext.ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Input to set a birthday date.

    Allows the USER to change their birthday date
    by pressing buttons on the inline keyboard.

    If the operation was done successfully,
    tell that the operation was successful.

    If the operation wasn't done successfully,
    remove this bot's message.
    """
    # creating tuples to be able to index keyboards
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
    message = text_responses.keyboard()
    keyboard = bot_keyboards.months()

    # create, get and extract the user's input
    query = update.callback_query
    await query.answer()
    data = query.data

    session_data = session_functions.extract(username)
    # to be able to use numertic comparation,
    # 'step' must be a number
    step = int(session_data[0])

    if data == button_manager.Control.back()[1]:
        # from 'confirmation' to 'month select'
        if step > 2:
            step = 2
            keyboard = bot_keyboards.keyboard_days()
        # from 'day select' to 'month select'
        else:
            step = 0

    elif data == button_manager.Control.finish()[1]:
        target_chat = update.effective_chat.id
        message = text_responses.write_success()
        keyboard = None
        database_functions.write(username, target_chat)

    elif data == button_manager.Control.abort()[1]:
        await query.delete_message()

    # don't get confused: those conditions apply
    # AFTER the button press
    # '0' == 'select range of months from all 12 months'
    elif step == 0:
        index = int(data)
        keyboard = keyboard_select_month[index]
        step += 1

    # '1' == 'select 1 month from 3 months'
    elif step == 1:
        # month
        session_data[2] = data + '\n'
        keyboard = bot_keyboards.keyboard_days()
        step += 1

    # '2' == 'select range of days from all 31 days'
    elif step == 2:
        index = int(data)
        keyboard = keyboard_select_day[index]
        step += 1

    # '3' == 'select 1 day from 6 days'
    elif step == 3:
        # day
        session_data[1] = data + '\n'
        message = text_responses.keyboard_final(username, session_data)
        keyboard = bot_keyboards.final()

    session_data[0] = str(step) + '\n'
    session_functions.write(username, session_data)

    # BadRequest is expected
    # it's raised when the bot is trying to edit a deleted message
    try:
        await query.edit_message_text(
            text=message,
            reply_markup=keyboard,
        )
    except telegram.error.BadRequest:
        pass
