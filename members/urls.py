from . import views
from django.urls import path

urlpatterns = [
  path("signup/", views.handleSignupUser, name="signup"),
  path("login/", views.handleLoginUser, name="login"),
  path("logout/", views.handleLogoutUser, name="logout"),
]