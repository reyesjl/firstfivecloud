# Generated by Django 4.2.3 on 2023-11-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0013_alter_team_rank"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="rank",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
