# Generated by Django 5.0.6 on 2024-10-19 21:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("commons", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FamilyMember",
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
                ("first_name", models.CharField(max_length=30)),
                ("surname", models.CharField(blank=True, max_length=30)),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("is_dead", models.BooleanField(default=False)),
                ("death_date", models.DateField(blank=True, null=True)),
                (
                    "sex",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "birth_location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="births",
                        to="commons.location",
                    ),
                ),
                (
                    "death_location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="deaths",
                        to="commons.location",
                    ),
                ),
                (
                    "parents",
                    models.ManyToManyField(
                        related_name="children", to="genealogy.familymember"
                    ),
                ),
                (
                    "source_files",
                    models.ManyToManyField(
                        blank=True,
                        related_name="family_members",
                        to="commons.fileattachment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="family_members",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Union",
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
                ("union_date", models.DateField(blank=True, null=True)),
                ("is_divorced", models.BooleanField(default=False)),
                ("divorce_date", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "parent_1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="union_as_parent_1",
                        to="genealogy.familymember",
                    ),
                ),
                (
                    "parent_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="union_as_parent_2",
                        to="genealogy.familymember",
                    ),
                ),
                (
                    "source_files",
                    models.ManyToManyField(
                        blank=True,
                        related_name="unions",
                        to="commons.fileattachment",
                    ),
                ),
                (
                    "union_location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="unions",
                        to="commons.location",
                    ),
                ),
            ],
        ),
    ]
