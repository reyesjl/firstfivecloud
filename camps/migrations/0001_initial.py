# Generated by Django 4.2.3 on 2023-07-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=200)),
                ("cost", models.DecimalField(decimal_places=2, max_digits=6)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("capacity", models.IntegerField()),
                ("attendees", models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name="EventRegistration",
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
                ("email", models.EmailField(max_length=254)),
                ("name", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=15)),
                (
                    "events",
                    models.ManyToManyField(
                        related_name="registrations", to="camps.event"
                    ),
                ),
            ],
        ),
    ]
