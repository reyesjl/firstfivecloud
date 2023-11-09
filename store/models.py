from django.db import models

# Create your models here.
class CapsInquiry(models.Model):
    email = models.EmailField()
    team_name = models.CharField(max_length=255)
    cap_base_color = models.CharField(max_length=50)
    cap_trim_color = models.CharField(max_length=50)
    cell_phone_number = models.CharField(max_length=15)
    number_of_caps = models.IntegerField()

    def __str__(self):
        return f"{self.team_name} - {self.email} - {self.number_of_caps}"
