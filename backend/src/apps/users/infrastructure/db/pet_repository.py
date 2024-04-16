from django.db import OperationalError
from django.db.models import Q, QuerySet
from typing import Dict, Any
from apps.users.infrastructure.db import UserRepository
from apps.users.domain.typing import StrUUID
from apps.users.models import Pet, PetType, PetSex, Shelter
from apps.exceptions import DatabaseConnectionError, ResourceNotFoundError


class PetRepository:
    """
    PetRepository is a class that provides an abstraction of the datashelterbase
    operations for the `Pet` model.
    """

    pet_model = Pet
    pet_type_model = PetType
    pet_sex_model = PetSex
    shelter_model = Shelter
    shelter_repository = UserRepository
    related_fields = {
        field.name: "shelter" for field in shelter_model._meta.get_fields()
    }
    related_fields.update(
        {field.name: "pet_type" for field in pet_type_model._meta.get_fields()}
    )
    related_fields.update(
        {field.name: "pet_sex" for field in pet_sex_model._meta.get_fields()}
    )

    @classmethod
    def _create_query_params(cls, **filters) -> Q:
        """
        Create a Q object based on the provided filters.

        #### Parameters:
        - filters: Keyword arguments that define the filters to apply.
        """

        query_params = Q()

        for field, value in filters.items():
            foreign_key = cls.related_fields.get(field, None)
            if foreign_key:
                query_params &= Q(**{f"{foreign_key}__{field}": value})
                continue
            query_params &= Q(**{field: value})

        return query_params

    @classmethod
    def create(cls, data: Dict[str, Any]) -> None:
        """
        Insert a new pet into the database.

        #### Parameters:
        - data: A dictionary containing the pet data.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        """

        pet_type = data.pop("pet_type")
        pet_sex = data.pop("pet_sex")
        shelter_uuid = data.pop("shelter")

        try:
            cls.pet_model.objects.create(
                pet_type=cls.pet_type_model.objects.get(type=pet_type),
                pet_sex=cls.pet_sex_model.objects.get(sex=pet_sex),
                shelter=cls.shelter_repository.get_shelter(
                    base_user=shelter_uuid
                ),
                **data,
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

    @classmethod
    def get_pet_by_filters(cls, **filters) -> QuerySet:
        """
        Retrieve a pet from the database based on the provided filters.

        #### Parameters:
        - filters: Keyword arguments that define the filters to apply.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        - ResourceNotFoundError: If no JWT matches the provided filters.
        """

        query_params = cls._create_query_params(**filters)

        try:
            pet = cls.pet_model.objects.select_related(
                "pet_type", "pet_sex", "shelter"
            ).filter(query_params)
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        if len(pet) == 0:
            raise ResourceNotFoundError(
                code="pet_not_found",
                detail={
                    "message": "pet with the following filters not found.",
                    "filters": filters,
                },
            )

        return pet

    @classmethod
    def get_pet_by_uuid(cls, uuid: StrUUID) -> Pet:
        """
        Retrieve a pet from the database based on its UUID.

        #### Parameters:
        - uuid: The UUID of the pet to retrieve.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        - ResourceNotFoundError: If no pet matches the provided UUID.
        """

        try:
            pet = (
                cls.pet_model.objects.select_related(
                    "pet_type", "pet_sex", "shelter"
                )
                .filter(pet_uuid=uuid)
                .first()
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        if not pet:
            raise ResourceNotFoundError(
                code="pet_not_found",
                detail={
                    "message": "pet with the following UUID not found.",
                    "uuid": uuid,
                },
            )

        return pet
