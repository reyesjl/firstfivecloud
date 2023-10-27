from django.contrib import admin
from .models import Event, EventTicket

# Register model with application
admin.site.register(Event)
admin.site.register(EventTicket)
