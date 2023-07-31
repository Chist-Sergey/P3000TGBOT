# core libraries for the bot to function
from telegram import (
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,  # adds commands to the bot
)

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


async def birthday_set(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function takes up to two optional arguments.

    Using it without any argument will add THIS user as the
    birthday person and set their birthday day to TODAY.

    Using it with one argument (person) will add THAT user as the
    birthday person and set their birthday day to TODAY.

    Using it with two arguments (person, date) will add THAT user
    as the birthday person and set their birthday day to that DATE.

    This function returns nothing.
    This function doesn't raise any errors.
    """


if __name__ == '__main__':
    # setting up the bot
    application = ApplicationBuilder().token(getenv('TG_BOT_TOKEN')).build()

    # setting up the commands
    birthday_set_handler = CommandHandler('give_birth', birthday_set)

    # applying said commands for the bot to recognize them
    # POSITION MATTERS: the bot will check them in order of appearence
    application.add_handler(birthday_set_handler)

    # asking the server for anything new every couple of seconds
    application.run_polling(poll_interval=3.0)
