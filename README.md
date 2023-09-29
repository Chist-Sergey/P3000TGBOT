# P30000TLBOT
Open-Source Telegram-bot for celebrating birthday dates.

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
    From the bot's folder directory, write in a console:
    "make {your_platform_here}"
    Options: mac, win, unx.

To stop the bot, press the combination of keys
while in a concole window:
    control + C

The DB consists of two columns: the username and a birthday date in formate DD:MM.

TODO (in order):
make the bot to announce when someone have a birthday
redesign the bot
add TODO command
add logging to commands
add exception handling to database being open
add remove command
/kogda_dr DATE to return multiple people
pytest
make so commands are not being send immideatly
docker-compose
get rid of makefile
make a wrapper for the results to look good
refactor code, separate function into folders
cut repetetive words in the code descriptions
