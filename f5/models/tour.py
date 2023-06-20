from django.db import models

class Tour(models.Model):
    """
    Represents a tour.
    """
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    season = models.CharField(max_length=255)
    image = models.ManyToManyField('TourImage')

    def __str__(self):
        return self.title

class TourImage(models.Model):
    """
    Represents an image for a tour.
    """
    image = models.ImageField(upload_to='tourmedia')

    def __str__(self):
        return self.image.name