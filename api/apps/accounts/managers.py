from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValidationError({"email": "The Email field must be set."})

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        # Ensure superuser fields are set correctly
        if extra_fields.get("is_staff") is not True:
            raise ValidationError(
                {"is_staff": "Superuser must have is_staff=True."}
            )
        if extra_fields.get("is_admin") is not True:
            raise ValidationError(
                {"is_admin": "Superuser must have is_admin=True."}
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValidationError(
                {"is_superuser": "Superuser must have is_superuser=True."}
            )

        return self.create_user(email, password, **extra_fields)
