# Generated by Django 4.2.3 on 2023-09-06 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("f5", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_played", models.DateField()),
                (
                    "team_1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_1_matches",
                        to="f5.team",
                    ),
                ),
                (
                    "team_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_2_matches",
                        to="f5.team",
                    ),
                ),
            ],
        ),
    ]