from django.contrib import admin

from .models import FamilyMember, Union, ParentChild


@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth", "death")


@admin.register(Union)
class UnionAdmin(admin.ModelAdmin):
    list_display = (
        "parent_1",
        "parent_2",
        "date_of_marriage",
        "date_of_divorce",
    )


@admin.register(ParentChild)
class ParentChildAdmin(admin.ModelAdmin):
    list_display = ("parent", "child", "union")
