from django.contrib import admin

from .models import FamilyMember, Union


@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    pass


@admin.register(Union)
class UnionAdmin(admin.ModelAdmin):
    pass
