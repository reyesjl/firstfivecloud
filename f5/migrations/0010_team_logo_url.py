# Generated by Django 4.2.3 on 2023-09-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("f5", "0009_alter_team_image_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="logo_url",
            field=models.CharField(
                default="https://place-hold.it/250x250", max_length=100
            ),
        ),
    ]