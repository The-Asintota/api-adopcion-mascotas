from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    Token,
)
from rest_framework import serializers
from django.core.validators import RegexValidator
from apps.users.infrastructure.schemas.jwt import AuthSerializerSchema
from apps.users.models import User
from apps.utils import ErrorMessagesSpanishSerializer, ERROR_MESSAGES


@AuthSerializerSchema
class AuthenticationSerializer(ErrorMessagesSpanishSerializer):
    """
    Handles the data for user authentication. Checks that the provided email and
    password meet the necessary requirements.
    """

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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Defines the custom serializer used to generate the access and refresh tokens wit
    custom payload.
    """

    @classmethod
    def get_token(cls, user: User) -> Token:
        token = cls.token_class.for_user(user)
        token["role"] = user.content_type.model_class().__name__

        return token
