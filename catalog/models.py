from django.db import models
import uuid


def generate_sku():
    return str(uuid.uuid4())[:8]  # Adjust as needed


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="catalog/static/product_images", blank=True, null=True)
    inventory = models.IntegerField(default=0)
    sku = models.CharField(max_length=200, default=generate_sku, unique=True)
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.name


class WRSInqueries(models.Model):
    """Model for WRS inqueries"""

    email = models.EmailField()
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name