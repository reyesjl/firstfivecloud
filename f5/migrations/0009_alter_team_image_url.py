# Generated by Django 4.2.3 on 2023-09-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("f5", "0008_alter_team_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="image_url",
            field=models.CharField(
                default="https://place-hold.it/1200x500", max_length=100
            ),
        ),
    ]