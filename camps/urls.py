from django.urls import path
from . import views

urlpatterns = [
    path("", views.handleWelcome, name="camps"),
]
