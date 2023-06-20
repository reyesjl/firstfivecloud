from django.db import models

class Article(models.Model):
    """
    Represents an article.
    """
    title = models.CharField(max_length=255)
    preview = models.TextField()
    body = models.TextField()
    images = models.ManyToManyField('ArticleImage')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

class ArticleImage(models.Model):
    """
    Represents an image for an article.
    """
    image = models.ImageField(upload_to='articlemedia')

    def __str__(self):
        return self.image.name

class Tag(models.Model):
    """
    Represents a tag for an article.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name