from django.core.validators import (
    MaxLengthValidator,
)
from rest_framework import serializers
from apps.users.endpoint_schemas.register_pet import SerializerSchema


class ErrorMessages(serializers.Serializer):
    """
    A serializer class that provides custom error messages for fields.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customized error messages
        msg = {
            "required": "Este campo es requerido.",
            "blank": "Este campo no puede estar en blanco.",
            "null": "Este campo no puede ser nulo.",
        }
        fields = list(self.fields.keys())
        for field_name in fields:
            self.fields[field_name].error_messages.update(msg)


@SerializerSchema
class RegisterPetSerializer(ErrorMessages):
    """
    Defines the data required to register a pet in the system.
    """

    pet_name = serializers.CharField(
        required=True,
        validators=[
            MaxLengthValidator(
                limit_value=50,
                message="El nombre no puede tener más de 50 caracteres.",
            ),
        ],
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
        required=True,
        validators=[
            MaxLengthValidator(
                limit_value=50,
                message="La raza no puede tener más de 50 caracteres.",
            ),
        ],
    )
    age = serializers.IntegerField(
        error_messages={
            "max_value": "Asegúrate que este valor sea menor o igual a {max_value}.",
            "min_value": "Asegúrate que este valor sea mayor o igual a {min_value}.",
            "invalid": "Se requiere un número entero válido.",
        },
        required=True,
        max_value=99,
        min_value=1,
    )
    observations = serializers.CharField(
        required=False,
        validators=[
            MaxLengthValidator(
                limit_value=200,
                message="La observación no puede tener más de 200 caracteres.",
            ),
        ],
    )
    description = serializers.CharField(
        required=False,
        validators=[
            MaxLengthValidator(
                limit_value=200,
                message="La descripción no puede tener más de 200 caracteres.",
            ),
        ],
    )
    image = serializers.URLField(
        required=False,
        validators=[
            MaxLengthValidator(
                limit_value=200,
                message="Supera el máximo de caracteres permitidos.",
            ),
        ],
    )
