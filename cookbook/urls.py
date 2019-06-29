from django.urls import path
from cookbook import views

urlpatterns = [
    path("", views.home, name="cookbook home"),
    path("<name>", views.item, name="cookbook home")
]