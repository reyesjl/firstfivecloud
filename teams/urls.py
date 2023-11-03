from . import views
from django.urls import path

urlpatterns = [
  # Teams page route
  path("", views.handleTeamsRoute, name="teams"),
  path("league/<int:league_id>", views.handleLeagueRoute, name="league"),
  path("team/<int:team_id>", views.handleTeamRoute, name="team"),
  path("roster/player-details/<int:player_id>", views.handlePlayerDetailsRoute, name="playerdetails"),
  path("matches/", views.handleMatchesRoute, name="matches"),
  path("matches/<int:match_id>", views.handleMatchDetailsRoute, name="matchdetails"),
]