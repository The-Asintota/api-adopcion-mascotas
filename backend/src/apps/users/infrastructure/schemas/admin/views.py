from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)


AdminPostSchema = extend_schema(
    operation_id="register_admin",
    tags=["Administrators"],
    responses={
        201: OpenApiResponse(
            description="**CREATED** The admin was created successfully.",
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
                            "admin_name": [
                                "El nombre no puede tener más de 50 caracteres.",
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
                            "confirm_password": [
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
