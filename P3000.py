# core libraries for the bot to function
from telegram import (
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,  # adds commands to the bot
)

# importing custom text from a local text storage file
from text_responses import wakeup

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
    # how much we want to observe
    level=INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Displays a message on a /start command.
    Acts as the placeholder, because all bots
    have to have a 'start' command (I guess).

    This function returns nothing
    This function doesn't raise any errors.
    """

    # the bot's respond to the 'start' command
    await context.bot.send_message(
        chat_id=update.effective_chat.id,  # recipient
        text=wakeup(),
    )


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

    if anything goes wrong, send a message with "n/a"

    This function returns nothing.
    This function doesn't raise any errors.
    """

    # WIP
    pass


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

    If anything goes wrong, send a message with "n/a".

    This function returns nothing.
    This function doesn't raise any errors.
    """

    # WIP
    pass


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
