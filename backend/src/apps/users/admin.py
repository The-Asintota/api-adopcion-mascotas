from django.contrib import admin
from .models import (
    BaseUser,
    Shelter,
    JWT,
    JWTBlacklist,
    AdminUser,
    Pet,
    PetType,
    PetSex,
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
        "base_user",
        "shelter_name",
        "shelter_address",
        "shelter_phone_number",
        "shelter_responsible",
        "shelter_logo",
    )
    search_fields = ("base_user",)


class AdminUserAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `AdminUser` model.
    """

    list_display = (
        "base_user",
        "admin_name",
    )
    search_fields = ("base_user",)


class JWTAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `JWT` model.
    """

    list_display = (
        "jwt_uuid",
        "user_uuid",
        "content_type",
        "jti",
        "token",
        "date_joined",
        "expires_at",
    )
    search_fields = ("user_uuid", "jti")


class JWTBlacklistAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `JWTBlacklist` model.
    """

    list_display = ("token_id", "date_joined")
    search_fields = ("token_id",)


class PetAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `Pet` model.
    """

    list_display = (
        "pet_uuid",
        "pet_type",
        "pet_sex",
        "shelter",
        "pet_name",
        "pet_race",
        "pet_age",
        "pet_observations",
        "pet_description",
        "pet_image",
        "date_joined",
    )
    search_fields = (
        "pet_uuid",
        "pet_type",
        "pet_sex",
        "shelter",
        "date_joined",
    )


class PetTypeAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `PetType` model.
    """

    list_display = (
        "id",
        "type",
        "date_joined",
    )
    search_fields = ("id",)


class PetSexAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `PetSex` model.
    """

    list_display = (
        "id",
        "sex",
        "date_joined",
    )
    search_fields = ("id",)


admin.site.register(BaseUser, BaseUserAdminPanel)
admin.site.register(Shelter, ShelterAdminPanel)
admin.site.register(AdminUser, AdminUserAdminPanel)
admin.site.register(JWT, JWTAdminPanel)
admin.site.register(JWTBlacklist, JWTBlacklistAdminPanel)
admin.site.register(Pet, PetAdminPanel)
admin.site.register(PetType, PetTypeAdminPanel)
admin.site.register(PetSex, PetSexAdminPanel)
