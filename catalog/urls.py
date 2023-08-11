from django.urls import path
from . import views

urlpatterns = [
    path("", views.handleCatalogRoute, name="catalog"),
    path("wrs/", views.handleFetchWrs, name="wrs_catalog"),
    path("add_product/", views.handleAddProduct, name="add_product"),
    path("caps/", views.handleCaps, name="caps"),
]
