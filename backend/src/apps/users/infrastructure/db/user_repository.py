from django.db.models import Q, Model
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

    models = {
        "base_user": BaseUser,
        "shelter": Shelter,
        "admin": AdminUser,
    }

    @classmethod
    def _get_model(cls, name: str) -> Model:
        """
        Method to get the model class based on the provided model name.
        """

        return cls.models[name]

    @classmethod
    def _create_base_user(cls, email: str, password: str) -> BaseUser:
        """
        Inserts a new user into the database.

        Raises:
            - DatabaseConnectionError: If there is an operational error with the database.
        """

        try:
            user_manager: CustomUserManager = cls._get_model(
                name="base_user"
            ).objects
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
    def create_user(cls, data: Dict[str, str], role: str) -> None:
        """
        Insert a new user into the database.

        Parameters:
            - data: A dictionary containing the user data.

        Raises:
            - DatabaseConnectionError: If there is an operational error with the database.
        """

        base_user = cls._create_base_user(
            email=data["email"], password=data["password"]
        )
        del data["email"]
        del data["password"]

        try:
            cls._get_model(name=role).objects.create(
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

        Raises:
            - DatabaseConnectionError: If there is an operational error with the database.
            - ResourceNotFoundError: If no JWT matches the provided filters.
        """

        query_params = Q()
        fields_base_user_model = [
            field.name
            for field in cls._get_model(name="base_user")._meta.get_fields()
        ]

        for field, value in filters.items():
            if field in fields_base_user_model:
                query_params &= Q(**{f"base_user__{field}": value})
                continue
            query_params &= Q(**{field: value})

        try:
            shelter = (
                cls._get_model(name="shelter")
                .objects.select_related("base_user")
                .filter(query_params)
                .first()
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        if not shelter:
            raise ResourceNotFoundError(
                code="shelter_not_found",
                detail={
                    "message": "shelter with the following filters not found.",
                    "filters": filters,
                },
            )

        return shelter

    @classmethod
    def get_admin(cls, **filters) -> AdminUser:
        """
        Retrieve a admin user from the database based on the provided filters.

        Raises:
            - DatabaseConnectionError: If there is an operational error with the database.
            - ResourceNotFoundError: If no JWT matches the provided filters.
        """

        query_params = Q()
        fields_base_user_model = [
            field.name
            for field in cls._get_model(name="base_user")._meta.get_fields()
        ]

        for field, value in filters.items():
            if field in fields_base_user_model:
                query_params &= Q(**{f"base_user__{field}": value})
                continue
            query_params &= Q(**{field: value})

        try:
            admin = (
                cls._get_model(name="admin")
                .objects.select_related("base_user")
                .filter(query_params)
                .first()
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        if not admin:
            raise ResourceNotFoundError(
                code="admin_not_found",
                detail={
                    "message": "admin with the following filters not found.",
                    "filters": filters,
                },
            )

        return admin
