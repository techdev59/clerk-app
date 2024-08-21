from django.contrib import admin

from accounts.models import Organization, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    # Define the fields to be displayed in the admin interface
    list_display = ('email', 'user_id', 'first_name', 'last_name', 'is_staff', 'is_active',"user_organization")
    # Define the fields that can be searched in the admin interface
    search_fields = ('email', 'user_id', 'first_name', 'last_name')
    # Define the fields that can be used for filtering in the admin interface
    list_filter = ('is_staff', 'is_active', 'date_joined')

    fieldsets = (
        (None, {'fields': ('email', 'user_id', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('date_joined', 'last_login')}),
    )
    # Define the fieldsets for adding a new user in the admin interface
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_id', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active',"user_organization"),
        }),
    )
    # Define the ordering of users in the admin interface
    ordering = ('email',)
    # Define the titles of sections in the admin interface
    section_titles = {
        'Personal Info': 'User Information',
        'Permissions': 'User Permissions'
    }

# Register the User model with the CustomUserAdmin
admin.site.register(User, CustomUserAdmin)
admin.site.register(Organization)