from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(
        request,
        'cookbook/home.html'
    )

def item(request, name):
    return render(
        request,
        'cookbook/item.html',
        {
            'name': name
        }
    )