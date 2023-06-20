from django.db import models
from django.contrib.auth.models import AbstractUser

# my models imported here
from models.article import Article, ArticleImage
from models.product import Product, ProductImage
from models.camp import Camp, CampImage
from models.tour import Tour, TourImage

Article, ArticleImage
Product, ProductImage
Camp, CampImage
Tour, TourImage

