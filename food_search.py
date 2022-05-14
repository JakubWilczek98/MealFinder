import pprint
import sys
import sqlite3
import json
import requests

#python food_search.py find_food 1 1

def find_food(ingredients, excludeIngredients):
    '''
    def add_to_ingredients_database(ingredients, excludeIngredients):
        db = sqlite3.connect("food_search.db")
        cursor = db.cursor()

        cursor.execute(
            "insert into ingredients values (?,?,?)",
            ["['tomato','cheese']", "['eggs']", 1]
        )

        db.commit()
        db.close()
    '''

    def check_database(ingredients, excludeIngredients):
        # Preparation of data from the database for comparison

        db = sqlite3.connect("food_search.db")
        cursor = db.cursor()

        cursor.execute('''
                    SELECT rowid, includeIngredients, excludeIngredients, recipe from ingredients
                ''')

        rows = cursor.fetchall()

        #Checking if the combination has already been used
        for row in rows:
            if row[1] == str(ingredients) and row[2] == str(excludeIngredients):
                return True, row[3]

        db.commit()
        db.close()

        return False, None

    def create_new_combination(ingredients, excludeIngredients):
        data = requests.get(
            f"https://api.spoonacular.com/recipes/complexSearch?includeIngredients={','.join([str(item) for item in ingredients])}&excludeIngredients={','.join([str(item) for item in excludeIngredients])}&fillIngredients=true&sort=min-missing-ingredients&addRecipeNutrition=true&number=2&apiKey=499e83f1ec4c45b18cea15d1d236cd1b").json()

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

    value, recipe_id = check_database(ingredients, excludeIngredients)

    if value == True:

        db = sqlite3.connect("food_search.db")
        cursor = db.cursor()

        cursor.execute(
            f"SELECT recipe from recipes where rowid={recipe_id}"
        )

        recipe = cursor.fetchall()

        db.commit()
        db.close()
        return ingredients, excludeIngredients, recipe

    else:
        last_rowid = create_new_combination(ingredients, excludeIngredients)
        db = sqlite3.connect("food_search.db")
        cursor = db.cursor()

        cursor.execute(
            f"SELECT recipe from recipes where rowid={last_rowid}"
        )

        recipe = cursor.fetchall()

        db.commit()
        db.close()

    return ingredients, excludeIngredients, recipe

    #print(create_new_combination(ingredients, excludeIngredients))
    #add_to_ingredients_database(ingredients, excludeIngredients)
    #print(check_database(ingredients, excludeIngredients))




if __name__ == '__main__':
    #globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
    recipe = json.loads(find_food(['tomato','cheese','onion'], ['eggs'])[2][0][0])
    pprint.pprint(recipe)

    for result in recipe['results']:
        print(result['title'],
              result['image'],
              result['missedIngredientCount'],
              result['usedIngredientCount'])

        print('USED:')
        for used_ingredience in result['usedIngredients']:
            print(used_ingredience['name'])

        print('MISSED:')
        for missed_ingredience in result['missedIngredients']:
            print(missed_ingredience['name'])


