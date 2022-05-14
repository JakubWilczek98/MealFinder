import pprint
import sqlite3
import json

def create_database():
    db = sqlite3.connect("food_search.db")
    cursor = db.cursor()

    try:
        cursor.execute('''DROP TABLE ingredients''')

        cursor.execute('''
            CREATE TABLE ingredients(
            includeIngredients string,
            excludeIngredients string,
            recipe integer
            )
        ''')
    except:
        cursor.execute('''
                    CREATE TABLE ingredients(
                    includeIngredients string,
                    excludeIngredients string,
                    recipe integer
                    )
                ''')

    try:
        cursor.execute('''DROP TABLE recipes''')

        cursor.execute('''
                CREATE TABLE recipes (
                recipe json
                )
            ''')
    except:
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
                SELECT recipe from recipes where rowid=15
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
    #create_database()
    #data = read_json_data()
    #add_to_database(data)
    data = read_from_database()
    #print()
    pprint.pprint(json.loads(data[0][0]))

