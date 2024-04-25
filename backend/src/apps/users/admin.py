from django.contrib import admin
from .models import (
    User,
    ShelterProfile,
    AdminProfile,
    JWT,
    JWTBlacklist,
    Pet,
    PetType,
    PetSex,
)


class UserAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `User` model.
    """

    list_display = (
        "uuid",
        "email",
        "password",
        "profile",
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
        "profile",
    )


class ShelterProfileAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `ShelterProfile` model.
    """

    list_display = (
        "uuid",
        "shelter_name",
        "shelter_address",
        "shelter_phone_number",
        "shelter_responsible",
        "shelter_logo",
    )
    search_fields = ("uuid", "shelter_name")


class AdminProfileAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `AdminProfile` model.
    """

    list_display = (
        "uuid",
        "admin_name",
    )
    search_fields = ("uuid", "admin_name")


class JWTAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `JWT` model.
    """

    list_display = (
        "uuid",
        "user",
        "jti",
        "token",
        "date_joined",
        "expires_at",
    )
    search_fields = ("user", "jti")


class JWTBlacklistAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `JWTBlacklist` model.
    """

    list_display = ("token", "date_joined")
    search_fields = ("token",)


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


admin.site.register(User, UserAdminPanel)
admin.site.register(ShelterProfile, ShelterProfileAdminPanel)
admin.site.register(AdminProfile, AdminProfileAdminPanel)
admin.site.register(JWT, JWTAdminPanel)
admin.site.register(JWTBlacklist, JWTBlacklistAdminPanel)
admin.site.register(Pet, PetAdminPanel)
admin.site.register(PetType, PetTypeAdminPanel)
admin.site.register(PetSex, PetSexAdminPanel)
