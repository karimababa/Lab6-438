from django.urls import path
from . import views

app_name = "main"   

urlpatterns = [
    path("home", views.home, name="home"),
    path("teams",views.teams, name="teams"),
    path("players",views.players, name="players")
    
]