from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Index world")

def wellcome(request):
    return render(request, "pages/wellcome.html")

def login(request):
    return render(request, "pages/login.html")
