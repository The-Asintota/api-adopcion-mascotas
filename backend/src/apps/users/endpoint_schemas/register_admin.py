from drf_spectacular.utils import (
    extend_schema_serializer,
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)


APISchema = extend_schema(
    tags=["Admins"],
    responses={
        201: OpenApiResponse(
            description="**(CREATED)** The admin was created successfully.",
        ),
        400: OpenApiResponse(
            description="**(BAD_REQUEST)**",
            response={
                "properties": {
                    "code": {"type": "string"},
                    "detail": {"type": "object"},
                }
            },
            examples=[
                OpenApiExample(
                    name="email_invalid",
                    summary="Invalid request data",
                    description="These are all the basic error messages for each field, in this example you can see how the messages will be sent. In a real use case, the error message for the validation or validations that have failed will be displayed.",
                    value={
                        "code": "invalid_request_data",
                        "detail": {
                            "email": [
                                "Correo electrónico inválido.",
                                "El correo electrónico no puede tener más de 90 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "password": [
                                "La contraseña debe tener al menos 8 caracteres.",
                                "La contraseña no puede tener más de 20 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "name": [
                                "El nombre no puede tener más de 50 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                        },
                    },
                ),
                OpenApiExample(
                    name="password_mismatch",
                    summary="Passwords do not match",
                    description="The passwords do not match.",
                    value={
                        "code": "password_mismatch",
                        "detail": "Las contraseñas no coinciden.",
                    },
                ),
            ],
        ),
        500: OpenApiResponse(
            description="**(INTERNAL_SERVER_ERROR)**",
            response={
                "properties": {
                    "code": {"type": "string"},
                    "detail": {"type": "string"},
                }
            },
            examples=[
                OpenApiExample(
                    name="internal_server_error",
                    summary="Internal server error",
                    description="An internal server error occurred.",
                    value={
                        "code": "internal_server_error",
                        "detail": "Internal server error.",
                    },
                ),
            ],
        ),
    },
)


SerializerSchema = extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="data_valid",
            summary="Register a new user",
            description="A valid admin registration data. The following validations will be applied:\n- *Email:* Must be in a valid email format, no longer than 90 characters and not in use.\n- *Password:* Must be at least 8 characters, not more than 20 characters, and not a common or simple password.\n- *Confirm Password:* Must match the password.\n- *Name:* Must not be longer than 50 characters.",
            value={
                "email": "admin1@example.com",
                "password": "contraseña1234",
                "confirm_password": "contraseña1234",
                "name": "Admin de la plataforma",
            },
            request_only=True,
        ),
    ],
)
