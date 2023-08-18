from django.contrib import admin
from .models import Event, EventInqueries, ToursInqueries

# Register your models here.
admin.site.register(Event)
admin.site.register(EventInqueries)
admin.site.register(ToursInqueries)
