import sys
import sqlite3
import json

db = sqlite3.connect("food_search.db")

cursor = db.cursor()

cursor.execute('''
            SELECT rowid, ingr, recipe from ingredients
        ''')

rows = cursor.fetchall()

print(dict(rows[0][1]))

db.commit()
db.close()