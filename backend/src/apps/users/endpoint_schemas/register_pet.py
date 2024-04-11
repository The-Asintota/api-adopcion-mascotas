from drf_spectacular.utils import (
    extend_schema_serializer,
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)


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
                            "type_pet": [
                                "Loro no es una elección válida.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "shelter_uuid": [
                                "58774f38-96f3-4550-a212-d35923c5bf9e is not a valid UUID.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "age": [
                                "El valor ingresado es inválido.",
                                "Asegúrate que este valor sea menor o igual a 99.",
                                "Asegúrate que este valor sea mayor o igual a 1.",
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                            ],
                            "observations": [
                                "El valor ingresado no puede tener más de 200 caracteres.",
                            ],
                            "description": [
                                "El valor ingresado no puede tener más de 200 caracteres.",
                            ],
                            "image": [
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
            description="A valid pet registration data. The following validation rules are applied:\n- **name:** the name must be less than 50 characters.\n- **type_pet:** the type of pet must be either 'Perro' or 'Gato'.\n- **shelter_uuid:** the shelter UUID must be a valid UUID.\n- **age:** the age must be between 1 and 99.\n\nObservations, description, and image fields are optional.",
            value={
                "name": "Hector",
                "type_pet": "Perro",
                "shelter_uuid": "58774f38-96f3-4550-a212-d35923c5bf9e",
                "race": "Pastor alemán",
                "age": 2,
                "observations": "Cachorro muy juguetón.",
                "description": "Cachorro muy juguetón.",
                "image": "https://example.com/image.png",
            },
            request_only=True,
        ),
    ],
)
