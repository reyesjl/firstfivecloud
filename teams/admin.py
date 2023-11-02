from django.contrib import admin
from .models import League, Team, Match, MatchEvent, Player, Roster

# Register your models here.
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(MatchEvent)
admin.site.register(Player)
admin.site.register(Roster)

