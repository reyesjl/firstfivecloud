from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.handleSignup, name="signup"),
    path("login", views.handleLogin, name="login"),
    path("logout", views.handleLogout, name="logout"),
]
