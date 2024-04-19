from django.db import OperationalError
from django.db.models import Q, QuerySet
from typing import Dict, Any
from apps.users.infrastructure.db import UserRepository
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
    def get_pet(cls, all: bool, **filters) -> QuerySet[Pet]:
        """
        Retrieve a pet from the database based on the provided filters.

        #### Parameters:
        - filters: Keyword arguments that define the filters to apply.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        - ResourceNotFoundError: If no pets are found in the database.
        """

        query_params = cls._create_query_params(**filters)

        try:
            objs = cls.pet_model.objects.select_related(
                "pet_type", "pet_sex", "shelter"
            )
            pet_list = (
                objs.filter(query_params).defer("date_joined")
                if not all
                else objs.all().defer("date_joined")
            )

        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        if not pet_list.exists():
            raise ResourceNotFoundError(
                code="pet_not_found",
                detail="No pets were found with the provided filters.",
            )

        return pet_list
