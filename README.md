# CarrotBot
-----------

WHO & WHEN
----------

Liz Codd, 03/18/2017 <br>
lizcodd@gmail.com

NOTE, 12/14/2020: Purple Carrot has redesigned their website since 2017. While fun and useful at the time, this app is now non-functional and not worth updating as Purple Carrot has included a recipe search feature in their new design. Just leaving it up as an example of one of my first Python projects.

WHAT
----

A GUI database program (written with Python 3 using tkinter for the GUI, sqlite3 for the databases) to manage
webscraped recipes from PurpleCarrot.com.

WHY
---

PurpleCarrot.com keeps vasts archives of their past recipes (with new ones posted every week) but it is not searchable.
CarrotBot offers a way to harvest all those recipes into a locally created database (the file recipes.db is created upon
first startup of the program). After the database is created the user can then search for keywords in recipe titles.
The user can bookmark favorite recipes in a separate database (the file favs.db is also created upon first startup).
At any point the user can select a recipe and click 'Open in Browser' to view the recipe details link (ingredients, instructions, pics)
in a new tab of their default browser.

HOW
---
For Windows users, just download and run cb_frontend.exe (found in the dist folder).
Otherwise, cb_frontend.py is the main python file so run that. It imports cb_backend.py.

TIPS
---

1.) Click 'Update Database' to sync your local database with PurpleCarrot.com's archives (takes several seconds).
It is recommended to do this weekly as that is how often PurpleCarrot updates their recipes.

2.) Use the singular form of keywords to get more results (instead of searching for 'carrots' try 'carrot').
