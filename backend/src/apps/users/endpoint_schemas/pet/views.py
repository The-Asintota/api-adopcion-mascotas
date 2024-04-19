from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)
from uuid import uuid4
from apps.users.endpoint_schemas.auth import JWTAuthenticationScheme
from apps.users.domain.constants import PET_TYPES, PET_SEX_TYPES


CreateUpdatePetSchema = extend_schema(
    operation_id="create_update_pet",
    tags=["Pets"],
    auth=[
        {
            "JWTAuthentication": [],
        }
    ],
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


GetAllPetsSchema = extend_schema(
    operation_id="get_all_pets",
    tags=["Pets"],
    auth=[],
    responses={
        200: OpenApiResponse(
            description="**OK**",
            response={
                "properties": {
                    "count": {"type": "integer"},
                    "next": {"type": "string"},
                    "previous": {"type": "string"},
                    "field": {
                        "type": "array",
                        "items": {"type": "object"},
                    },
                }
            },
            examples=[
                OpenApiExample(
                    name="request_success",
                    summary="Request successful",
                    description="This is an example of a successful request. In this example, you can see how the information will be represented.",
                    value={
                        "count": 57,
                        "next": "http://127.0.0.1:8000/api/v1/pet/97c6efb5d6cc429098e0047bde3de168/?page=2",
                        "previous": None,
                        "results": [
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": uuid4().__str__(),
                                    "name": "Refugio 1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": uuid4().__str__(),
                                    "name": "Refugio 2",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": uuid4().__str__(),
                                    "name": "Refugio 3",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": uuid4().__str__(),
                                    "name": "Refugio 4",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": uuid4().__str__(),
                                    "name": "Refugio 5",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": uuid4().__str__(),
                                    "name": "Refugio 6",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": uuid4().__str__(),
                                    "name": "Refugio 7",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": uuid4().__str__(),
                                    "name": "Refugio 8",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": uuid4().__str__(),
                                    "name": "Refugio 9",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": uuid4().__str__(),
                                    "name": "Refugio 10",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                        ],
                    },
                ),
            ],
        ),
        404: OpenApiResponse(
            description="**NOT_FOUND**",
            response={
                "properties": {
                    "code": {"type": "string"},
                    "detail": {"type": "string"},
                }
            },
            examples=[
                OpenApiExample(
                    name="pet_not_found",
                    summary="Shelter not found",
                    description="These are all the basic error messages for each field, in this example you can see how the messages will be sent. In a real use case, the error message for the validation or validations that have failed will be displayed.",
                    value={
                        "code": "pet_not_found",
                        "detail": "No pets were found with the provided filters.",
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


GetPetByShelterSchema = extend_schema(
    operation_id="get_pet_by_shelter",
    tags=["Pets"],
    responses={
        200: OpenApiResponse(
            description="**OK**",
            response={
                "properties": {
                    "count": {"type": "integer"},
                    "next": {"type": "string"},
                    "previous": {"type": "string"},
                    "field": {
                        "type": "array",
                        "items": {"type": "object"},
                    },
                }
            },
            examples=[
                OpenApiExample(
                    name="request_success",
                    summary="Request successful",
                    description="This is an example of a successful request. In this example, you can see how the information will be represented.",
                    value={
                        "count": 57,
                        "next": "http://127.0.0.1:8000/api/v1/pet/97c6efb5d6cc429098e0047bde3de168/?page=2",
                        "previous": None,
                        "results": [
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": "58774f38-96f3-4550-a212-d35923c5bf9e",
                                    "name": "Refugio1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": "58774f38-96f3-4550-a212-d35923c5bf9e",
                                    "name": "Refugio1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": "58774f38-96f3-4550-a212-d35923c5bf9e",
                                    "name": "Refugio1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": "58774f38-96f3-4550-a212-d35923c5bf9e",
                                    "name": "Refugio1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": "58774f38-96f3-4550-a212-d35923c5bf9e",
                                    "name": "Refugio1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": "58774f38-96f3-4550-a212-d35923c5bf9e",
                                    "name": "Refugio1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": "58774f38-96f3-4550-a212-d35923c5bf9e",
                                    "name": "Refugio1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": "58774f38-96f3-4550-a212-d35923c5bf9e",
                                    "name": "Refugio1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": "58774f38-96f3-4550-a212-d35923c5bf9e",
                                    "name": "Refugio1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                            {
                                "pet_name": "mascota1",
                                "pet_type": PET_TYPES[0],
                                "pet_sex": PET_SEX_TYPES[0],
                                "shelter": {
                                    "uud": "58774f38-96f3-4550-a212-d35923c5bf9e",
                                    "name": "Refugio1",
                                },
                                "pet_race": "pastor aleman",
                                "pet_age": 2,
                                "pet_observations": "sin observaciones",
                                "pet_description": "sin descripciones",
                                "pet_image": "https://imagedefault.com",
                            },
                        ],
                    },
                ),
            ],
        ),
        404: OpenApiResponse(
            description="**NOT_FOUND**",
            response={
                "properties": {
                    "code": {"type": "string"},
                    "detail": {"type": "string"},
                }
            },
            examples=[
                OpenApiExample(
                    name="pet_not_found",
                    summary="Shelter not found",
                    description="These are all the basic error messages for each field, in this example you can see how the messages will be sent. In a real use case, the error message for the validation or validations that have failed will be displayed.",
                    value={
                        "code": "pet_not_found",
                        "detail": "No pets were found with the provided filters.",
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
