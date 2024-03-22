# P30000TLBOT
Open-Source Telegram-bot for celebrating birthday dates.

Created using "python-telegram-bot"

Intended use: in a telegram group chat.

## Features
- Checks for birthday twice a day at the time of your like!
- Easy controls. Has only two commands and it doesn't require any arguments!
- Confidential. A personal birthday list for every group chat!

## Available commands:
    /ya_rodilsa - set up a birthday date.
    /ya_rodilsa - look up a birthday date.
    /ya_oshibsa - remove a record of a birthday date

    Examples (yes, it's that easy):
    /ya_rodilsa
    /ya_oshibsa

## Instructions for the bot set-up:
    1. From the bot's folder directory, create a ".env" file.
    2. Wirte to it the following text:

        TOKEN = ''

    3. Paste your telegram bot key in the empty brackets.
        Example:

        TOKEN = '5553535420:AABBCDJtttx-xlXsb055qOFrTH1s-c6yM22'

    4. From the bot's folder directory, type in a console:
    *For MacOS/Linux, use "python3" and "pip3" instead.*

        python -m venv venv
        source venv/scripts/bin/Activate
        pip install -r requirements.txt
        python P3000.py

    ***To stop the bot***, press the combination of keys:
        control + C

    5. In a Telegram app, add @Pozdravitel3000_bot to your telegram group.

    6. In your telegram group chat, send a message:

        /start@Pozdravitel3000_bot

### How it works
On a prescribed time, the bot gets a current date by using 'datetime.now()', formats it to 'Day.Month' and then checks it against the dates in a database.

The DB consists of two columns: the username and a birthday date in a format: username DD.MM
Example: Pozdravitel3000_bot 31.12

### TODO (in order):
docker-compose to do all the bot set up instead of the user (on hold 'til I find a way to sign up on Docker)
migrate to a database system like SQLite or Docker's innate PostgreSQL
