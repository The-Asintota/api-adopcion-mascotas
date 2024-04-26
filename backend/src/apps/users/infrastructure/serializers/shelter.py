from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from typing import Dict
from apps.users.infrastructure.db import UserRepository
from apps.users.infrastructure.schemas.shelter import ShelterSerializerSchema
from apps.users.domain.constants import UserRoles
from apps.utils import ErrorMessagesSpanishSerializer, ERROR_MESSAGES


@ShelterSerializerSchema
class ShelterSerializer(ErrorMessagesSpanishSerializer):
    """
    Defines the data required to register a shelter in the system.
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
        required=True,
        max_length=40,
        validators=[
            RegexValidator(
                regex=r"^([A-Za-z0-9]+[-_.])*[A-Za-z0-9]+@[A-Za-z]+(\.[A-Z|a-z]{2,4}){1,2}$",
                code="invalid_data",
                message=ERROR_MESSAGES["invalid"].format(
                    field_name="El correo electrónico"
                ),
            ),
        ],
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
    shelter_phone_number = PhoneNumberField(
        required=True,
        error_messages={
            "invalid": ERROR_MESSAGES["invalid"].format(
                field_name="El número de teléfono"
            ),
            "max_length": ERROR_MESSAGES["max_length"].format(
                field_name="El número de teléfono", max_length="{max_length}"
            ),
        },
        max_length=25,
    )
    shelter_name = serializers.CharField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
                field_name="El nombre", max_length="{max_length}"
            ),
        },
        required=True,
        max_length=50,
    )
    shelter_address = serializers.CharField(
        error_messages={
            "max_length": "La dirección no puede tener más de {max_length} caracteres.",
        },
        required=True,
        max_length=100,
    )
    shelter_responsible = serializers.CharField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=True,
        max_length=50,
    )
    shelter_logo = serializers.URLField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
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

    def validate_shelter_name(self, value: str) -> str:
        user = self._user_repository.get_profile_data(
            role=UserRoles.SHELTER.value,
            shelter_name=value,
        ).exists()

        if user:
            raise serializers.ValidationError(
                code="invalid_data",
                detail=ERROR_MESSAGES["name_in_use"],
            )

        return value

    def validate_shelter_responsible(self, value: str) -> str:
        user = self._user_repository.get_profile_data(
            role=UserRoles.SHELTER.value,
            shelter_responsible=value,
        ).exists()

        if user:
            raise serializers.ValidationError(
                code="invalid_data",
                detail="No se puede estar a cargo de más de un refugio.",
            )

        return value

    def validate_shelter_phone_number(self, value: str) -> str:
        user = self._user_repository.get_profile_data(
            role=UserRoles.SHELTER.value,
            shelter_phone_number=value,
        ).exists()

        if user:
            raise serializers.ValidationError(
                code="invalid_data",
                detail=ERROR_MESSAGES["phone_in_use"],
            )

        return value

    def validate_shelter_address(self, value: str) -> str:
        user = self._user_repository.get_profile_data(
            role=UserRoles.SHELTER.value,
            shelter_address=value,
        ).exists()

        if user:
            raise serializers.ValidationError(
                code="invalid_data",
                detail=ERROR_MESSAGES["address_in_use"],
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
