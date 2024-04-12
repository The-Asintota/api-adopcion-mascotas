from django.contrib import admin
from .models import (
    BaseUser,
    Shelter,
    JWT,
    JWTBlacklist,
    AdminUser,
    Pet,
    TypePet,
)


class BaseUserAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `BaseUser` model.
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
    Admin panel configuration for the `Shelter` model.
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


class AdminUserAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `AdminUser` model.
    """

    list_display = (
        "admin_uuid",
        "base_user",
        "admin_name",
    )
    search_fields = ("admin_uuid", "base_user")


class JWTAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `JWT` model.
    """

    list_display = ("id", "user", "jti", "token", "date_joined", "expires_at")
    search_fields = ("user", "jti")


class JWTBlacklistAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `JWTBlacklist` model.
    """

    list_display = ("id", "token_id", "date_joined")
    search_fields = ("token_id",)


class PetAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `Pet` model.
    """

    list_display = (
        "pet_uuid",
        "type_pet",
        "shelter",
        "pet_name",
        "race",
        "age",
        "observations",
        "description",
        "image",
        "date_joined",
    )
    search_fields = ("pet_uuid", "type_pet", "shelter", "date_joined")


class TypePetAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `TypePet` model.
    """

    list_display = (
        "id",
        "type_name",
        "date_joined",
    )
    search_fields = ("id",)


admin.site.register(BaseUser, BaseUserAdminPanel)
admin.site.register(Shelter, ShelterAdminPanel)
admin.site.register(AdminUser, AdminUserAdminPanel)
admin.site.register(JWT, JWTAdminPanel)
admin.site.register(JWTBlacklist, JWTBlacklistAdminPanel)
admin.site.register(Pet, PetAdminPanel)
admin.site.register(TypePet, TypePetAdminPanel)
