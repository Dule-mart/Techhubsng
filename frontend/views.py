from django.shortcuts import render

# Create your views here.


def index(request):
    text = {
        "title" : "Home",
        "text": "this is the home page" 
    }
    return render(request, "frontend/home.html", text)

def login(request):
    ctx = {
        "title": "login"
    }
    return render(request, "frontend/login.html", ctx)