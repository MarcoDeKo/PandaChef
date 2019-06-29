from django.urls import path
from cookbook import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes", views.recipes, name="recipes"),
    path("ingredients", views.ingredients, name="ingredients"),
    path("kitchen", views.kitchen, name="kitchen"),
]