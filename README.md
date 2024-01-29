# P30000TLBOT
Open-Source Telegram-bot for celebrating birthday dates.

Created using "python-telegram-bot"

Intended use: in a telegram group chat.

# Features
- Checks for birthday twice a day at the time of your like!
- Easy controls. Has only two commands and it doesn't require any arguments!
- Confidential. A personal birthday list for every chat!

# Available commands:
    /ya_rodilsa - set up a birthday date.
    /ya_rodilsa - look up a birthday date.
    /ya_oshibsa - remove a record of a birthday date

    Examples (yes, it's that easy):
    /ya_rodilsa
    /ya_oshibsa

# Instructions for the bot set-up:
    1. From the bot's folder directory, create a ".env" file.
    2. Wirte to it the following text:

        TOKEN = ''

    3. Paste your telegram bot key in the empty brackets.
        Example:

        TOKEN = '5553535420:AABBCDJtttx-xlXsb055qOFrTH1s-c6yM22'

    4. From the bot's folder directory, type in a console:

        python3 -m venv venv
        source venv/scripts/bin/Activate
        pip3 install -r requirements.txt
        python3 P3000.py
    
    5. In a Telegram app, add @Pozdravitel3000_bot to your telegram group.

    6. In your telegram group chat, send a message:

        /start@Pozdravitel3000_bot

To stop the bot, press the combination of keys
in a concole window, where the bot instance is running:
    control + C

# How it works
On time, the bot gets a current date by using 'datetime.now()', formats it to 'Day.Month' and then checks it against the dates in a database.

The DB consists of two columns: the username and a birthday date in a format: DD.MM (example: 31.12)

# TODO (in order):
Get rid of log spam when cancelling the message
docker-compose for it to do all the set up instead of the user (on hold 'til I find a way to sign up)
migrate to a database
