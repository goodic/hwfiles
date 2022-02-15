def ingredient_to_dict(ingredient):
    ingredient_list = ingredient.split("|")
    return {'ingredient_name': str(ingredient_list[0]), 'quantity': int(ingredient_list[1]), 'measure': str(ingredient_list[2][:-1])}

def make_dish(file):
    dish_name = file.readline()[:-1]
    if len(dish_name) == 0:
        return None
    ingredient_quant = int(file.readline())
    ingredient_list = []
    while ingredient_quant > 0:
        ingredient = file.readline()
        ingredient = ingredient_to_dict(ingredient)
        ingredient_list.append(ingredient)
        ingredient_quant -= 1
    devnull = file.readline() #буду рад узнать как удалять пустую строку правильно
    return {'name': dish_name, 'ingredients': ingredient_list}

def make_book(path):
    book = {}
    f = open(path, encoding="utf-8")
    while 1:
        dish = make_dish(f)
        if dish == None:
            return book
        book[dish['name']]=dish['ingredients']

path = "files/recipes.txt"
cook_book = make_book(path)
print(cook_book)