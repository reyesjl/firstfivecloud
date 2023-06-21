from django.contrib.auth.models import AbstractUser
from django.db import models

class F5user(AbstractUser):
    # Additional rugby player attributes
    email = models.EmailField(unique=True)
    is_player = models.BooleanField(default=False)
    cipp = models.CharField(max_length=8, unique=True, blank=True, null=True) 