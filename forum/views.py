from django.shortcuts import render

def home(request):
    return render(request, "forum/home.html")

# Create your views here.
