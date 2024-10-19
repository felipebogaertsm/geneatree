from django.db import models
from django.utils import timezone

from apps.accounts.models import User
from apps.commons.models import FileAttachment, Location


class FamilyMember(models.Model):
    SEX_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, blank=True)

    birth_date = models.DateField(blank=True, null=True)
    birth_location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="births",
    )

    is_dead = models.BooleanField(default=False)
    death_date = models.DateField(blank=True, null=True)
    death_location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="deaths",
    )

    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    parents = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="children",
        blank=True,
    )

    user = models.ForeignKey(
        User,
        related_name="family_members",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    source_files = models.ManyToManyField(
        FileAttachment,
        related_name="family_members",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

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
    union_location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="unions",
    )

    is_divorced = models.BooleanField(default=False)
    divorce_date = models.DateField(blank=True, null=True)

    source_files = models.ManyToManyField(
        FileAttachment,
        related_name="unions",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.parent_1} & {self.parent_2} - {self.union_date or 'No marriage date'}"
