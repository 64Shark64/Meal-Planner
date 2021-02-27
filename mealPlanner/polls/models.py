import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# class MyUser(models.Model):
#     username = models.CharField(max_length=24)
#     password = models.CharField(max_length=30)

#     def __str__(self):
#         return self.username

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredient_name
    

class Unit(models.Model):
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.unit
    

class Meal(models.Model):
    # user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
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


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#     def __str__(self):
#         return self.question_text


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text