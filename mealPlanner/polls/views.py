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

from .models import Meal, Ingredient, MealIngredient

class UserView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'alphabetical_meals_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Meal.objects.order_by('meal_name')


class LoginView(generic.DetailView):
    template_name = 'polls/login.html'


def meal_view(request, meal_id):
    try:
        ingredients = MealIngredient.objects.filter(meal=meal_id)
        #ing = []
        #for tmp in ingredients:
         #   ing.append(Ingredient.objects.get(pk=tmp.))
        #print(ingredients)
        meal = Meal.objects.get(pk=meal_id)
        #print(meal)
    except MealIngredient.DoesNotExist:
        raise Http404("There is no such meal!")

    #return render(request, 'polls/detail.html', {'ingredients':ing, 'meal':meal})
    return render(request, 'polls/detail.html', {'mealname':meal, 'mi':ingredients})


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")