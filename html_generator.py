import dominate
from dominate.tags import *
import pprint
import sys
import sqlite3
import json
import requests

def create_page(ingredience, excludeIngredients, recipe):
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
                                    br ()
                                if parameter['name'] == 'Carbohydrates':
                                    span(parameter['name'])
                                    span(parameter['amount'], parameter['unit'])
                                    br()
                            br()
                            h4('Missed ingredient count: ', result['missedIngredientCount'])

                            h4('Missed ingredients list:')
                            for missed_ingredience in result['missedIngredients']:
                                li(missed_ingredience['name'])
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

    with open("index.html", "w") as html_file:
        html_file.write(str(doc))
        print("Html file created")

    print(doc)

db = sqlite3.connect("food_search.db")
cursor = db.cursor()

cursor.execute(
    "SELECT recipe from recipes where rowid=1"
)

recipe = cursor.fetchall()

db.commit()
db.close()

recipe = json.loads(recipe[0][0])

create_page(['tomato','cheese'], ['eggs'], recipe)