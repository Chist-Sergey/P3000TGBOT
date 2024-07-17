(TODO: put release story there)

## Features

- Checks for birthday twice a day at the time of your like!
- Easy controls. Has only two commands and they don't require any arguments!
- Confidential. A personal birthday list for every group chat!

## Available commands:

    /ya_rodilsa - set up a birthday date.
    /ya_rodilsa - look up a birthday date.
    /ya_oshibsa - remove a record of a birthday date

    Examples (yes, it's that easy):
    /ya_rodilsa
    /ya_oshibsa

## How it works

On a prescribed time, the bot gets a current date
by using 'datetime.now()', formats it to 'Day.Month',
and then checks it against the dates in a database.

The DB consists of two columns, the username and a birthday date, in a format: username DD.MM
Example: Pozdravitel3000_bot 31.12

## Style

Single brackets are preferred over double brackets.
Following PEP8 style, except for function comments.
List of things ignored: E116, E117, W503, F523, F524.
W504 is preferred over W503.