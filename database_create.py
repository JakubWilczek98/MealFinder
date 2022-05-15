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

if __name__ == '__main__':
    create_database()