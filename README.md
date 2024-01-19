# P30000TLBOT
Open-Source Telegram-bot for celebrating birthday dates.

Created using "python-telegram-bot"

Intended use: in a telegram group chat,
controlled using the bot's own commands.

Available commands:
    /start - first thing you have to type for the bot to begin being active.

    /ya_rodilsa - set up a birthday date.
    Examples:
        Set up your birthday to today:
            /ya_rodilsa
        Set up someone's birthday to today:
            /ya_rodilsa @birthday_person
        Set up someone's birthday to set date:
            /ya_rodilsa @birthday_person DD:MM
    
    /kogda_dr - look up a birthday date.
    Examples:
        Look up your birthday date:
            /kogda_dr
        Look up someone's birthday date:
            /kogda_dr @birthday_person
        Look up evey person whos birthday is matching the set date:
            /kogda_dr DD:MM


Instructions for the bot set-up:
    From the bot's folder directory, create a ".env" file, wirte to it the following text:
    "TG_BOT_TOKEN = ''".
    Paste your telegram bot key in the empty brackets.
    From the bot's folder directory, write in a console:
    "make {your_platform_here}"
    Options: mac, win, unx.

To stop the bot, press the combination of keys
while in a concole window:
    control + C

The DB consists of two columns: the username and a birthday date in a format 'DD.MM' (without apostrophes).

TODO (in order):
add blank files in the folders 'user_data', 'databases'
update this documentation
do something with this newline chaos!!
trim those ugle chat id's
take a look to use a different jobQueue option
docker-compose (on hold 'til I find a way to sign up)
migrate to a database
