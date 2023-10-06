from django.contrib import admin
from .models import Team, Fixture, Product, Category, Event, EventTicket

# Register model with application
admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(EventTicket)
