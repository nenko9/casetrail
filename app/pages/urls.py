from django.urls import path
from . import views


urlpatterns = [
    path("", views.root, name="root"),
    path("login", views.login, name="login"),
    path("documents", views.documents, name="documents"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
]