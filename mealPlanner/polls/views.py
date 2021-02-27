# from django.http import HttpResponse, HttpResponseRedirect

# from django.shortcuts import render, get_object_or_404

# from django.urls import reverse

# from .models import Question, Choice
 

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.views import generic

# from .models import Meals, Ingredients


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
   

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils.datastructures import MultiValueDictKeyError

from .models import Meal, Ingredient, MealIngredient, Unit
from .generate_list import generate

# class UserView(generic.ListView):
#     try:
#         name = request.POST['newmeal']
#         meal = Meal(meal_name=name)
#         meal.save()
#     except:
#         pass
#     template_name = 'polls/index.html'
#     context_object_name = 'alphabetical_meals_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         print(Meal.objects.order_by('meal_name'))
#         return Meal.objects.order_by('meal_name')


# def login_view(request):
#     return render(request, 'polls/login.html')

def user_view(request):
    if request.method == "POST":
        name = request.POST['newmeal']
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

    return render(request, 'polls/shoppinglist.html', {"ingredient_pairs":ingredients})
    
    


def ing_view(request):
    if request.method == "POST":
        name = request.POST['newing']
        ing = Ingredient(ingredient_name=name)
        ing.save()
        return HttpResponseRedirect(reverse('polls:ingredients'))
    

    ings = Ingredient.objects.order_by('ingredient_name')

    return render(request, 'polls/ingredients.html', {'ings':ings})       


def unit_view(request):
    if request.method == "POST":
        name = request.POST['newunit']
        unit = Unit(unit=name)
        unit.save()
        return HttpResponseRedirect(reverse('polls:units'))
    

    un = Unit.objects.order_by('unit')

    return render(request, 'polls/units.html', {'units':un})       




def meal_view(request, meal_id):

    if request.method == "POST":
        ingredient = request.POST['ingredient']
        unit = request.POST['unit']
        qty = request.POST['qty']
        meal = Meal.objects.get(pk=meal_id)
        added_ingredient = MealIngredient(meal=meal, ingredient=Ingredient.objects.get(pk=ingredient), quantity=int(qty), unit=Unit.objects.get(pk=unit))
        added_ingredient.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(meal_id,)))

    try:
        ingredients = MealIngredient.objects.filter(meal=meal_id)
        alling = Ingredient.objects.all()
        allunits = Unit.objects.all()
        meal = Meal.objects.get(pk=meal_id)
    except MealIngredient.DoesNotExist:
        raise Http404("There is no such meal!")

    return render(request, 'polls/detail.html', {'meal':meal, 'mi':ingredients, 'ing':alling, 'units':allunits})


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")