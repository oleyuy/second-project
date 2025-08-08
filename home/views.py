from django.shortcuts import render
from django.http import HttpResponse
from .models import Anime

def home(request):
    animes = Anime.objects.all()
    return render(request, "home/home.html", {'animes': animes})
# Create your views here.

def user_profile(request):
    # This is a placeholder for user profile logic
    # In a real application, you would retrieve user data from the database
    return render(request, "home/user_profile.html", {"username": "User001"})