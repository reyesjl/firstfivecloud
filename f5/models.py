from django.db import models

class Team(models.Model):
  """
    Team model
  """
  name = models.CharField(max_length=100)
  history = models.TextField()
  coach = models.CharField(max_length=100)
  contact_email = models.EmailField()
  division = models.CharField(default="open", max_length=100)
  image_url = models.CharField(default="https://place-hold.it/1200x500", max_length=100)
  logo_url = models.CharField(default="https://place-hold.it/250x250", max_length=100)
  register_url = models.CharField(default="usarugby.com", max_length=100);
  region = models.CharField(default="usa", max_length=100)
  zipcode = models.CharField(default="00000", max_length=100)

  def __str__(self):
    return self.name
  
class Fixture(models.Model):
  """
    Record of macth history.
  """
  date_played = models.DateField()
  team_1 = models.ForeignKey(Team, related_name="team_1_matches", on_delete=models.CASCADE)
  team_2 = models.ForeignKey(Team, related_name="team_2_matches", on_delete=models.CASCADE)
  score_team_1 = models.IntegerField(default=0)
  score_team_2 = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.team_1.name} vs. {self.team_2.name} | {self.score_team_1}-{self.score_team_2} | {self.date_played}"