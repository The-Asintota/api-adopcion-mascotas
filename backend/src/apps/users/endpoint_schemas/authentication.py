from drf_spectacular.utils import (
    extend_schema_serializer,
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)


GetEndPointSchema = extend_schema(
    tags=["JSON Web Token"],
    responses={
        200: OpenApiResponse(
            description="**OK**",
            response={
                "properties": {
                    "access": {"type": "string"},
                    "refresh": {"type": "string"},
                }
            },
            examples=[
                OpenApiExample(
                    name="response_ok",
                    summary="Valid request",
                    description="Authenticated user, the response will contain the access and refresh tokens.",
                    value={
                        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExMDU0MzYyLCJpYXQiOjE3MTEwNDcxNjIsImp0aSI6IjY0MTE2YzgyYjhmMDQzOWJhNTJkZGZmMzgyNzQ2ZTIwIiwidXNlcl9pZCI6IjJhNmI0NTNiLWZhMmItNDMxOC05YzM1LWIwZTk2ZTg5NGI2MyJ9.gfhWpy5rYY6P3Xrg0usS6j1KhEvF1HqWMiU7AaFkp9A",
                        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTEzMzU2MiwiaWF0IjoxNzExMDQ3MTYyLCJqdGkiOiI2ZTRmNTdkMGJjNTc0NWY0OWMzODg4YjQ2YTM1OTJjNSIsInVzZXJfaWQiOiIyYTZiNDUzYi1mYTJiLTQzMTgtOWMzNS1iMGU5NmU4OTRiNjMifQ.81pQ3WftFZs5O50vGqwY2a6yPkXArQK6WKyrwus3s6A",
                    },
                ),
            ],
        ),
        400: OpenApiResponse(
            description="**BAD_REQUEST**",
            response={
                "properties": {
                    "code": {"type": "string"},
                    "detail": {
                        "type": "object",
                        "properties": {
                            "field": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                        },
                    },
                }
            },
            examples=[
                OpenApiExample(
                    name="data_invalid",
                    summary="Invalid request data",
                    description="These are all the basic error messages for each field, in this example you can see how the messages will be sent. In a real use case, the error message for the validation or validations that have failed will be displayed.",
                    value={
                        "code": "invalid_request_data",
                        "detail": {
                            "email": [
                                "El correo electrónico es inválido.",
                                "El correo electrónico no puede tener más de 40 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "password": [
                                "La contraseña no puede tener más de 20 caracteres."
                                "La contraseña debe tener al menos8 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                        },
                    },
                ),
            ],
        ),
        401: OpenApiResponse(
            description="**UNAUTHORIZED**",
            response={
                "properties": {
                    "code": {"type": "string"},
                    "detail": {"type": "string"},
                }
            },
            examples=[
                OpenApiExample(
                    name="authentication_failed",
                    summary="Credentials invalid",
                    description="The user's credentials are invalid.",
                    value={
                        "code": "authentication_failed",
                        "detail": "Correo o contraseña inválida.",
                    },
                ),
                OpenApiExample(
                    name="user_inactive",
                    summary="User inactive",
                    description="The user's account is inactive.",
                    value={
                        "code": "authentication_failed",
                        "detail": "Cuenta del usuario inactiva.",
                    },
                ),
            ],
        ),
        500: OpenApiResponse(
            description="**INTERNAL_SERVER_ERROR**",
            response={
                "properties": {
                    "detail": {"type": "string"},
                    "code": {"type": "string"},
                }
            },
            examples=[
                OpenApiExample(
                    name="database_connection_error",
                    summary="Database connection error",
                    description="This error message is used when the API cannot connect to the database. In this example you can see how the information will be represented.",
                    value={
                        "code": "database_connection_error",
                        "detail": "Unable to establish a connection with the database. Please try again later.",
                    },
                ),
            ],
        ),
    },
)


GetSerializerSchema = extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="data_valid",
            summary="User authentication data.",
            description="Valid credentials for a user. The following validations will be applied:\n- **email:** Must be in a valid email format and no longer than 40 characters.\n- **password:** Must be at least 8 characters and not more than 20 characters.",
            value={
                "email": "user1@example.com",
                "password": "contraseña1234",
            },
            request_only=True,
        ),
    ],
)
