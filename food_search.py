import sys
import sqlite3
import json
import requests

#python food_search.py find_food 1 1

def find_food(ingredients, excludeIngredients):

    def add_to_ingredients_database(ingredients, excludeIngredients):
        db = sqlite3.connect("food_search.db")
        cursor = db.cursor()

        cursor.execute(
            "insert into ingredients values (?,?,?)",
            ["['tomato','cheese']", "['eggs']", 1]
        )

        db.commit()
        db.close()

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


        #Checking if the combination has already been used
        for row in rows:
            if convert(row[1]) == ingredients and convert(row[2]) == excludeIngredients:
                value = True
            else:
                value = False

        db.commit()
        db.close()

        return value

    def create_new_combination(ingredients, excludeIngredients):
        data = requests.get(
            "https://api.spoonacular.com/recipes/complexSearch?includeIngredients=tomato,cheese&excludeIngredients=eggs&fillIngredients=true&number=2&apiKey=499e83f1ec4c45b18cea15d1d236cd1b").json()

        db = sqlite3.connect("food_search.db")
        cursor = db.cursor()

        cursor.execute(
            "insert into recipes values (?)",
            [json.dumps(data)]
        )

        cursor.execute(
            "SELECT max(rowid) from recipes"
        )

        last_rowid = cursor.fetchall()

        cursor.execute(
            "insert into ingredients values (?,?,?)",
            [str(ingredients), str(excludeIngredients), last_rowid[0][0]]
        )

        db.commit()
        db.close()

        return last_rowid[0][0]

    print(create_new_combination(ingredients, excludeIngredients))

    #add_to_ingredients_database(ingredients, excludeIngredients)
    #print(check_database(ingredients, excludeIngredients))
    return ingredients, excludeIngredients



if __name__ == '__main__':
    #globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
    print(find_food(['tomato','cheese'], ['eggs']))


