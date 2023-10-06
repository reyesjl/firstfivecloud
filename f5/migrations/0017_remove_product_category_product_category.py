# Generated by Django 4.2.3 on 2023-09-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("f5", "0016_product_image_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(to="f5.category"),
        ),
    ]
