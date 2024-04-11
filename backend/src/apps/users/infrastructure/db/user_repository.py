from django.db.models import Q
from django.db import OperationalError
from typing import Dict
from apps.users.models import (
    BaseUser,
    Shelter,
    AdminUser,
    CustomUserManager,
)
from apps.exceptions import DatabaseConnectionError, ResourceNotFoundError


class UserRepository:
    """
    UserRepository is a class that provides an abstraction of the database
    operations for the `Shelter` and `AdminUser` models.
    """

    base_user_model = BaseUser
    shelter_model = Shelter
    admin_model = AdminUser

    @classmethod
    def _create_base_user(cls, email: str, password: str) -> BaseUser:
        """
        Inserts a new user into the database.
        """

        try:
            user_manager: CustomUserManager = cls.base_user_model.objects
            base_user = user_manager.create_base_user(
                email=email,
                password=password,
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        return base_user

    @classmethod
    def create_shelter(cls, data: Dict[str, str]) -> None:
        """
        Insert a new shelter into the database.

        Parameters:
        - data: A dictionary containing the shelter data.
        """

        base_user = cls._create_base_user(
            email=data["email"], password=data["password"]
        )
        del data["email"]
        del data["password"]

        try:
            cls.shelter_model.objects.create(
                base_user=base_user,
                **data,
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

    @classmethod
    def get_shelter(cls, **filters) -> Shelter:
        """
        Retrieve a shelter from the database based on the provided filters.
        """

        query_params = Q()
        fields_base_user_model = [
            field.name for field in cls.base_user_model._meta.get_fields()
        ]

        for field, value in filters.items():
            if field in fields_base_user_model:
                query_params &= Q(**{f"base_user__{field}": value})
                continue
            else:
                query_params &= Q(**{field: value})

        try:
            shelter = (
                cls.shelter_model.objects.select_related("base_user")
                .filter(query_params)
                .first()
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        if not shelter:
            raise ResourceNotFoundError(
                detail={
                    "message": "shelter with the following filters not found.",
                    "filters": filters,
                },
                code="shelter_not_found",
            )

        return shelter

    @classmethod
    def create_admin(cls, data: Dict[str, str]) -> None:
        """
        Insert a new admin into the database.

        Parameters:
        - data: A dictionary containing the admin data.
        """

        base_user = cls._create_base_user(
            email=data["email"], password=data["password"]
        )
        del data["email"]
        del data["password"]

        try:
            cls.admin_model.objects.create(
                base_user=base_user,
                **data,
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()
