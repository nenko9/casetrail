from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def login(request):
    return HttpResponse("Login page")