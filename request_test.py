import requests
import pprint
import json

def save_json_data(data):
    json_object = json.dumps(data, indent=4)
    with open("recipe.json", "w") as outfile:
        outfile.write(json_object)


if __name__ == '__main__':
    data = requests.get("https://api.spoonacular.com/recipes/complexSearch?includeIngredients=tomato,cheese&excludeIngredients=eggs&fillIngredients=true&number=2&apiKey=499e83f1ec4c45b18cea15d1d236cd1b").json()
    save_json_data(data)
    pprint.pprint(data)