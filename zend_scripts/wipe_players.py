from teams.models import Roster, Player

# Delete all existing rosters
Roster.objects.all().delete()
Player.objects.all().delete()

