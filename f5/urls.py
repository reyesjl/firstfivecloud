from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog/", views.catalog, name="catalog"),
    path("news/", views.news, name="news"),
    path("camps/", views.camps, name="camps"),
    path("tours/", views.tours, name="tours"),
    path("info/", views.info, name="info"),
]
