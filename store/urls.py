from . import views
from django.urls import path

urlpatterns = [
  path("", views.handleStoreRoute, name="store"),
  path("caps/orderform/", views.handleCapsInquiry, name="capsorder"),
  path("caps/sucess/", views.handleCapsSuccess, name="success_caps"),
]