# MealFinder

The program using given list of ingredients and the list of ingredients to exclude create html output of 4 meals. In the output also will be displayed:
* name of the meal,
* pictur,
* list of ingredients already present,
* list of missing ingredients,
* carbs,
* proteins,
* calories
* and some information about its composition.

The source of meals is  `https://spoonacular.com/food-api/`.

If someone wants to find meals with the same input as before the resulting meals data is store in a local database(SQLite).

## Run the script using main.py.
## Clear and create database using database_create.py.

## Required modules:
### pip install requests
### pip install pip install googletrans
### pip install pip install dominate

## Example output for ['bread', 'cheese', 'ham', 'eggs', 'chicken breast'] as ingredience and ingredients to exclude: ['cucumber'].
The output does not have styling, bootstrap was included for basic responsiveness and readability.


![food_search](https://user-images.githubusercontent.com/77202126/168466363-d5f792c3-e205-485e-a05f-fd8d2146a69d.png)
