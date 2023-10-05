# Generated by Django 4.2.3 on 2023-10-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("f5", "0021_event_logo_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="category",
            field=models.CharField(
                choices=[
                    ("pathways", "Pathways"),
                    ("festival", "Festival"),
                    ("camp", "Camp"),
                ],
                default="camp",
                max_length=20,
            ),
        ),
    ]
