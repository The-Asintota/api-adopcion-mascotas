from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)
from apps.users.domain.constants import PET_TYPES, PET_SEX_TYPES


GetEndPointSchema = extend_schema(
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
                                "shelter": "Refugio1",
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
                                "shelter": "Refugio1",
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
                                "shelter": "Refugio1",
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
                                "shelter": "Refugio1",
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
                                "shelter": "Refugio1",
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
                                "shelter": "Refugio1",
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
                                "shelter": "Refugio1",
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
                                "shelter": "Refugio1",
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
                                "shelter": "Refugio1",
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
                                "shelter": "Refugio1",
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
                    "detail": {
                        "type": "object",
                        "properties": {
                            "field": {"type": "string"},
                        },
                    },
                }
            },
            examples=[
                OpenApiExample(
                    name="pet_not_found",
                    summary="Shelter not found",
                    description="These are all the basic error messages for each field, in this example you can see how the messages will be sent. In a real use case, the error message for the validation or validations that have failed will be displayed.",
                    value={
                        "code": "pet_not_found",
                        "detail": {
                            "message": "pet with the following filters not found.",
                            "filters": {
                                "shelter": "97c6efb5d6cc429098e0047bde3de169"
                            },
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
