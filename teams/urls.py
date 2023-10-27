from . import views
from django.urls import path

urlpatterns = [
  # Teams page route
  path("", views.handleTeamsRoute, name="teams"),
  path("leagues/<str:league_name>", views.handleTeamsInLeagueRoute, name="teams-in-league"),
  path("matches/", views.handleMatchesRoute, name="matches"),
]