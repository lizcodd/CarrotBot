# CarrotBot v1, SQLite 3 Backend
# Liz Codd, 3/12/17

import sqlite3, requests
from bs4 import BeautifulSoup

# A database to store the user's favorite recipes
class Fav_Recipes():

	def __init__(self, filename):
		self.db = sqlite3.connect(filename)
		self.cur = self.db.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS favs (name TEXT, link TEXT)")
		self.db.commit()

	def view(self):
		self.cur.execute("SELECT * FROM favs")
		rows = self.cur.fetchall()
		return rows

	# Only allow recipe to be added if it's not already in the database
	def insert(self, name, link):
		self.cur.execute("SELECT * FROM favs WHERE name=?", (name,))
		is_present = self.cur.fetchall()
		if not is_present and [name, link] != [None, None]:
			self.cur.execute("INSERT INTO favs VALUES(?, ?)", (name, link))
			self.db.commit()

	def delete(self, name):
		self.cur.execute("DELETE FROM favs WHERE name=?", (name,))
		self.db.commit()

	def __del__(self):
		self.db.close()

class All_Recipes():

	def __init__(self, filename):
		self.db = sqlite3.connect(filename)
		self.cur = self.db.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS recipes (name TEXT, link TEXT)")
		self.db.commit()

	def view(self):
		self.cur.execute("SELECT * FROM recipes")
		rows = self.cur.fetchall()
		return rows

	# Webscrapes purplecarrot.com to fill the database with recipes
	def scrape(self):
		num_recipes = 0
		# Clear out old data from the table
		self.cur.execute("DELETE FROM recipes")
		base_url = 'http://www.purplecarrot.com'
		# Go thru all pages of recipes and scrape them, then store results in the database
		for i in range(1, 100 + 1):
			r = requests.get(base_url + '/plant-based-recipes?page=' + str(i))
			c = r.content
			soup = BeautifulSoup(c, 'html.parser')
			recipes = soup.find_all('li', {'class':'col-md-3 col-sm-4'})
			if not recipes:
				break
			for recipe in recipes:
				link = base_url + recipe.find('a').get('href')
				name = recipe.find('img').get('title')
				# Store it in the database
				self.cur.execute("INSERT INTO recipes VALUES(?, ?)", (name, link))
				num_recipes += 1
		# Remove duplicates (Purple Carrot seems to have some duplicate recipe names but with different links)
		self.cur.execute("DELETE FROM recipes WHERE rowid NOT IN (SELECT MIN(rowid) FROM recipes GROUP BY name)")
		self.db.commit()
		return num_recipes

	
	def search(self, keywords):
		matches = []
		self.cur.execute("SELECT * FROM recipes")
		all = self.cur.fetchall()
		for row in all:
			missing_keyword = False
			for keyword in keywords:
				if keyword.lower() not in row[0].lower():
					missing_keyword = True
					break
			if not missing_keyword:
				matches.append(row)
		return matches

	def __del__(self):
		self.db.close()	