from teams.models import Team, League

# Delete all existing teams associated with the league
Team.objects.all().delete()
League.objects.all().delete()
