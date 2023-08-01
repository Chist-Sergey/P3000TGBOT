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
    WINDOWS OS:
        open a cmd console
        type in console the following commands (with no brackets):
            "git clone https://github.com/Chist-Sergey/P3000TLBOT"
            "cd P3000TLBOT"
            "python -m venv venv"
            "source venv/scripts/Activate"
            "pip install -r requirements.txt"
            "touch .env"
        fill up the ".env" file with your telegram bot key
        type in console:
            "python P3000.py"

    MAC/LINUX OS:
        open a cmd console
        type in console the following commands (with no brackets):
            "git clone https://github.com/Chist-Sergey/P3000TLBOT"
            "cd P3000TLBOT"
            "python3 -m venv venv"
            "source venv/bin/activate"
            "pip3 install -r requirements.txt"
            "touch .env"
        fill up the ".env" file with your telegram bot key
        type in console:
            "python3 P3000.py"
