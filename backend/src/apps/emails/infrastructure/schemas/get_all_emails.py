from drf_spectacular.utils import (
    extend_schema_serializer,
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)


EmailSentListSchema = extend_schema(
    operation_id="get_all_emails",
    tags=["Emails"],
    auth=[
        {
            "JWTAuthentication": [],
        }
    ],
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
                        "next": "http://127.0.0.1:8000/api/v1/email/?page=2",
                        "previous": None,
                        "results": [
                            {
                                "uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                                "subject": "Solicitud de adopción",
                                "message": "Mensaje de prueba.",
                                "addressee": "refugio11@email.com",
                                "additional_info": {
                                    "pet_name": "Macota 1",
                                    "user_name": "User 1",
                                    "user_email": "user1@email.com",
                                    "user_phone": "+573212547790",
                                },
                            },
                            {
                                "uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                                "subject": "Solicitud de adopción",
                                "message": "Mensaje de prueba.",
                                "addressee": "refugio2@email.com",
                                "additional_info": {
                                    "pet_name": "Macota 2",
                                    "user_name": "User 2",
                                    "user_email": "user2@email.com",
                                    "user_phone": "+573202447980",
                                },
                            },
                            {
                                "uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                                "subject": "Solicitud de adopción",
                                "message": "Mensaje de prueba.",
                                "addressee": "refugio3@email.com",
                                "additional_info": {
                                    "pet_name": "Macota 3",
                                    "user_name": "User 3",
                                    "user_email": "user3@email.com",
                                    "user_phone": "+573159874512",
                                },
                            },
                            {
                                "uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                                "subject": "Solicitud de adopción",
                                "message": "Mensaje de prueba.",
                                "addressee": "refugio3@email.com",
                                "additional_info": {
                                    "pet_name": "Macota 3",
                                    "user_name": "User 3",
                                    "user_email": "user3@email.com",
                                    "user_phone": "+573159874512",
                                },
                            },
                            {
                                "uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                                "subject": "Solicitud de adopción",
                                "message": "Mensaje de prueba.",
                                "addressee": "refugio3@email.com",
                                "additional_info": {
                                    "pet_name": "Macota 3",
                                    "user_name": "User 3",
                                    "user_email": "user3@email.com",
                                    "user_phone": "+573159874512",
                                },
                            },
                            {
                                "uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                                "subject": "Solicitud de adopción",
                                "message": "Mensaje de prueba.",
                                "addressee": "refugio3@email.com",
                                "additional_info": {
                                    "pet_name": "Macota 3",
                                    "user_name": "User 3",
                                    "user_email": "user3@email.com",
                                    "user_phone": "+573159874512",
                                },
                            },
                            {
                                "uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                                "subject": "Solicitud de adopción",
                                "message": "Mensaje de prueba.",
                                "addressee": "refugio3@email.com",
                                "additional_info": {
                                    "pet_name": "Macota 3",
                                    "user_name": "User 3",
                                    "user_email": "user3@email.com",
                                    "user_phone": "+573159874512",
                                },
                            },
                            {
                                "uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                                "subject": "Solicitud de adopción",
                                "message": "Mensaje de prueba.",
                                "addressee": "refugio3@email.com",
                                "additional_info": {
                                    "pet_name": "Macota 3",
                                    "user_name": "User 3",
                                    "user_email": "user3@email.com",
                                    "user_phone": "+573159874512",
                                },
                            },
                            {
                                "uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                                "subject": "Solicitud de adopción",
                                "message": "Mensaje de prueba.",
                                "addressee": "refugio3@email.com",
                                "additional_info": {
                                    "pet_name": "Macota 3",
                                    "user_name": "User 3",
                                    "user_email": "user3@email.com",
                                    "user_phone": "+573159874512",
                                },
                            },
                            {
                                "uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                                "subject": "Solicitud de adopción",
                                "message": "Mensaje de prueba.",
                                "addressee": "refugio3@email.com",
                                "additional_info": {
                                    "pet_name": "Macota 3",
                                    "user_name": "User 3",
                                    "user_email": "user3@email.com",
                                    "user_phone": "+573159874512",
                                },
                            },
                        ],
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


EmailsListSerializerSchema = extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="data_valid",
            summary="Data valid",
            description=f"This is an example of a valid email object.",
            value={
                "shelter_uuid": "44c79edd-1188-45dc-85af-7398ddee0546",
                "message": "Mensaje de prueba.",
                "pet_name": "Macota 3",
                "user_name": "User 3",
                "user_email": "user3@email.com",
                "user_phone": "+573159874512",
            },
            request_only=True,
        ),
    ],
)
