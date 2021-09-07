from django.contrib import admin
from userapp.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserAdmin(UserAdmin):
    ordering = ("-date_joined",)
    search_fields = ('username', 'email')
    list_display = ('email', 'username', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        ("Login Info", {'fields': ('email', 'username', 'password',)}),
        ('permission', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')})
    )
    # exclude = ('date_joined',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )


admin.site.register(User, UserAdmin)
