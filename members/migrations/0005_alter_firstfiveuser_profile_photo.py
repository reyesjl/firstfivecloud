# Generated by Django 4.2.3 on 2023-11-08 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0004_alter_firstfiveuser_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="firstfiveuser",
            name="profile_photo",
            field=models.CharField(
                blank=True, default="https://i.imgur.com/vuKfIWS.png"
            ),
        ),
    ]
