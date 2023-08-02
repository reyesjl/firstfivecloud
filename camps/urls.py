from django.urls import path
from . import views

urlpatterns = [
    path("", views.handleCampsRoute, name="camps"),
]
