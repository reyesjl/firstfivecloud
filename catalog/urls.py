from django.urls import path
from . import views

urlpatterns = [
    path("", views.handleCatalogRoute, name="catalog"),
    path("caps/", views.handleCapsRoute, name="caps"),
]
