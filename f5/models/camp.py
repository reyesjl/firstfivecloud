from django.db import models
from django.contrib.auth.models import AbstractUser

class Camp(models.Model):
    """
    Represents a rugby camp.
    """
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()
    times = models.CharField(max_length=255)
    coaches = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    images = models.ManyToManyField('CampImage')

    def __str__(self):
        return f"{self.title} ({self.location}) - {self.startdate} through {self.enddate} | Coaches: {self.coaches}"

class CampImage(models.Model):
    """
    Represents an image for a rugby camp.
    """
    image = models.ImageField(upload_to='campmedia')

    def __str__(self):
        return self.image.name