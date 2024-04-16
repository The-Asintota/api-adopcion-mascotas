from drf_spectacular.utils import (
    extend_schema_serializer,
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)
from apps.users.domain.constants import PET_TYPES, PET_SEX_TYPES


GetEndPointSchema = extend_schema(
    tags=["Pets"],
    responses={
        201: OpenApiResponse(
            description="**CREATED** The pet was created successfully.",
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
                    name="invalid_request_data",
                    summary="Invalid request data",
                    description="These are all the basic error messages for each field, in this example you can see how the messages will be sent. In a real use case, the error message for the validation or validations that have failed will be displayed.",
                    value={
                        "code": "invalid_request_data",
                        "detail": {
                            "pet_name": [
                                "El nombre no puede tener más de 50 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "pet_type": [
                                "Loro no es una elección válida.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "pet_sex": [
                                "M no es una elección válida.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "shelter": [
                                "58774f38-96f3-4550-a212-d35923c5bf9e is not a valid UUID.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "pet_race": [
                                "El valor ingresado es inválido.",
                                "El valor ingresad no puede tener más de 50 caracteres.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "pet_age": [
                                "El valor ingresado es inválido.",
                                "Asegúrate que este valor sea menor o igual a 99.",
                                "Asegúrate que este valor sea mayor o igual a 1.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "pet_observations": [
                                "El valor ingresado no puede tener más de 200 caracteres.",
                            ],
                            "pet_description": [
                                "El valor ingresado no puede tener más de 200 caracteres.",
                            ],
                            "pet_image": [
                                "El valor ingresado no puede tener más de 200 caracteres.",
                            ],
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
            summary="Register a new pet.",
            description=f"A valid pet registration data. The following validation rules are applied:\n- **pet_name:** the name must be less than 50 characters.\n- **pet_type:** the type of pet must be either {' or '.join(PET_TYPES)}.\n- **pet_sex:** the sex of the pet must be {' or '.join(PET_SEX_TYPES)}.\n- **shelter:** the shelter UUID must be a valid UUID.\n- **pet_age:** the age must be between 1 and 99.\n\pet_observations, pet_description, and pet_image fields are optional.",
            value={
                "pet_name": "Hector",
                "pet_type": PET_TYPES[0],
                "shelter": "58774f38-96f3-4550-a212-d35923c5bf9e",
                "pet_race": "Pastor alemán",
                "pet_sex": PET_SEX_TYPES[0],
                "pet_age": 2,
                "pet_observations": "Cachorro muy juguetón.",
                "pet_description": "Cachorro muy juguetón.",
                "pet_image": "https://example.com/image.png",
            },
            request_only=True,
        ),
    ],
)
