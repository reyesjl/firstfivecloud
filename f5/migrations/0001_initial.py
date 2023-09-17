# Generated by Django 4.2.3 on 2023-09-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=100)),
                ("history", models.TextField()),
                ("coach", models.CharField(max_length=100)),
                ("contact_email", models.EmailField(max_length=254)),
            ],
        ),
    ]