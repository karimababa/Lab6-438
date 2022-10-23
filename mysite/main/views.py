from django.shortcuts import render
from .forms import PlayerForm, TeamForm
from .models import Player, Team

def home(request):
  return render(request, "home.html")

def teams(request):
  if request.method == "POST":
    form = TeamForm(request.POST)
    if form.is_valid():
      form.save()
  teams = Team.objects.all()
  form = TeamForm()
  return render(request, "teams.html", {"form": form, "teams": teams})

def players(request):
  if request.method == "POST":
    form = PlayerForm(request.POST)
    if form.is_valid():
      form.save()
  players = Player.objects.all()
  form = PlayerForm()
  return render(request, "players.html", {"form": form, "players": players})