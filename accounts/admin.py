from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from .forms import CustomUserCreatingForm, UserUpdateForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreatingForm
    form = UserUpdateForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)