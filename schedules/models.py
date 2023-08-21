from django.db import models

# Create your models here.
class LocalEvent(models.Model):
    """Model for events"""
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to="schedules/static/images", blank=True, null=True
    )
    description = models.TextField()
    location = models.CharField(max_length=200)
    event_date = models.DateField()
    event_type = models.CharField(max_length=100)
    event_time = models.CharField(max_length=50)
    home_team = models.CharField(max_length=200)
    away_team = models.CharField(max_length=200)
    home_score = models.IntegerField(default=0)
    away_Score = models.IntegerField(default=0)
  
    def __str__(self):
        return self.name