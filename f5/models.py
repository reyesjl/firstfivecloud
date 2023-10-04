from django.db import models
import uuid

class Team(models.Model):
  """
  Team model
  """
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  history = models.TextField()
  coach = models.CharField(max_length=100)
  contact_email = models.EmailField()
  division = models.CharField(default="open", max_length=100)
  image_url = models.CharField(default="https://shorturl.at/krW01", max_length=100)
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
  id = models.AutoField(primary_key=True)
  date_played = models.DateField()
  team_1 = models.ForeignKey(Team, related_name="team_1_matches", on_delete=models.CASCADE)
  team_2 = models.ForeignKey(Team, related_name="team_2_matches", on_delete=models.CASCADE)
  score_team_1 = models.IntegerField(default=0)
  score_team_2 = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.team_1.name} vs. {self.team_2.name} | {self.score_team_1}-{self.score_team_2} | {self.date_played}"

class Category(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
      return self.name
  
class Product(models.Model):
  """
  Record of a product from the store.
  """

  # Generate product number
  def generate_sku():
    return str(uuid.uuid4())[:8]  # Adjust as needed

  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  description = models.TextField()
  image_url = models.CharField(default="https://place-hold.it/500", max_length=200)
  category = models.ManyToManyField(Category) 
  price = models.DecimalField(max_digits=10, decimal_places=2)
  inventory = models.IntegerField(default=0)
  sku = models.CharField(max_length=200, default=generate_sku, unique=True)
  is_active = models.BooleanField(default=True)
  team_only = models.BooleanField(default=False)
  size = models.CharField(default="M", max_length=10)
  
  def __str__(self):
    return self.name
  
class Event(models.Model):
  """
  Record of an event users can attend.
  """
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=50)
  description = models.TextField()
  location = models.CharField(max_length=100)
  date = models.DateField()
  time = models.TimeField()

  def __str__(self):
    return self.title