from django.db import models

class Inquiry(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  number = models.CharField(max_length=20)
  service = models.CharField(max_length=100)
  date = models.DateField(auto_now_add=True)
  status = models.BooleanField(default=False)

  def __str__(self):
      return self.name