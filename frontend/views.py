from django.shortcuts import render

# Create your views here.


def index(request):
    text = {"text": "this is the home page" }
    return render(request, "frontend/home.html", text)