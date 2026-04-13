from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello world")

def login(request):
    return render(request, "pages/login.html")
