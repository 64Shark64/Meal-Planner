# Generated by Django 3.1.7 on 2021-02-27 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210227_1321'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
        migrations.RenameModel(
            old_name='Meals',
            new_name='Meal',
        ),
        migrations.RenameModel(
            old_name='MealsIngredients',
            new_name='MealIngredient',
        ),
    ]