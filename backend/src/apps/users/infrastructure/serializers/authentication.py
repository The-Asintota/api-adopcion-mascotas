from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    AuthUser,
    Token,
)
from rest_framework import serializers
from django.core.validators import RegexValidator
from apps.users.infrastructure.serializers.utils import ErrorMessages
from apps.users.infrastructure.serializers.constants import (
    COMMON_ERROR_MESSAGES,
)
from apps.users.endpoint_schemas.authentication import GetSerializerSchema


@GetSerializerSchema
class AuthenticationSerializer(ErrorMessages):
    """
    Handles the data for user authentication. Checks that the provided email and
    password meet the necessary requirements.
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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Defines the custom serializer used to generate the access and refresh tokens wit
    custom payload.
    """

    @classmethod
    def get_token(cls, user: AuthUser) -> Token:

        token = cls.token_class.for_user(user)
        token["role"] = user.__class__.__name__.lower()

        return token
