# Generated by Django 4.2.3 on 2023-07-30 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="catalog/static/product_images/"
            ),
        ),
    ]
