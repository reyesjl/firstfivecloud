# Generated by Django 4.2.3 on 2023-08-18 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("camps", "0003_alter_event_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(
                blank=True,
                default="static/images/baltimore.png",
                null=True,
                upload_to="images",
            ),
        ),
    ]
