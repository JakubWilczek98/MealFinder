import sqlite3

def database_operations():
    db = sqlite3.connect("food_search.db")
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE ingredients(
        id integer,
        ingr string
        )
    ''')

    db.commit()
    db.close()


if __name__ == '__main__':
    database_operations()