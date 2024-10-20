from django.db import models


class Location(models.Model):
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        parts = [
            self.street_address,
            self.city,
            self.state,
            self.country,
            self.postal_code,
        ]

        parts = [part for part in parts if part]
        return ", ".join(parts) if parts else "Unknown Location"


class FileAttachment(models.Model):
    file = models.FileField(upload_to="attachments")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
