from drf_spectacular.utils import (
    extend_schema_serializer,
    OpenApiExample,
)
from apps.users.domain.constants import PET_TYPES, PET_SEX_TYPES


PetSerializerSchema = extend_schema_serializer(
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
