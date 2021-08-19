from django.shortcuts import render

def home(request):
    return render(request, "forum/home.html")

def login(request):
    return render(request, "forum/login.html")

def signup(request):
    return render(request, "forum/signup.html")

# Create your views here.
