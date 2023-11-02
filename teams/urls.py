from . import views
from django.urls import path

urlpatterns = [
  # Teams page route
  path("", views.handleTeamsRoute, name="teams"),
  path("all-american-pro/", views.handleAllAmericanProLeagueRoute, name="all-american-pro"),
  path("teamdetails/<str:team_name>", views.handleTeamDetailsRoute, name="teamdetails"),
  path("matches/", views.handleMatchesRoute, name="matches"),
]