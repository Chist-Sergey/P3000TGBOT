# core libraries for the bot to function
from telegram import (
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
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
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=INFO
)
