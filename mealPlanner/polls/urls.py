from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.user_view, name='index'),
    path('ingredients/', views.ing_view, name='ingredients'),
    path('<int:meal_id>/', views.meal_view, name='detail'),
    # path('making/', views.make_meal, name='making'),
    # path('login/', views.login_view, name='login'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
# from django.urls import path

# from . import views

# app_name = 'polls'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]