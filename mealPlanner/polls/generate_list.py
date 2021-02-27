
#Meals is a list of meals objects
#Returns a list of pairs consisting of ingredient name, qnty 
def generate(meals):
    shop_list = {} 
    for meal in meals:
        ingredients = MealIngredient.objects.filter(meal=meal) # get each ingredient belonging to a meal
        for ing in ingredients:   #add each ingredient to shopping list 
            key = ing.ingredient.ingredient_name+"###"+ ing.unit #key is ingredient name + unit (### for delimiter)
            shop_list.update({key:ing.quantity+shop_list.setdefault(key,0)})

    shopping = []
    for k,v in shop_list:
        name_unit = k.split("###")
        shopping.append((name_unit[0],v+name_unit[1]))
    return shopping

