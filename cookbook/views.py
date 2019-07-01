from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(
        request,
        'cookbook/home.html'
    )

def ingredients(request):
    return render(
        request,
        'cookbook/ingredients.html'
    )

def recipes(request):
    return render(
        request,
        'cookbook/recipes.html'
    )

def kitchen(request):
    return render(
        request,
        'cookbook/kitchen.html'
    )

def shoppinglist(request):
    return render(
        request,
        'cookbook/shoppinglist.html'
    )