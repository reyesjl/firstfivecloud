from django.db import models

class Product(models.Model):
    """
    Represents a product.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight_oz = models.DecimalField(max_digits=8, decimal_places=2)
    images = models.ManyToManyField('ProductImage')

    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    """
    Represents an image for a product.
    """
    image = models.ImageField(upload_to='productmedia')

    def __str__(self):
        return self.image.name