# Generated by Django 4.2.3 on 2023-11-08 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0002_firstfiveuser_level_firstfiveuser_xp"),
    ]

    operations = [
        migrations.AddField(
            model_name="firstfiveuser",
            name="profile_photo",
            field=models.TextField(blank=True),
        ),
    ]