import pprint
import sys
import sqlite3
import json
import requests

def read_from_database():
    def show_results(rows):
        for row in rows:
            print(row)

    db = sqlite3.connect("food_search.db")
    cursor = db.cursor()

    cursor.execute('''
                SELECT * from recipes
            ''')

    rows = cursor.fetchall()

    #show_results(rows)

    db.commit()
    db.close()

    return rows

def check_database(ingredients, excludeIngredients):
    # Preparation of data from the database for comparison
    def convert(string):
        string = string.replace("[", "")
        string = string.replace("]", "")
        string = string.replace("'", "")
        li = list(string.split(","))
        return li

    db = sqlite3.connect("food_search.db")
    cursor = db.cursor()

    cursor.execute('''
                SELECT rowid, includeIngredients, excludeIngredients, recipe from ingredients
            ''')

    rows = cursor.fetchall()

    # Checking if the combination has already been used
    for row in rows:
        if row[1] == str(ingredients) and row[2] == str(excludeIngredients):
            return True, row[3]


    db.commit()
    db.close()
    return False


print(check_database(['tomato','cheese'], ['eggs']))