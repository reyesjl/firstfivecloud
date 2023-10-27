from django.contrib import admin
from .models import League, Team, Match, MatchEvent

# Register your models here.
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(MatchEvent)
