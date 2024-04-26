from drf_spectacular.utils import (
    extend_schema_serializer,
    OpenApiExample,
)


AuthSerializerSchema = extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="data_valid",
            summary="User authentication data.",
            description="Valid credentials for a user. The following validations will be applied:\n- **email:** Must be in a valid email format and no longer than 40 characters.\n- **password:** Must be at least 8 characters and not more than 20 characters.",
            value={
                "email": "user1@example.com",
                "password": "contraseña1234",
            },
            request_only=True,
        ),
    ],
)
