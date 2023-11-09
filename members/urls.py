from . import views
from django.urls import path

urlpatterns = [
  path("", views.handleMembersRoute, name="members"),
  path("profile/<str:username>", views.handleProfileRoute, name="profile"),
  path("profile/edit/<int:user_id>", views.handleEditProfileRoute, name="alterprofile"),
  path("signup/", views.handleSignupUser, name="signup"),
  path("login/", views.handleLoginUser, name="login"),
  path("logout/", views.handleLogoutUser, name="logout"),
  path("dashboard/", views.handleDashboardRoute, name="dashboard"),
]