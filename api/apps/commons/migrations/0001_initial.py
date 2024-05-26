# Generated by Django 5.0.6 on 2024-05-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Date",
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
                ("date", models.DateField(blank=True, null=True)),
                ("year", models.IntegerField(blank=True, null=True)),
                ("time", models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
