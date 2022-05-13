import pprint
import sqlite3
import json

def create_database():
    db = sqlite3.connect("food_search.db")
    cursor = db.cursor()

    cursor.execute('''DROP TABLE ingredients''')

    cursor.execute('''
        CREATE TABLE ingredients(
        ingr string,
        recipe integer
        )
    ''')
    cursor.execute('''DROP TABLE recipes''')

    cursor.execute('''
            CREATE TABLE recipes (
            recipe json
            )
        ''')

    db.commit()
    db.close()

def add_to_database(data):
    db = sqlite3.connect("food_search.db")
    cursor = db.cursor()

    cursor.execute(
        "insert into recipes values (?)",
        [json.dumps(data)]
    )

    db.commit()
    db.close()

def read_from_database():
    def show_results(rows):
        for row in rows:
            print(row)

    db = sqlite3.connect("food_search.db")
    cursor = db.cursor()

    cursor.execute('''
                SELECT rowid, recipe from recipes
            ''')

    rows = cursor.fetchall()

    #show_results(rows)

    db.commit()
    db.close()

    return rows

def read_json_data():
    with open('recipe.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        return json_object

if __name__ == '__main__':
    create_database()
    data = read_json_data()
    add_to_database(data)
    data = read_from_database()
    #print(data)
    pprint.pprint(json.loads(data[0][1]))

