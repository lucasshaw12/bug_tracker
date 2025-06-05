from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Extend the existing UserAdmin class to use the new CustomUser model.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # What fields to display in list view
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "user_role",
        "team_name",
        "num_bugs_assigned",
        "is_staff",
        "is_superuser",
    )

    # What fields to use in the user edit form
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Info", {"fields": ("user_role", "team_name", "num_bugs_assigned")}),
    )

    # What fields to use when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra Info", {"fields": ("user_role", "team_name", "num_bugs_assigned")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
