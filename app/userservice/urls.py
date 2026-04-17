from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.sign_up, name="sign-up")
]