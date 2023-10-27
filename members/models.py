from django.contrib.auth.models import AbstractUser
from django.db import models

class FirstfiveUser(AbstractUser):
  # Add your custom fields here, for example:
  bio = models.TextField(blank=True)
