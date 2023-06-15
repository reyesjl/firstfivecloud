from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom User model with an additional 'role' field.
    Inherits from Django's AbstractUser.
    """
    ROLE_CHOICES = [
        ('coach', 'Coach'),
        ('user', 'User'),
    ]
    
    """
    The role of the user on the page.
    Available choices: 'admin', 'editor', 'user'.
    Default: 'user'.
    """
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user')
    
    def __str__(self):
        return self.username

class RugbyCamp(models.Model):
    """
    Represents a rugby camp.
    """
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()
    times = models.CharField(max_length=255)
    coaches = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ManyToManyField('CampImage')
    attendees = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f"{self.title} ({self.location}) - {self.startdate} through {self.enddate} | Coaches: {self.coaches}"
    
class CampImage(models.Model):
    """
    Represents the image for a camp.
    """
    image = models.ImageField(upload_to='apparel_images')

    def __str__(self):
        return self.image.name
    
class Tour(models.Model):
    """
    Represents a tour.
    """
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    season = models.CharField(max_length=255)
    image = models.ManyToManyField('TourImage')

    def __str__(self):
        return self.title

class TourImage(models.Model):
    """
    Represents an image for a tour.
    """
    image = models.ImageField(upload_to='tour_images')

    def __str__(self):
        return self.image.name
    
class Article(models.Model):
    """
    Represents an article.
    """
    title = models.CharField(max_length=255)
    small_description = models.TextField()
    body = models.TextField()
    images = models.ManyToManyField('ArticleImage')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

class ArticleImage(models.Model):
    """
    Represents an image for an article.
    """
    image = models.ImageField(upload_to='article_images')

    def __str__(self):
        return self.image.name

class Tag(models.Model):
    """
    Represents a tag for an article.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class ApparelProduct(models.Model):
    """
    Represents a product
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    images = models.ManyToManyField('ProductImage')

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    """
    Represents an image for a product.
    """
    image = models.ImageField(upload_to='apparel_images')

    def __str__(self):
        return self.image.name
    
class MOTD(models.Model):
    """
    Represents a message of the day!
    """
    page = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.message