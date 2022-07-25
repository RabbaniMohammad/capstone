from turtle import settiltangle
from django.urls import path 
from . views import Auth, single, History

urlpatterns = [ 
    path("",Auth),
    path("single/<str:pk>", single),
    path("history", History)
]

