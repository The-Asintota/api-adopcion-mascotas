from drf_spectacular.utils import (
    extend_schema_serializer,
    OpenApiExample,
)


AdminSerializerSchema = extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="data_valid",
            summary="Administrator user registration data.",
            description="A valid admin registration data. The following validations will be applied:\n- **email:** Must be in a valid email format, no longer than 40 characters and not in use.\n- **password:** Must be at least 8 characters, not more than 20 characters, and not a common or simple password.\n- **confirm_password:** Must match the password.\n- **admin_name:** Must not be longer than 50 characters and not in use.",
            value={
                "email": "admin1@example.com",
                "password": "contraseña1234",
                "confirm_password": "contraseña1234",
                "admin_name": "Admin de la plataforma",
            },
            request_only=True,
        ),
    ],
)
