from django.urls import path, re_path
from cookbook import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes", views.recipes, name="recipes"),
    path("ingredients", views.ingredients, name="ingredients")
]