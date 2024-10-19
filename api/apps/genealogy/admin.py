from django.contrib import admin

from apps.genealogy.models import FamilyMember, Union


class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "surname",
        "sex",
        "birth_date",
        "is_dead",
        "user",
    )
    list_filter = ("sex", "is_dead", "user")
    search_fields = ("first_name", "surname", "user__email")
    filter_horizontal = ("parents", "source_files")
    date_hierarchy = "birth_date"
    ordering = ("surname", "first_name")

    fieldsets = (
        (None, {"fields": ("first_name", "surname", "sex", "user")}),
        ("Birth Information", {"fields": ("birth_date", "birth_location")}),
        (
            "Death Information",
            {"fields": ("is_dead", "death_date", "death_location")},
        ),
        ("Family Relations", {"fields": ("parents",)}),
        ("Additional Information", {"fields": ("source_files",)}),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")


class UnionAdmin(admin.ModelAdmin):
    list_display = ("parent_1", "parent_2", "union_date", "is_divorced")
    list_filter = ("is_divorced", "union_date")
    search_fields = (
        "parent_1__first_name",
        "parent_1__surname",
        "parent_2__first_name",
        "parent_2__surname",
    )
    filter_horizontal = ("source_files",)
    date_hierarchy = "union_date"
    ordering = ("-union_date",)

    fieldsets = (
        (None, {"fields": ("parent_1", "parent_2")}),
        ("Union Details", {"fields": ("union_date", "union_location")}),
        ("Divorce Details", {"fields": ("is_divorced", "divorce_date")}),
        ("Additional Information", {"fields": ("source_files",)}),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")


admin.site.register(FamilyMember, FamilyMemberAdmin)
admin.site.register(Union, UnionAdmin)
