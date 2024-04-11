from drf_spectacular.utils import (
    extend_schema_serializer,
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)


GetEndPointSchema = extend_schema(
    tags=["Shelters"],
    responses={
        201: OpenApiResponse(
            description="**CREATED** The shelter was created successfully.",
        ),
        400: OpenApiResponse(
            description="**(BAD_REQUEST)**",
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
                    name="invalid_request_data1",
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
                                "La contraseña debe contener al menos una mayuscula o una minuscula.",
                                "Esta contraseña es demasiado común."
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "phone_number": [
                                "El número de teléfono es inválido.",
                                "El número de teléfono no puede tener más de 25 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "shelter_name": [
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
                                "El valor ingresado no puede tener más de 50 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "logo_url": [
                                "El valor ingresado no puede tener más de 200 caracteres.",
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
                        "code": "invalid_request_data2",
                        "detail": {
                            "non_field_errors": [
                                "Las contraseñas no coinciden."
                            ]
                        },
                    },
                ),
                OpenApiExample(
                    name="invalid_request_data3",
                    summary="Email already in use",
                    description="This error message is used when the email is already in use. In this example you can see how the information will be represented.",
                    value={
                        "code": "invalid_request_data",
                        "detail": {
                            "email": [
                                "Este correo electrónico ya está en uso.",
                            ]
                        },
                    },
                ),
            ],
        ),
        500: OpenApiResponse(
            description="**INTERNAL_SERVER_ERROR**",
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


GetSerializerSchema = extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="data_valid",
            summary="Register a new shelter.",
            description="A valid shelter registration data. The following validations will be applied:\n- **email:** Must be in a valid email format, no longer than 40 characters and not in use.\n- **password:** Must be at least 8 characters, not more than 20 characters, and not a common or simple password.\n- **confirm_password:** Must match the password.\n- **phone_number:** Must be a valid phone number, no longer than 25 characters.\n- **shelter_name:** Must not be longer than 50 characters.\n- **address:** Must not be longer than 100 characters.\n- **responsible:** Must not be longer than 50 characters.\n- **logo_url:** Must not be longer than 200 characters.",
            value={
                "email": "shelter1@example.com",
                "password": "contraseña123456789",
                "confirm_password": "contraseña123456789",
                "phone_number": "+57 3213149578",
                "shelter_name": "Refugio de animales",
                "address": "Calle 123 # 45-67",
                "responsible": "Juan Pérez",
                "logo_url": "https://example.com/logo.png",
            },
            request_only=True,
        ),
    ],
)
