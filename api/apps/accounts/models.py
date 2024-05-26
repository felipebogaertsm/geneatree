import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    """
    Custom user model for the application.

    Fields:
        _id: UUID field to uniquely identify the user.
        email: Email address of the user.
        company: ForeignKey to link the user to a company.
        is_active: Boolean field to indicate if the user is active or not.
        is_staff: Boolean field to indicate if the user is staff or not.
        is_admin: Boolean field to indicate if the user is admin or not.
        timestamp: DateTime field to indicate when the user was created.
    """

    _id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True, blank=True)
    is_staff = models.BooleanField(default=False, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        """Return a string representation of the user."""
        return str(self.email)
