from drf_spectacular.utils import (
    extend_schema_serializer,
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)


APISchema = extend_schema(
    tags=["Users"],
    responses={
        201: OpenApiResponse(
            description="**(CREATED)** The shelter was created successfully.",
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
                            "phone_number": [
                                "Número inválido.",
                                "La nùmero no puede tener más de 25 caracteres.",
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
                            "address": [
                                "El dirección no puede tener más de 100 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "responsible": [
                                "El nombre del responsable no puede tener más de 50 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "logo_url": [
                                "Supera el máximo de caracteres permitidos.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                        },
                    },
                ),
                OpenApiExample(
                    name="passwords_not_match",
                    summary="Passwords do not match",
                    description="This error message is used when the passwords do not match. In this example you can see how the information will be represented.",
                    value={
                        "code": "invalid_request_data",
                        "detail": {
                            "non_field_errors": [
                                "Las contraseñas no coinciden."
                            ]
                        },
                    },
                ),
                OpenApiExample(
                    name="email_already_use",
                    summary="Email already in use",
                    description="This error message is used when the email is already in use. In this example you can see how the information will be represented.",
                    value={
                        "code": "invalid_request_data",
                        "detail": {
                            "email": [
                                "Este correo electrónico ya está en uso."
                            ]
                        },
                    },
                ),
            ],
        ),
        500: OpenApiResponse(
            description="**(INTERNAL_SERVER_ERROR)**",
            response={
                "properties": {
                    "detail": {
                        "type": "string",
                    },
                    "code": {
                        "type": "string",
                    },
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


SerializerSchema = extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="data_valid",
            summary="Register a new user",
            description="A valid shelter registration data. The following validations will be applied:\n- **Email:** Must be in a valid email format, no longer than 90 characters and not in use.\n- **Password:** Must be at least 8 characters, not more than 20 characters, and not a common or simple password.\n- **Confirm Password:** Must match the password.\n- **Phone Number:** Must be a valid phone number, no longer than 25 characters.\n- **Name:** Must not be longer than 50 characters.\n- **Address:** Must not be longer than 100 characters.\n- **Responsible:** Must not be longer than 50 characters.\n- **Logo URL:** Must not be longer than 200 characters.",
            value={
                "email": "shelter1@example.com",
                "password": "contraseña123456789",
                "confirm_password": "contraseña123456789",
                "phone_number": "+57 3213149578",
                "name": "Refugio de animales",
                "address": "Calle 123 # 45-67",
                "responsible": "Juan Pérez",
                "logo_url": "https://example.com/logo.png",
            },
            request_only=True,
        ),
    ],
)
