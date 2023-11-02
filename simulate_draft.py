import random
from django.db.models import Q
from teams.models import Player, Team, Roster

# Delete all existing rosters
Roster.objects.all().delete()

# Get all players and teams
players = Player.objects.all()
teams = Team.objects.all()

# Create a pool of available players
available_players = list(players)
random.shuffle(available_players)

# Loop through teams and simulate the draft
for team in teams:
    # Check if the team already has a roster; if not, create one
    roster, created = Roster.objects.get_or_create(team=team)

    # Determine how many players to draft for this team (adjust as needed)
    starting_lineup_limit = 23
    reserve_limit = 25

    # Draft players for the starting lineup
    while (
        roster.starting_23.count() < starting_lineup_limit
        and roster.starting_23.count() + roster.reserves.count() < starting_lineup_limit + reserve_limit
        and available_players
    ):
        drafted_player = available_players.pop()
        if not Roster.objects.filter(Q(starting_23=drafted_player) | Q(reserves=drafted_player)).exists():
            roster.starting_23.add(drafted_player)
            drafted_player.team = team
            drafted_player.save()
            print(f"Drafted {drafted_player.first_name} {drafted_player.last_name} to {team.name} (Starting lineup)")

    # Draft players for the reserve list
    while (
        roster.reserves.count() < reserve_limit
        and roster.starting_23.count() + roster.reserves.count() < starting_lineup_limit + reserve_limit
        and available_players
    ):
        drafted_player = available_players.pop()
        if not Roster.objects.filter(Q(starting_23=drafted_player) | Q(reserves=drafted_player)).exists():
            roster.reserves.add(drafted_player)
            drafted_player.team = team
            drafted_player.save()
            print(f"Drafted {drafted_player.first_name} {drafted_player.last_name} to {team.name} (Reserve list)")

print("Draft completed.")