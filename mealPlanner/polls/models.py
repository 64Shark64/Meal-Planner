import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredient_name
    

class Unit(models.Model):
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.unit
    

class Meal(models.Model):
    meal_name = models.CharField(max_length=50)

    def __str__(self):
        return self.meal_name


class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.meal) + " "+str(self.ingredient)+" "+str(self.quantity)+str(self.unit)
