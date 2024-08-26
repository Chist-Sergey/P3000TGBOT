## Instructions for the bot set-up:

-1. Create a Telegram bot or get a Telegram Bot Token.  
This can be done via [@BotFather](https://t.me/botfather) in Telegram.
0. Clone a repository on your computer:
        git clone --filter=tree:0 https://github.com/Chist-Sergey/P3000TLBOT
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