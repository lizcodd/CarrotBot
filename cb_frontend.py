# CarrotBot v1, TKinter Frontend
# Liz Codd, 3/12/17

from tkinter import *
import cb_backend
import webbrowser, os

# Initialize databases
recipes = cb_backend.All_Recipes('recipes.db')
favs = cb_backend.Fav_Recipes('favs.db')
global selected_row
selected_row = [None, None]

# Color constants for easy color adjusting
PURPLE = '#AB73AB'
ORANGE = '#FFBD59'

# Callback functions for the button widgets
def clear(): # clear the entry widget
	e_terms.delete(0, END)

# Ask the recipe database to return only recipes matching at least one
# of the user's keywords (sorted with most matching keywords first) and display in listbox
def search():
	recipe_list.delete(0, END)
	terms_list = terms.get().split(', ')
	results = recipes.search(terms_list)
	for row in results:
		recipe_list.insert(END, row)
	if results:
		box_title.set('I found these matching Purple Carrot recipes:')
	else:
		box_title.set('Sorry, no Purple Carrot recipes matched your search...')

# Open a new browser tab with the url of the currently selected recipe
def open_in_browser():
	try:
		webbrowser.open_new_tab(selected_row[1])
	except TypeError:
		box_title.set('Please select a recipe first!')

# Display the favs database (user's bookmarked recipes) in the listbox
def view_favs():
	box_title.set('Favorite Recipes:')
	recipe_list.delete(0, END)
	for row in favs.view():
		recipe_list.insert(END, row)

# Add the recipe currently selected in the listbox to the favs database
# (if it's not already in there)
def add_to_favs():
	favs.insert(selected_row[0], selected_row[1])
	view_favs()

# Delete the recipe currently selected in the listbox from the favs database
def del_from_favs():
	favs.delete(selected_row[0])
	view_favs()

def select(event):
	# Handles a click event from the listbox by storing the clicked row
	# in a global variable so all functions can use it
	global selected_row
	index = recipe_list.curselection()
	selected_row = recipe_list.get(index)

def view_all():
	box_title.set('Here are all archived Purple Carrot recipes:')
	recipe_list.delete(0, END)
	for row in recipes.view():
		recipe_list.insert(END, row)

def update():
	msg.set("Please be patient while I sync my database with PurpleCarrot.com's archives...")
	box_title.set('Updating... This may take several seconds.')
	toggle_buttons() # disable all buttons
	window.update()
	num_recipes = recipes.scrape() # this takes several seconds
	view_all()
	msg.set("To search type a keyword or list of keywords separated by commas (e.g. broccoli, tofu)")
	box_title.set('The recipe database has been updated. There are %i available recipes!' % num_recipes)
	toggle_buttons() # enable all buttons

def toggle_buttons():
	# Toggle the state of all buttons together
	buttons = [b_search, b_clear, b_update, b_view_all, b_goto, b_view_favs, b_add_favs, b_del_favs]
	new_state=NORMAL
	if b_search['state'] == 'normal':
		new_state = DISABLED
	for button in buttons:
		button.config(state=new_state)

# Need this to fix pyinstaller --onefile issue...
if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

# Configure main window
window = Tk()
window.title("CARROTBOT version 1.0")
window.geometry('680x480')
window.configure(bg=PURPLE)

# Create widgets
img = PhotoImage(file='imgs/purple_carrots.gif')
l_logo = Label(window, image=img, borderwidth=0, highlightthickness=0)
l_logo.image = img
l_spacer_vert1 = Label(window, text="", width=3, bg=PURPLE)
l_spacer_vert2 = Label(window, text="", width=5, bg=PURPLE)
l_spacer_hor1 = Label(window, text="", bg=PURPLE)
l_spacer_hor2 = Label(window, text="", bg=PURPLE)
l_spacer_hor3 = Label(window, text="", bg=PURPLE)
l_title = Label(window, text="CARROTBOT", bg=PURPLE)
box_title = StringVar(); msg = StringVar()
l_box_title = Label(window, textvariable=box_title, bg=PURPLE)
l_msg = Label(window, textvariable=msg, width=70, anchor='w', bg=PURPLE)
l_cb_says = Label(window, text="CarrotBot says:", anchor='w', bg=PURPLE)
terms = StringVar()
e_terms = Entry(window, textvariable=terms, width=40, bg=ORANGE)
b_search = Button(window, text="Search", width=7, bg=ORANGE, command=search)
b_clear = Button(window, text="Clear", width=7, bg=ORANGE, command=clear)
b_update = Button(window, text="Update Database", bg=ORANGE, command=update)
b_view_all = Button(window, text="View All", width=12, bg=ORANGE, command=view_all)
b_goto = Button(window, text="Open in Browser", width=12, bg=ORANGE, command=open_in_browser)
b_add_favs = Button(window, text="Add to Favs", width=12, bg=ORANGE, command=add_to_favs)
b_del_favs = Button(window, text="Del from Favs", width=12, bg=ORANGE, command=del_from_favs)
b_view_favs = Button(window, text="View Favs", width=12, bg=ORANGE, command=view_favs)
recipe_list = Listbox(window, height=15, width=80, bg=ORANGE)
recipe_list.bind('<<ListboxSelect>>', select)
recipe_scroll = Scrollbar(window, bg=ORANGE)
recipe_list.configure(yscrollcommand=recipe_scroll.set)
recipe_scroll.configure(command=recipe_list.yview)

# Style widget text
l_title.config(font=('Helvetica', 28))
l_box_title.config(font=('Helvetica', 10))
l_msg.config(font=('Helvetica', 9, 'italic'))
l_cb_says.config(font=('Helvetica', 9, 'bold'))
e_terms.config(font=('Helvetica', 10))
b_search.config(font=('Helvetica', 10))
b_clear.config(font=('Helvetica', 10))
b_update.config(font=('Helvetica', 10))
b_view_all.config(font=('Helvetica', 10))
b_goto.config(font=('Helvetica', 10))
b_add_favs.config(font=('Helvetica', 10))
b_del_favs.config(font=('Helvetica', 10))
b_view_favs.config(font=('Helvetica', 10))


# Arrange widgets in window
l_logo.grid(row=1, column=9, pady=10)
l_spacer_vert1.grid(row=0, column=0, rowspan=10)
l_spacer_vert2.grid(row=0, column=7, rowspan=10)
l_spacer_hor1.grid(row=0, column=0, columnspan=6)
l_spacer_hor2.grid(row=3, column=0, columnspan=6)
l_spacer_hor3.grid(row=5, column=0, columnspan=6)
l_title.grid(row=1, column=2, columnspan=6)
l_cb_says.grid(row=2, column=1)
l_msg.grid(row=2, column=2, columnspan=8)
l_box_title.grid(row=6, column=1, columnspan=6)
e_terms.grid(row=4, column=1, columnspan=3)
b_search.grid(row=4, column=5)
b_clear.grid(row=4, column=6)
b_update.grid(row=4, column=9)
recipe_list.grid(row=7, column=1, columnspan=6, rowspan=5)
recipe_scroll.grid(row=7, column=7, rowspan=5, sticky='NS')
b_view_all.grid(row=7, column=9)
b_goto.grid(row=8, column=9)
b_view_favs.grid(row=9, column=9)
b_add_favs.grid(row=10, column=9)
b_del_favs.grid(row=11, column=9)


# On very first startup there will be no recipes in the database, so update it first
rows = recipes.view()
if not rows:
	update()
else:
	msg.set('Welcome back, my friend!')

# Show all recipes in the database on every startup
view_all()

window.mainloop()