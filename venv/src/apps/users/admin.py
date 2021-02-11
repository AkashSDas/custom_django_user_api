from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserProfile

# User model
User = get_user_model()


# Customizing the interface of User model in the Admin Page
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_active', 'is_staff', 'is_admin']
    list_filter = ['email']

    fieldsets = [
        [None, {'fields': ['email', 'password', ]}],
        # ['Personal Info', {'fields': ['username', ]}],
        ['Permissions', {'fields': ['is_active', 'is_staff', 'is_admin']}],
    ]

    add_fieldsets = [
        [
            None,
            {
                'classes': ['wide', ],
                'fields': ['email', 'password', 'confirm_password'],
            },
        ],
    ]

    search_fields = ['email', ]
    ordering = ['email', ]
    filter_horizontal = []


class UserProfileAdmin(admin.ModelAdmin):
    pass


# Registering User model and its interface in admin page
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
