from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello world")

def wellcome(request):
    return HttpResponse("Wellcome page")

def login(request):
    return render(request, "pages/login.html")
