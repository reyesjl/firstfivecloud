from django.urls import path

from . import views

urlpatterns = [
    # Root url
    path("", views.handleDownRoute, name="home"),
    # About match
    path("about/", views.handleAboutRoute, name="about"),
    # Maintainence match
    path("down/", views.handleDownRoute, name="down"),
]
