from django.shortcuts import render, redirect
from django.db.models import Manager
from .models import Game

def platform(request):
    return render(request, 'third_task/platform.html')

def game_list(request):
    games = Game.objects.all()
    return render(request, 'third_task/games.html', {'games': games})

def cart(request):
    return render(request, 'third_task/cart.html')






