from django.db import models
import uuid
  
class Event(models.Model):
  """
  Record of an event users can attend.
  """

  CATEGORY_CHOICES = (
        ('pathways', 'Pathways'),
        ('festival', 'Festival'),
        ('camp', 'Camp'),
    )
  
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=50)
  description = models.TextField()
  hosted_by = models.CharField(default="First Five Rugby",max_length=50)
  location = models.CharField(max_length=100)
  date = models.DateField()
  time = models.TimeField()
  register_link = models.CharField(default="https://firstfiverugby.com/camps", max_length=100)
  logo_url = models.CharField(default="https://i.imgur.com/chO9gOg.png", max_length=100)
  category = models.CharField(default="camp", max_length=20, choices=CATEGORY_CHOICES)
  external_registration = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.title}, {self.date}, {self.hosted_by}"
  
class EventTicket(models.Model):
  """
  Event Registration
  """
  player_full_name = models.CharField(max_length=100)
  player_age = models.PositiveIntegerField()
  player_grade = models.CharField(max_length=50)
  parent_full_name = models.CharField(max_length=100)
  parent_email = models.EmailField()
  camp = models.ForeignKey(Event, on_delete=models.CASCADE)  # ForeignKey to link the signup to the camp
  risk_checkbox = models.BooleanField()

  def __str__(self):
      return f"{self.player_full_name} - {self.camp.title}"