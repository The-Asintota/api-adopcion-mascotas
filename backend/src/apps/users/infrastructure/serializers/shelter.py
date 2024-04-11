from rest_framework import serializers
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from phonenumber_field.serializerfields import PhoneNumberField
from django.core.exceptions import ValidationError
from typing import Dict
from apps.users.infrastructure.serializers.utils import ErrorMessages
from apps.users.infrastructure.serializers.constants import (
    COMMON_ERROR_MESSAGES,
)
from apps.users.infrastructure.db import UserRepository
from apps.exceptions import ResourceNotFoundError
from apps.users.endpoint_schemas.register_shelter import SerializerSchema


@SerializerSchema
class RegisterShelterSerializer(ErrorMessages):
    """
    Defines the data required to register a shelter in the system.
    """

    email = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El correo electrónico", max_length="{max_length}"
            ),
        },
        required=True,
        max_length=40,
        validators=[
            RegexValidator(
                regex=r"^([A-Za-z0-9]+[-_.])*[A-Za-z0-9]+@[A-Za-z]+(\.[A-Z|a-z]{2,4}){1,2}$",
                code="invalid_data",
                message=COMMON_ERROR_MESSAGES["invalid"].format(
                    field_name="El correo electrónico"
                ),
            ),
        ],
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
    phone_number = PhoneNumberField(
        required=True,
        error_messages={
            "invalid": COMMON_ERROR_MESSAGES["invalid"].format(
                field_name="El número de teléfono"
            ),
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El número de teléfono", max_length="{max_length}"
            ),
        },
        max_length=25,
    )
    shelter_name = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El nombre", max_length="{max_length}"
            ),
        },
        required=True,
        max_length=50,
    )
    address = serializers.CharField(
        error_messages={
            "max_length": "La dirección no puede tener más de {max_length} caracteres.",
        },
        required=True,
        max_length=100,
    )
    responsible = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=True,
        max_length=50,
    )
    logo_url = serializers.URLField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=False,
        max_length=200,
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
            _ = UserRepository.get_shelter(email=value)
        except ResourceNotFoundError:
            return value

        raise serializers.ValidationError(
            code="invalid_data",
            detail=COMMON_ERROR_MESSAGES["email_in_use"],
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
