from django.contrib.auth.models import AbstractUser
from django.db import models

class FirstfiveUser(AbstractUser):
  # Add your custom fields here, for example:
  bio = models.TextField(blank=True)
  profile_photo = models.CharField(default="https://i.imgur.com/vuKfIWS.png")
  level = models.IntegerField(default="0")
  xp = models.IntegerField(default="0")