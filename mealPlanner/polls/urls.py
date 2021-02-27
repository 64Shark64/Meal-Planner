from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.user_view, name='index'),
    path('ingredients/', views.ing_view, name='ingredients'),
    path('units/', views.unit_view, name='units'),
    path('shop-list/', views.list_view, name='shoplist'),
    path('<int:meal_id>/', views.meal_view, name='detail'),
]