import sqlite3
import json
import requests
import dominate
from dominate.tags import *
from googletrans import Translator

#python food_search.py find_food 1 1

def find_food(ingredients, excludeIngredients):
    def create_page(ingredience, excludeIngredients, recipe):
        translator = Translator()
        doc = dominate.document(title='food_search')
        with doc.head:
            link(rel="stylesheet", href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css")

        with doc:
            with div(cls='container'):
                h1('food_search:')
                hr()
                with div(cls='row'):
                    with div(cls='col'):
                        h4('Your ingredients:')
                        span(','.join([str(item) for item in ingredience]))
                    with div(cls='col'):
                        h4('Excluded ingredients:')
                        span(','.join([str(item) for item in excludeIngredients]))
                hr()
                with div(cls='results'):
                    for result in recipe['results']:
                        with div(cls='row'):
                            with div(cls='col'):
                                h2('Title: ', result['title'])
                                br()
                                h4('Parameters')
                                for parameter in result['nutrition']['nutrients']:
                                    if parameter['name'] == 'Calories':
                                        span(parameter['name'])
                                        span(parameter['amount'], parameter['unit'])
                                        br()
                                    if parameter['name'] == 'Protein':
                                        span(parameter['name'])
                                        span(parameter['amount'], parameter['unit'])
                                        br()
                                    if parameter['name'] == 'Carbohydrates':
                                        span(parameter['name'])
                                        span(parameter['amount'], parameter['unit'])
                                        br()
                                br()
                                h4('Missed ingredient count: ', result['missedIngredientCount'])

                                h4('Missed ingredients list:')
                                for missed_ingredience in result['missedIngredients']:
                                    li(span(missed_ingredience['name']), span(translator.translate(missed_ingredience['name'], dest='pl').text))
                                br()
                                h4('Used ingredient count: ', result['usedIngredientCount'])
                                h4('Used ingredients list:')
                                for used_ingredience in result['usedIngredients']:
                                    li(used_ingredience['name'])
                            with div(cls='col'):
                                img(src=result['image'])
                        hr()
            script(src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js")
            script(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js")
            script(src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js")

        return doc

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
            f"https://api.spoonacular.com/recipes/complexSearch?includeIngredients={','.join([str(item) for item in ingredients])}&excludeIngredients={','.join([str(item) for item in excludeIngredients])}&fillIngredients=true&sort=min-missing-ingredients&addRecipeNutrition=true&number=4&apiKey=499e83f1ec4c45b18cea15d1d236cd1b").json()

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

        recipe = json.loads(recipe[0][0])

        doc = create_page(ingredients, excludeIngredients, recipe)

        db.commit()
        db.close()
        return doc

    else:
        last_rowid = create_new_combination(ingredients, excludeIngredients)
        db = sqlite3.connect("food_search.db")
        cursor = db.cursor()

        cursor.execute(
            f"SELECT recipe from recipes where rowid={last_rowid}"
        )

        recipe = cursor.fetchall()

        recipe = json.loads(recipe[0][0])

        doc = create_page(ingredients, excludeIngredients, recipe)

        db.commit()
        db.close()
        return doc

if __name__ == '__main__':
    print(find_food(['tomato','eggs','pasta'], ['plum']))


