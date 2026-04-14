
from django.urls import path
from . import views


urlpatterns = [
    path("", views.wellcome, name="wellcome"),
    path("login", views.login, name="login"),
]
