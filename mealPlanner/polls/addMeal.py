from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils.datastructures import MultiValueDictKeyError


def add_meal(name):
    meal = Meal(meal_name=name)
    meal.save()
    