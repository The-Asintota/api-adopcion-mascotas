from rest_framework import serializers
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from typing import Dict
from apps.users.infrastructure.serializers.constants import (
    COMMON_ERROR_MESSAGES,
)
from apps.users.infrastructure.db import UserRepository
from apps.exceptions import ResourceNotFoundError
from apps.users.endpoint_schemas.register_admin import GetSerializerSchema
from apps.utils import ErrorMessages


@GetSerializerSchema
class RegisterAdminSerializer(ErrorMessages):
    """
    Defines the data required to register a admin in the system.
    """

    email = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El correo electrónico", max_length="{max_length}"
            ),
        },
        validators=[
            RegexValidator(
                regex=r"^([A-Za-z0-9]+[-_.])*[A-Za-z0-9]+@[A-Za-z]+(\.[A-Z|a-z]{2,4}){1,2}$",
                code="invalid_data",
                message=COMMON_ERROR_MESSAGES["invalid"].format(
                    field_name="El correo electrónico"
                ),
            ),
        ],
        required=True,
        max_length=40,
    )
    password = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="La contraseña", max_length="{max_length}"
            ),
            "min_length": COMMON_ERROR_MESSAGES["min_length"].format(
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
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
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
                    detail=COMMON_ERROR_MESSAGES["password_no_upper_lower"],
                )
            raise serializers.ValidationError(
                code="invalid_data",
                detail=COMMON_ERROR_MESSAGES["password_common"],
            )

        return value

    def validate_email(self, value: str) -> str:
        try:
            _ = UserRepository.get_admin(email=value)
        except ResourceNotFoundError:
            return value

        raise serializers.ValidationError(
            code="invalid_data",
            detail=COMMON_ERROR_MESSAGES["email_in_use"],
        )

    def validate_admin_name(self, value: str) -> str:

        try:
            _ = UserRepository.get_admin(admin_name=value)
        except ResourceNotFoundError:
            return value

        raise serializers.ValidationError(
            code="invalid_data",
            detail=COMMON_ERROR_MESSAGES["name_in_use"],
        )

    def validate(self, data: Dict[str, str]) -> Dict[str, str]:
        password = data["password"]
        confirm_password = data["confirm_password"]

        if not password == confirm_password:
            raise serializers.ValidationError(
                code="invalid_data",
                detail=COMMON_ERROR_MESSAGES["password_mismatch"],
            )

        return data
