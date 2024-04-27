from rest_framework import serializers
from rest_framework import serializers
from apps.users.infrastructure.db import UserRepository
from apps.users.infrastructure.schemas.pet import PetSerializerSchema
from apps.users.domain.constants import (
    PET_TYPES,
    PET_SEX_TYPES,
    UserRoles,
)
from apps.users.models import Pet
from apps.utils import ErrorMessagesSpanishSerializer, ERROR_MESSAGES
from typing import Dict, Any


class PetReadOnlySerializer(serializers.Serializer):
    """
    Defines the serialization of a pet object for read-only purposes.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._user_repository = UserRepository

    pet_uuid = serializers.UUIDField(read_only=True)
    pet_type = serializers.CharField(read_only=True)
    pet_sex = serializers.CharField(read_only=True)
    shelter = serializers.CharField(read_only=True)
    pet_name = serializers.CharField(read_only=True)
    pet_race = serializers.CharField(read_only=True)
    pet_age = serializers.IntegerField(read_only=True)
    pet_observations = serializers.CharField(read_only=True)
    pet_description = serializers.CharField(read_only=True)
    pet_image = serializers.URLField(read_only=True)

    def to_representation(self, instance: Pet) -> Dict[str, Any]:
        profile_data = self._user_repository.get_profile_data(
            uuid=instance.shelter.profile,
            role=UserRoles.SHELTER.value,
        ).first()

        return {
            "pet_uuid": instance.pet_uuid.__str__(),
            "pet_type": instance.pet_type.type,
            "pet_sex": instance.pet_sex.sex,
            "shelter": {
                "uuid": instance.shelter.uuid.__str__(),
                "name": profile_data.shelter_name,
            },
            "pet_name": instance.pet_name,
            "pet_race": instance.pet_race,
            "pet_age": instance.pet_age,
            "pet_observations": instance.pet_observations,
            "pet_description": instance.pet_description,
            "image": instance.pet_image,
        }


@PetSerializerSchema
class PetSerializer(ErrorMessagesSpanishSerializer):
    """
    Defines the data required to register or update a pet in the system.
    """

    pet_name = serializers.CharField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
                field_name="El nombre", max_length="{max_length}"
            ),
        },
        required=True,
        max_length=50,
    )
    pet_type = serializers.ChoiceField(
        required=True,
        error_messages={
            "invalid_choice": ERROR_MESSAGES["invalid_choice"].format(
                input="{input}"
            ),
        },
        choices=PET_TYPES,
    )
    pet_sex = serializers.ChoiceField(
        required=True,
        error_messages={
            "invalid_choice": ERROR_MESSAGES["invalid_choice"].format(
                input="{input}"
            ),
        },
        choices=PET_SEX_TYPES,
    )
    pet_race = serializers.CharField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
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
            "invalid": ERROR_MESSAGES["invalid"].format(
                field_name="El valor ingresado"
            ),
        },
        required=True,
        max_value=99,
        min_value=1,
    )
    pet_observations = serializers.CharField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=False,
        max_length=200,
    )
    pet_description = serializers.CharField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=False,
        max_length=200,
    )
    pet_image = serializers.URLField(
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
                field_name="El valor ingresado", max_length="{max_length}"
            ),
        },
        required=False,
        max_length=200,
    )
