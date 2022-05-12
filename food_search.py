import sys
#python food_search.py find_food 1 1

def find_food(ingredients, bad_products):
    return ingredients, bad_products

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
