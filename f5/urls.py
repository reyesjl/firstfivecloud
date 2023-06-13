from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("catalog/", views.catalog, name="catalog"),
    path("news/", views.news, name="news"),
    path("camps/", views.camps, name="camp"),
    path("tours/", views.tours, name="tours"),
    path("help/", views.help, name="help")
]
