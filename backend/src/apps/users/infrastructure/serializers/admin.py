from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from typing import Dict
from apps.users.infrastructure.db import UserRepository
from apps.users.domain.constants import UserRoles
from apps.users.endpoint_schemas.register_admin import GetSerializerSchema
from apps.utils import ErrorMessages, ERROR_MESSAGES


@GetSerializerSchema
class RegisterAdminSerializer(ErrorMessages):
    """
    Defines the data required to register a admin in the system.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._user_repository = UserRepository

    email = serializers.CharField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
                field_name="El correo electrónico", max_length="{max_length}"
            ),
        },
        validators=[
            RegexValidator(
                regex=r"^([A-Za-z0-9]+[-_.])*[A-Za-z0-9]+@[A-Za-z]+(\.[A-Z|a-z]{2,4}){1,2}$",
                code="invalid_data",
                message=ERROR_MESSAGES["invalid"].format(
                    field_name="El correo electrónico"
                ),
            ),
        ],
        required=True,
        max_length=40,
    )
    password = serializers.CharField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
                field_name="La contraseña", max_length="{max_length}"
            ),
            "min_length": ERROR_MESSAGES["min_length"].format(
                field_name="La contraseña", min_length="{min_length}"
            ),
        },
        required=True,
        write_only=True,
        style={"input_type": "password"},
        max_length=20,
        min_length=8,
    )
    confirm_password = serializers.CharField(
        required=True, write_only=True, style={"input_type": "password"}
    )
    admin_name = serializers.CharField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
                field_name="El nombre", max_length="{max_length}"
            ),
        },
        required=True,
        max_length=50,
    )

    def validate_password(self, value: str) -> str:
        try:
            validate_password(value)
        except ValidationError:
            if value.isdecimal():
                raise serializers.ValidationError(
                    code="invalid_data",
                    detail=ERROR_MESSAGES["password_no_upper_lower"],
                )
            raise serializers.ValidationError(
                code="invalid_data",
                detail=ERROR_MESSAGES["password_common"],
            )

        return value

    def validate_email(self, value: str) -> str:
        user = self._user_repository.get(email=value).exists()

        if user:
            raise serializers.ValidationError(
                code="invalid_data",
                detail=ERROR_MESSAGES["email_in_use"],
            )

        return value

    def validate_admin_name(self, value: str) -> str:
        user = self._user_repository.get_profile_data(
            role=UserRoles.ADMIN_USER.value,
            admin_name=value,
        ).exists()

        if user:
            raise serializers.ValidationError(
                code="invalid_data",
                detail=ERROR_MESSAGES["name_in_use"],
            )

        return value

    def validate(self, data: Dict[str, str]) -> Dict[str, str]:
        # Validate that the password and confirm_password fields match
        password = data["password"]
        confirm_password = data["confirm_password"]

        if not password == confirm_password:
            raise serializers.ValidationError(
                code="invalid_data",
                detail={
                    "confirm_password": [
                        ERROR_MESSAGES["password_mismatch"],
                    ]
                },
            )

        return data
