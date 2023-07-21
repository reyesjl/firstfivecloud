from django.db import models

class Event(models.Model):
    """Model for events"""

    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    attendees = models.IntegerField(default=2)

    def __str__(self):
        return self.name


class EventInqueries(models.Model):
    """Model for event inqueries"""

    email = models.EmailField()
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    events = models.ManyToManyField(Event, related_name="inqueries")

    def __str__(self):
        return self.name