from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils.datastructures import MultiValueDictKeyError

from .models import Meal, Ingredient, MealIngredient, Unit
from .generate_list import generate

def user_view(request):
    if request.method == "POST":
        name = request.POST['newmeal']
        test = name.strip()
        if len(test) != 0:
            meal = Meal(meal_name=name)
            meal.save()
        return HttpResponseRedirect(reverse('polls:index'))
    

    meals = Meal.objects.order_by('meal_name')
    print(meals)

    return render(request, 'polls/index.html', {'alphabetical_meals_list':meals})

def list_view(request):
    meals = []
    for key, value in request.POST.items():
        try:
            value = int(value)
        except ValueError:
            continue
        
        meals.append(Meal.objects.get(pk=int(value)))
    ingredients = generate(meals)
    print(ingredients)

    return render(request, 'polls/shoppinglist.html', {"ingredient_list":ingredients})
    
    


def ing_view(request):
    if request.method == "POST":
        name = request.POST['newing']
        test = name.split()
        if len(test) != 0:
            ing = Ingredient(ingredient_name=name)
            ing.save()
        return HttpResponseRedirect(reverse('polls:ingredients'))
    

    ings = Ingredient.objects.order_by('ingredient_name')

    return render(request, 'polls/ingredients.html', {'ings':ings})       


def unit_view(request):
    if request.method == "POST":
        name = request.POST['newunit']
        test = name.split()
        if len(test) != 0:
            unit = Unit(unit=name)
            unit.save()
        return HttpResponseRedirect(reverse('polls:units'))
    

    un = Unit.objects.order_by('unit')

    return render(request, 'polls/units.html', {'units':un})       




def meal_view(request, meal_id):

    if request.method == "POST":
        qty = request.POST['qty']
        test = qty.split()
        if len(test) != 0:
            try:
                ingredient = request.POST['ingredient']
                unit = request.POST['unit']
                meal = Meal.objects.get(pk=meal_id)
                added_ingredient = MealIngredient(meal=meal, ingredient=Ingredient.objects.get(pk=ingredient), quantity=int(qty), unit=Unit.objects.get(pk=unit))
                added_ingredient.save()
            except MultiValueDictKeyError:
                pass
        return HttpResponseRedirect(reverse('polls:detail', args=(meal_id,)))

    try:
        ingredients = MealIngredient.objects.filter(meal=meal_id)
        alling = Ingredient.objects.all()
        allunits = Unit.objects.all()
        meal = Meal.objects.get(pk=meal_id)
    except MealIngredient.DoesNotExist:
        raise Http404("There is no such meal!")

    return render(request, 'polls/detail.html', {'meal':meal, 'mi':ingredients, 'ing':alling, 'units':allunits})
