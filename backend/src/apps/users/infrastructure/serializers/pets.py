from rest_framework import serializers
from django.core.validators import (
    MaxLengthValidator,
)


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


class RegisterPetSerializer(ErrorMessages):
    """
    Defines the data required to register a pet in the system.
    """

    name = serializers.CharField(
        required=True,
        validators=[
            MaxLengthValidator(
                limit_value=50,
                message="El nombre no puede tener más de 50 caracteres.",
            ),
        ],
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
        required=True,
        validators=[
            MaxLengthValidator(
                limit_value=2,
                message="La edad no puede tener más de 2 caracteres.",
            ),
        ],
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


class TypePetSerializer(ErrorMessages):
    """
    Defines the data required to register a pet in the system.
    """

    name = serializers.CharField(
        required=True,
        validators=[
            MaxLengthValidator(
                limit_value=50,
                message="El nombre no puede tener más de 50 caracteres.",
            ),
        ],
    )
