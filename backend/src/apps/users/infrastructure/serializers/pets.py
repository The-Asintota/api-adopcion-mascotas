from rest_framework import serializers
from apps.users.infrastructure.serializers.utils import ErrorMessages
from apps.users.infrastructure.serializers.constants import (
    COMMON_ERROR_MESSAGES,
)
from apps.users.domain.constants import PET_TYPES, PET_SEX_TYPES
from apps.users.endpoint_schemas.register_pet import GetSerializerSchema


@GetSerializerSchema
class RegisterPetSerializer(ErrorMessages):
    """
    Defines the data required to register a pet in the system.
    """

    pet_name = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El nombre", max_length="{max_length}"
            ),
        },
        required=True,
        max_length=50,
    )
    pet_type = serializers.ChoiceField(
        required=True,
        error_messages={
            "invalid_choice": COMMON_ERROR_MESSAGES["invalid_choice"].format(
                input="{input}"
            ),
        },
        choices=PET_TYPES,
    )
    pet_sex = serializers.ChoiceField(
        required=True,
        error_messages={
            "invalid_choice": COMMON_ERROR_MESSAGES["invalid_choice"].format(
                input="{input}"
            ),
        },
        choices=PET_SEX_TYPES,
    )
    shelter = serializers.UUIDField(
        required=True,
        error_messages={"invalid": "{input} is not a valid UUID."},
    )
    pet_race = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=True,
        max_length=50,
    )
    pet_age = serializers.IntegerField(
        error_messages={
            "max_value": "Asegúrate que este valor sea menor o igual a {max_value}.",
            "min_value": "Asegúrate que este valor sea mayor o igual a {min_value}.",
            "invalid": COMMON_ERROR_MESSAGES["invalid"].format(
                field_name="El valor ingresado"
            ),
        },
        required=True,
        max_value=99,
        min_value=1,
    )
    pet_observations = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=False,
        max_length=200,
    )
    pet_description = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=False,
        max_length=200,
    )
    pet_image = serializers.URLField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=False,
        max_length=200,
    )
