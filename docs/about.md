## Features  

- Checks for birthday at the time of your like!  
- Easy controls. Has only two commands and they don't require any arguments!  
- Confidential. A personal birthday list for every group chat!  

## Available commands:  

    /ya_rodilsa - set up a birthday date.  
    /ya_rodilsa - look up a birthday date.  
    /ya_oshibsa - remove a record of a birthday date.  

    Examples (yes, it's that easy):  
    /ya_rodilsa  
    /ya_oshibsa  

## How it works  

On a prescribed time, the bot gets a current date by using 'datetime.now()',  
formats it to 'Day.Month', and then checks it against the dates in a database.  
The DB consists of two columns, the username and a birthday date,  
in a format: username DD.MM (example: Pozdravitel3000_bot 31.12)  

## Style  

Single brackets are preferred over double brackets.  
Following Google style, but not entirely.  
List of things ignored: E116, E117, W503, F523, F524.  
W504 is selected over W503.  
No variable typing because its looks good without it.  

## Story  

After 5 months, 5 days and 5 hours in development, hopefully,  
it has been worth the wait.  

The idea of this bot took place in a "21-school" group chat,  
at July 26th  2023, as a suggestion made by Maxim Liamkin,  
who also picked up a name for this bot - "Проздравитель 3000"  
("Pozdravitel" == Celebrator).  

I thought it would be a nice challenge for me to make this bot,  
so I have begun the development later that day.  

There were many ideas about how I should make this bot - in the bot  
constructor; continue the abandoned project of other developers;  
or I could make it myself from scratch.  

The original idea was overly complicated, yet in my eyes,  
it was the simplest bot design. Public tests have revealed to me flaws  
of my designs, and every time I thought of a new way how I can improve it.  

This version, in my opinion, is the best version I can make at the moment.  
I'm glad I made it so far. With the project being open-source,  
I hope it will save some headaches for the people who want to use it  
in their own way.  