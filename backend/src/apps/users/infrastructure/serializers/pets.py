from rest_framework import serializers
from apps.users.infrastructure.serializers.utils import ErrorMessages
from apps.users.infrastructure.serializers.constants import (
    COMMON_ERROR_MESSAGES,
)
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
    type_pet = serializers.ChoiceField(
        required=True,
        error_messages={
            "invalid_choice": "{input} no es una elección válida."
        },
        choices=["Perro", "Gato"],
    )
    shelter_uuid = serializers.UUIDField(
        required=True,
        error_messages={"invalid": "{input} is not a valid UUID."},
    )
    race = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=True,
        max_length=50,
    )
    age = serializers.IntegerField(
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
    observations = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=False,
        max_length=200,
    )
    description = serializers.CharField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=False,
        max_length=200,
    )
    image = serializers.URLField(
        error_messages={
            "max_length": COMMON_ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=False,
        max_length=200,
    )
