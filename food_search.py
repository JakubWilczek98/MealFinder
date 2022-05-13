import sys
import sqlite3

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

    add_to_ingredients_database(ingredients,excludeIngredients)

    def check_database(ingredients, excludeIngredients):
        def show_results(rows):
            for row in rows:
                print(row)

        db = sqlite3.connect("food_search.db")
        cursor = db.cursor()

        cursor.execute('''
                    SELECT rowid, includeIngredients, excludeIngredients, recipe from ingredients
                ''')

        rows = cursor.fetchall()

        show_results(rows)
        for row in rows:
            if row[1] ==  and row[2] == excludeIngredients:
                result = 'True'
                return result
            else:
                result = 'False'

        return result

        #show_results(rows)


        db.commit()
        db.close()

    print(check_database(ingredients, excludeIngredients))






    return ingredients, excludeIngredients



if __name__ == '__main__':
    #globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
    print(find_food(['tomato','cheese'], ['eggs']))


