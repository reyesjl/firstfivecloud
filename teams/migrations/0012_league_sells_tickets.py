# Generated by Django 4.2.3 on 2023-11-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0011_league_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="league",
            name="sells_tickets",
            field=models.BooleanField(default=False),
        ),
    ]