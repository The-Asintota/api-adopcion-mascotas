from drf_spectacular.utils import (
    extend_schema_serializer,
    OpenApiExample,
)


ShelterSerializerSchema = extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="data_valid",
            summary="Register a new shelter.",
            description="A valid shelter registration data. The following validations will be applied:\n- **email:** Must be in a valid email format, no longer than 40 characters and not in use.\n- **password:** Must be at least 8 characters, not more than 20 characters, and not a common or simple password.\n- **confirm_password:** Must match the password.\n- **shelter_phone_number:** Must be a valid phone number, no longer than 25 characters.\n- **shelter_name:** Must not be longer than 50 characters and not in use.\n- **shelter_address:** Must not be longer than 100 characters.\n- **shelter_responsible:** Must not be longer than 50 characters.\n- **shelter_logo:** Must not be longer than 200 characters.",
            value={
                "email": "shelter1@example.com",
                "password": "contraseña1234",
                "confirm_password": "contraseña1234",
                "shelter_phone_number": "+57 3213149578",
                "shelter_name": "Refugio de animales",
                "shelter_address": "Calle 123 # 45-67",
                "shelter_responsible": "Juan Pérez",
                "shelter_logo": "https://example.com/logo.png",
            },
            request_only=True,
        ),
    ],
)
