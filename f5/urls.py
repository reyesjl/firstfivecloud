from django.urls import path

from . import views

urlpatterns = [
    # Root url 
    path("", views.handleHomeRoute, name="index"),

    # Catalog match
    path("catalog/", views.handleCatalogRoute, name="catalog"),

    # Camps match
    path("camps/", views.handleCampsRoute, name="camps"),

    # Tours match
    path("tours/", views.handleToursRoute, name="tours"),
]
    