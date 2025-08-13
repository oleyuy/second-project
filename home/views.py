from django.shortcuts import render
from django.http import HttpResponse
from .models import Anime
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import MyUser
# Create your views here.
def home(request):
    animes = Anime.objects.all()
    return render(request, "home/home.html", {'animes': animes})

def register_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if len(name) < 3 or len(name) > 15:
            return HttpResponse("Name must be between 3 and 15 characters long.")
        email = request.POST.get('email')
        # Check if email is available
        if MyUser.objects.filter(email=email).exists():
            return HttpResponse("Email already exists.")
        
        birth_year = request.POST.get('birth_year')
        # Ensure birth_year is an integer
        try:
            birth_year = int(birth_year)
            birth_year = max(1900, min(birth_year, 2023))  # correct range?
        except ValueError:
            return HttpResponse("Invalid birth year.")
        # Get the password from the form
        password = request.POST.get('password')
        if len(password) < 8:
            return HttpResponse("Password must be at least 8 characters long.")
        # validation of input
        if not name or not email or not birth_year or not password:
            return HttpResponse("All fields are required.")
        # Create a new user
        user = MyUser.objects.create_user(
            name=name,
            email=email,
            birth_year=birth_year,
            password=password
        )
        # Log the user in
        login(request, user)
        return redirect('home')
        
    return render(request, "account/register.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Validate the input
        if not email or not password:
            return HttpResponse("Email and password are required.")
        # Authenticate the user using the custom user model
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials")

    return render(request, "account/login.html")

def user_profile(request):
    # This is a placeholder for user profile logic
    # In a real application, you would retrieve user data from the database
    return render(request, "home/user_profile.html", {"username": request.user.name })