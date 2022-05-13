import sqlite3
import json

def create_database():
    db = sqlite3.connect("food_search.db")
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE ingredients(
        id integer,
        ingr string,
        recipe integer
        )
    ''')

    cursor.execute('''
            CREATE TABLE recipes(
            id integer,
            recipe json
            )
        ''')

    db.commit()
    db.close()

def add_to_database():
    db = sqlite3.connect("food_search.db")
    cursor = db.cursor()

    cursor.execute(
        "insert into ingredients values (?,?,?)",
        [1, "['apple','pear']", 1]
    )

    db.commit()
    db.close()

def read_from_database():
    db = sqlite3.connect("food_search.db")
    cursor = db.cursor()

    cursor.execute('''
                SELECT * from ingredients
            ''')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.commit()
    db.close()

if __name__ == '__main__':
    create_database()
    #add_to_database()
    #read_from_database()
