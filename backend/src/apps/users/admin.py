from django.contrib import admin
from .models import BaseUser, Shelter, JWT, JWTBlacklist


class BaseUserAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the BaseUser model.
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
        "shelter_name",
        "address",
        "phone_number",
        "responsible",
        "logo_url",
    )
    search_fields = ("shelter_uuid", "base_user")


class JWTAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the JWT model.
    """

    list_display = ("id", "user", "jti", "token", "date_joined", "expires_at")
    search_fields = ("user", "jti")


class JWTBlacklistAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the JWTBlacklist model.
    """

    list_display = ("id", "token_id", "date_joined")
    search_fields = ("token_id",)


admin.site.register(BaseUser, BaseUserAdminPanel)
admin.site.register(Shelter, ShelterAdminPanel)
admin.site.register(JWT, JWTAdminPanel)
admin.site.register(JWTBlacklist, JWTBlacklistAdminPanel)
