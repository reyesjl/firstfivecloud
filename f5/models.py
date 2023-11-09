from django.db import models
import uuid

from members.models import FirstfiveUser
  
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
  coach = models.ForeignKey(FirstfiveUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='coached_events')
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

  SCHOOL_GRADE_CHOICES = (
      ('1', '1st Grade'),
      ('2', '2nd Grade'),
      ('3', '3rd Grade'),
      ('4', '4th Grade'),
      ('5', '5th Grade'),
      ('6', '6th Grade'),
      ('7', '7th Grade'),
      ('8', '8th Grade'),
      ('9', '9th Grade'),
      ('10', '10th Grade'),
      ('11', '11th Grade'),
      ('12', '12th Grade'),
      ('C1', 'College 1st Year'),
      ('C2', 'College 2nd Year'),
      ('C3', 'College 3rd Year'),
      ('C4', 'College 4th Year'),
      ('None', 'None'),
    )
  
  player_full_name = models.CharField(max_length=100)
  player_age = models.PositiveIntegerField()
  player_grade = models.CharField(max_length=4, choices=SCHOOL_GRADE_CHOICES)
  parent_full_name = models.CharField(max_length=100)
  parent_email = models.EmailField()
  camp = models.ForeignKey(Event, on_delete=models.CASCADE)  # ForeignKey to link the signup to the camp
  risk_checkbox = models.BooleanField()

  def __str__(self):
      return f"{self.player_full_name} - {self.camp.title}"

  
