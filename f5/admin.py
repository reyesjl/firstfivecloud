from django.contrib import admin
from .models import Team, Fixture

# Register model with application
admin.site.register(Team)
admin.site.register(Fixture)
