from django.urls import path
from . import views

urlpatterns = [
    path("", views.handleToursRoute, name="tours"),
    path("globetrotter", views.handleInsuranceRoute, name="globetrotter"),
]
