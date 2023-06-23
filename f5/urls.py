from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # Rugby caps
    path("rugbycaps/", views.rugbycaps, name='rugbycaps'),
    
    # Catalog match
    path("catalog/", views.catalog, name="catalog"),
    
    # News match
    path('article/<int:id>/', views.article, name="article"),
    path("news/", views.news, name="news"),

    # Camps match
    path("camps/", views.camps, name="camps"),

    # Tours match
    path("tours/", views.tours, name="tours"),

    # Info match
    path("info/", views.info, name="info"),
]
