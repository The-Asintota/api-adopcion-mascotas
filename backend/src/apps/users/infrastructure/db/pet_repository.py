from django.db import OperationalError
from django.db.models import Q, QuerySet
from typing import Dict, Any
from apps.users.infrastructure.db import UserRepository
from apps.users.models import Pet, PetType, PetSex
from apps.exceptions import DatabaseConnectionError, ResourceNotFoundError


class PetRepository:
    """
    PetRepository is a class that provides an abstraction of the datashelterbase
    operations for the `Pet` model.
    """

    pet_model = Pet
    pet_type_model = PetType
    pet_sex_model = PetSex
    user_repository = UserRepository
    related_fields = {
        field.name: "pet_type" for field in pet_type_model._meta.get_fields()
    }
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
        - ResourceNotFoundError: If the shelter provided does not exist.
        """

        shelter = cls.user_repository.get(uuid=data.pop("shelter")).first()

        if not shelter:
            raise ResourceNotFoundError(
                code="shelter_not_found",
                detail="The shelter provided does not exist.",
            )

        pet_type = data.pop("pet_type")
        pet_sex = data.pop("pet_sex")

        try:
            cls.pet_model.objects.create(
                pet_type=cls.pet_type_model.objects.get(type=pet_type),
                pet_sex=cls.pet_sex_model.objects.get(sex=pet_sex),
                shelter=shelter,
                **data,
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

    @classmethod
    def get(cls, all: bool, **filters) -> QuerySet[Pet]:
        """
        Retrieve a pet from the database based on the provided filters.

        #### Parameters:
        - filters: Keyword arguments that define the filters to apply.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        """

        query_params = cls._create_query_params(**filters)

        try:
            objs = cls.pet_model.objects.defer(
                "date_joined",
                "shelter__password",
                "shelter__last_login",
                "shelter__is_superuser",
                "shelter__date_joined",
            ).select_related("pet_type", "pet_sex", "shelter")
            pet_list = objs.filter(query_params) if not all else objs.all()
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        return pet_list
