from django.contrib import admin
from users.models import AuthUser, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

# admin.site.unregister(AuthUser)
# admin.site.unregister(Profile)


@admin.register(AuthUser)
class AuthUserAdmin(BaseUserAdmin):
    ordering = ('id',)
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff')
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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ('user',)
    list_display = ('id', 'about', 'city', 'country', 'avatar')
    search_fields = ('city', 'country',)

    fieldsets = (
        (None, {'fields': ('city', 'country')}),
        (_('Personal info'), {'fields': ('about',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('about', 'city', 'country', 'avatar'),
        }),
    )


# admin.site.unregister(Profile)
