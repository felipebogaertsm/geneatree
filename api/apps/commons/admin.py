from django.contrib import admin
from .models import Location, FileAttachment


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "city", "state", "country", "postal_code")
    list_filter = ("country", "state", "city")
    search_fields = (
        "street_address",
        "city",
        "state",
        "country",
        "postal_code",
    )
    ordering = ("country", "state", "city")


@admin.register(FileAttachment)
class FileAttachmentAdmin(admin.ModelAdmin):
    list_display = ("name", "file", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "description")
    ordering = ("-created_at",)
