CarrotBot
Liz Codd, 03/18/2017
lizcodd AT gmail.com
----------

WHAT
----

A GUI database program (written with Python 3 and using tkinter for the GUI, sqlite3 for the databases) to manage
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
For Windows users, just download and run cb_frontend.exe (found in the dist folder)
Otherwise, cb_frontend.py is the main python file so run that. It imports cb_backend.py 

TIPS
---

1.) Click 'Update Database' to sync your local database with PurpleCarrot.com's archives (takes several seconds).
It is recommended to do this weekly as that is how often PurpleCarrot updates their recipes.

2.) Use the singular form of keywords to get more results (instead of searching for 'carrots' try 'carrot')
