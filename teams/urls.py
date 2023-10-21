from . import views
from django.urls import path

urlpatterns = [
  # Teams page route
  path("", views.handleTeamsRoute, name="teams"),
  path("matches/", views.handleMatchesRoute, name="matches"),
]