from django.db import OperationalError
from django.db.models import Q
from typing import Dict, Any
from apps.users.infrastructure.db import UserRepository
from apps.users.models import Pet, TypePet, Shelter
from apps.exceptions import DatabaseConnectionError, ResourceNotFoundError


class PetRepository:
    """
    PetRepository is a class that provides an abstraction of the datashelterbase
    operations for the `Pet` model.
    """

    pet_model = Pet
    type_pet_model = TypePet
    shelter_model = Shelter
    shelter_repository = UserRepository

    @classmethod
    def _get_type_pet(cls, type_pet: str) -> TypePet:
        """
        Method responsible for retrieving the pet type from the database.
        """

        try:
            type_pet = cls.type_pet_model.objects.get(type_name=type_pet)
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        return type_pet

    @classmethod
    def create(cls, data: Dict[str, Any]) -> None:
        """
        Insert a new pet into the database.

        Parameters:
        - data: A dictionary containing the pet data.
        """

        type_pet = data.pop("type_pet")
        shelter_uuid = data.pop("shelter_uuid")

        try:
            cls.pet_model.objects.create(
                type_pet=cls._get_type_pet(type_pet=type_pet),
                shelter=cls.shelter_repository.get_shelter(
                    shelter_uuid=shelter_uuid
                ),
                **data,
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

    @classmethod
    def get_pet(cls, **filters) -> Pet:
        """
        Retrieve a pet from the database based on the provided filters.

        Parameters:
        - filters: Keyword arguments that define the filters to apply.
        """

        query_params = Q()
        fields_shelter_model = [
            field.name for field in cls.shelter_model._meta.get_fields()
        ]
        fields_type_pet_model = [
            field.name for field in cls.type_pet_model._meta.get_fields()
        ]

        for field, value in filters.items():
            if field in fields_shelter_model:
                query_params &= Q(**{f"shelter__{field}": value})
                continue
            elif field in fields_type_pet_model:
                query_params &= Q(**{f"type_pet__{field}": value})
                continue
            else:
                query_params &= Q(**{field: value})

        try:
            pet = (
                cls.pet_model.objects.select_related("type_pet", "shelter")
                .filter(query_params)
                .first()
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        if not pet:
            raise ResourceNotFoundError(
                detail={
                    "message": "pet with the following filters not found.",
                    "filters": filters,
                },
                code="pet_not_found",
            )

        return pet
