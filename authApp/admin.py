from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
class SimpleUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "role", "is_active")
    list_filter = ("role", "is_active")

    fieldsets = UserAdmin.fieldsets + (
        ("Role Information", {"fields": ("role",)}),
    )


# Register your models here.


admin.site.register(CustomUser, SimpleUserAdmin)
