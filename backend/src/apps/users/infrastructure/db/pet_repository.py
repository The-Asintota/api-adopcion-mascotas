from django.db import OperationalError
from django.db.models import Q
from typing import Dict, Any
from apps.users.infrastructure.db import UserRepository
from apps.users.models import Pet, TypePet
from apps.exceptions import DatabaseConnectionError, UserNotFoundError


class PetRepository:
    """
    PetRepository is a class that provides an abstraction of the datashelterbase
    operations for the `Pet` model.
    """

    model_pet = Pet
    model_type_pet = TypePet
    shelter_repository = UserRepository

    @classmethod
    def _get_type_pet(cls, type_pet: str) -> TypePet:
        """
        Method responsible for retrieving the pet type from the database.
        """

        try:
            type_pet = cls.model_type_pet.objects.get(name=type_pet)
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
            cls.model_pet.objects.create(
                type_pet=cls._get_type_pet(type_pet=type_pet),
                shelter=cls.shelter_repository.get_shelter(shelter_uuid=shelter_uuid),
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
        """

        query = Q()
        for field, value in filters.items():
            if field == "type_pet":
                query &= Q(**{f"type_pet__{field}": value})
            else:
                query &= Q(**{field: value})
        try:
            pet = (
                cls.model_pet.objects.select_related("type_pet")
                    .filter(query)
                    .first()
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()
        if not pet:
            raise UserNotFoundError(
                detail=f"Pet with the following filters: {filters} not found.",
                code="pet_not_found",
            )

        return pet