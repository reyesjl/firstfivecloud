from django.urls import path

from . import views

urlpatterns = [
    # Root url
    path("", views.handleHomeRoute, name="home"),
    # About match
    path("about/", views.handleAboutRoute, name="about"),
    # Success route
    path("success/", views.handleSuccessRoute, name="success"),
]
