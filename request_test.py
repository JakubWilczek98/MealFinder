import requests
import pprint

if __name__ == '__main__':
    data = requests.get("https://api.spoonacular.com/recipes/complexSearch?includeIngredients=tomato,cheese&excludeIngredients=eggs&fillIngredients=true&number=2&apiKey=499e83f1ec4c45b18cea15d1d236cd1b").json()

    pprint.pprint(data)