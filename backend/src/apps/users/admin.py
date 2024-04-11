from django.contrib import admin
from .models import User, Shelter, JWT, JWTBlacklisted


class UserAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the User model.
    """

    list_display = (
        "uuid",
        "email",
        "password",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
        "last_login",
    )
    search_fields = (
        "uuid",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    )


class ShelterAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the Shelter model.
    """

    list_display = (
        "shelter_uuid",
        "base_user",
        "name",
        "address",
        "phone_number",
        "responsible",
        "logo_url",
        "data_joined",
    )
    search_fields = (
        "shelter_uuid",
        "base_user",
        "data_joined",
    )


class JWTAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the JWT model.
    """

    list_display = ("id", "user", "jti", "token", "date_joined", "expires_at")
    search_fields = ("user", "jti")


class JWTBlacklistedAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the JWTBlacklisted model.
    """

    list_display = ("id", "token", "date_joined")
    search_fields = ("token",)


admin.site.register(User, UserAdminPanel)
admin.site.register(Shelter, ShelterAdminPanel)
admin.site.register(JWT, JWTAdminPanel)
admin.site.register(JWTBlacklisted, JWTBlacklistedAdminPanel)
