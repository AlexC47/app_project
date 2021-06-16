from django.contrib import admin
from users.models import AuthUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(AuthUser)
class AuthUserAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('first_name', 'last_name',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
