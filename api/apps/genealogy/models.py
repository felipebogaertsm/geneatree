from django.db import models

from apps.accounts.models import User
from apps.commons.models import Date


class FamilyMember(models.Model):
    SEX_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)

    birth = models.OneToOneField(
        Date,
        related_name="birth_family_member",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    death = models.OneToOneField(
        Date,
        related_name="death_family_member",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    parents = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="children",
        through="ParentChild",
    )

    user = models.ForeignKey(
        User,
        related_name="family_members",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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

    date_of_marriage = models.OneToOneField(
        Date,
        related_name="date_of_marriage_union",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date_of_divorce = models.OneToOneField(
        Date,
        related_name="date_of_divorce_union",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.parent_1} & {self.parent_2} - {self.date_of_marriage or 'No marriage date'}"


class ParentChild(models.Model):
    parent = models.ForeignKey(
        FamilyMember,
        related_name="child_set",
        on_delete=models.CASCADE,
    )
    child = models.ForeignKey(
        FamilyMember,
        related_name="parent_set",
        on_delete=models.CASCADE,
    )
    union = models.ForeignKey(
        Union,
        related_name="children",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.parent} -> {self.child}"
