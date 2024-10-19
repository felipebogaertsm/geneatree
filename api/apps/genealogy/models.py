from django.db import models

from apps.accounts.models import User


class FamilyMember(models.Model):
    SEX_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, blank=True)

    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)

    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    parents = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="children",
    )

    user = models.ForeignKey(
        User,
        related_name="family_members",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.surname}"


class Union(models.Model):
    parent_1 = models.ForeignKey(
        FamilyMember,
        related_name="union_as_parent_1",
        on_delete=models.CASCADE,
    )
    parent_2 = models.ForeignKey(
        FamilyMember,
        related_name="union_as_parent_2",
        on_delete=models.CASCADE,
    )

    union_date = models.DateField(blank=True, null=True)
    divorce_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.parent_1} & {self.parent_2} - {self.union_date or 'No marriage date'}"
