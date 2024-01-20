# P30000TLBOT
Open-Source Telegram-bot for celebrating birthday dates.

Created using "python-telegram-bot"

Intended use: in a telegram group chat.

Available commands:
    /ya_rodilsa - set up a birthday date.
    /ya_rodilsa - look up a birthday date.
    /ya_oshibsa - remove a record of a birthday date

    Examples (yes, it's that easy):
    /ya_rodilsa
    /ya_oshibsa

Instructions for the bot set-up:
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

To stop the bot, press the combination of keys
while in a concole window:
    control + C

The DB consists of two columns: the username and a birthday date in a format: DD.MM (example: 31.12)

TODO (in order):
add blank files in the folders 'user_data', 'databases'
make a valid makefile
do something with this newline chaos!!
trim those ugle chat id's
take a look to use a different jobQueue option
docker-compose (on hold 'til I find a way to sign up)
migrate to a database
