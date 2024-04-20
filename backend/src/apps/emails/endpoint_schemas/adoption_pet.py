from drf_spectacular.utils import (
    extend_schema_serializer,
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)


PostSchema = extend_schema(
    operation_id="send_adoption_pet_email",
    tags=["Emails"],
    responses={
        200: OpenApiResponse(
            description="**OK** Mail sent successfully.",
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
                            "pet_name": [
                                "El valor ingresado es inválido.",
                                "El valor ingresado no puede tener más de 50 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "shelter_uuid": [
                                "El id del refugio es inválido.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "user_phone": [
                                "El número de teléfono es inválido.",
                                "El número de teléfono no puede tener más de 25 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "user_name": [
                                "El nombre es inválido.",
                                "El nombre no puede tener más de 50 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "user_email": [
                                "El correo electrónico es inválido.",
                                "El correo electrónico no puede tener más de 40 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "message": [
                                "El valor ingresado es inválido.",
                                "El valor ingresado no puede tener más de 300 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                        },
                    },
                ),
            ],
        ),
        404: OpenApiResponse(
            description="**NOT_FOUND**",
            response={
                "properties": {
                    "detail": {"type": "string"},
                    "code": {"type": "object"},
                }
            },
            examples=[
                OpenApiExample(
                    name="shelter_not_found",
                    summary="Pet shelter not found",
                    description="This message is used when the shelter is not found. In this example you can see how the information will be represented.",
                    value={
                        "code": "shelter_not_found",
                        "detail": {
                            "message": "shelter with the following filters not found.",
                            "filters": {
                                "base_user": "123e4567-e89b-12d3-a456-426614174000",
                            },
                        }
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


AdoptionPetSerializerSchema = extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="data_valid",
            summary="RegistData required for the message",
            description="Valid data required to send the message to the shelter. This message is a notification that will be sent to the shelter with the necessary information about the adoption request by a user of the platform. The following validations will be applied:\n- **pet_name:** Must not be longer than 50 characters and valid string.\n- **shelter_uuid:** Must be a valid UUID.\n- **user_name:** Must not be longer than 50 characters and valid string.\n- **user_email:** Must not be longer than 40 characters and valid email.\n- **user_phone:** Must not be longer than 25 characters and valid phone number.\n- **message:** Must not be longer than 300 characters and valid string.",
            value={
                "pet_name": "Mascota 1",
                "shelter_uuid": "123e4567-e89b-12d3-a456-426614174000",
                "user_name": "User 1",
                "user_email": "user@email.com",
                "user_phone": "+57 3213514798",
                "message": "Mensaje de prueba",
            },
            request_only=True,
        ),
    ],
)
