# Generated by Django 4.2.3 on 2023-11-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("f5", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventticket",
            name="player_grade",
            field=models.CharField(
                choices=[
                    ("1", "1st Grade"),
                    ("2", "2nd Grade"),
                    ("3", "3rd Grade"),
                    ("4", "4th Grade"),
                    ("5", "5th Grade"),
                    ("6", "6th Grade"),
                    ("7", "7th Grade"),
                    ("8", "8th Grade"),
                    ("9", "9th Grade"),
                    ("10", "10th Grade"),
                    ("11", "11th Grade"),
                    ("12", "12th Grade"),
                    ("C1", "College 1st Year"),
                    ("C2", "College 2nd Year"),
                    ("C3", "College 3rd Year"),
                    ("C4", "College 4th Year"),
                    ("None", "None"),
                ],
                max_length=4,
            ),
        ),
    ]
