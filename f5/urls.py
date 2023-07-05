from django.urls import path

from . import views

urlpatterns = [
    # Root url 
    path("", views.handleHomeRoute, name="home"),

    # About match
    #path("about/", views.handleAboutRoute, name="about"),

    # Catalog match
    #path("catalog/", views.handleCatalogRoute, name="catalog"),

    # Camps match
    #path("camps/", views.handleCampsRoute, name="camps"),

    # Tours match
    #path("tours/", views.handleToursRoute, name="tours"),
]
    