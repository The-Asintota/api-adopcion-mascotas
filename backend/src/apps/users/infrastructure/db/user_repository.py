from django.db.models import Q
from django.db import OperationalError
from typing import Dict
from apps.users.domain.abstractions import IUserRepository
from apps.users.models import User, Shelter
from apps.exceptions import DatabaseConnectionError, UserNotFoundError


class UserRepository(IUserRepository):
    """
    UserRepository is a class that provides an abstraction of the database
    operations for the `User` and `Shelter` models.
    """

    @classmethod
    def _create_user(cls, email: str, password: str) -> User:
        """
        Inserts a new user into the database.
        """

        try:
            user = cls.model_user.objects.create_user(
                email=email,
                password=password,
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        return user

    @classmethod
    def create_shelter(cls, data: Dict[str, str]) -> None:
        """
        Insert a new shelter into the database.

        Parameters:
        - data: A dictionary containing the shelter data.
        """

        user = cls._create_user(email=data["email"], password=data["password"])
        del data["email"]
        del data["password"]
        try:
            cls.model_shelter.objects.create(
                user=user,
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

        query = Q()
        fields_user_model = [
            field.name for field in cls.model_user._meta.get_fields()
        ]
        for field, value in filters.items():
            if field in fields_user_model:
                query &= Q(**{f"user__{field}": value})
            else:
                query &= Q(**{field: value})
        try:
            shelter = (
                cls.model_shelter.objects.select_related("user")
                .filter(query)
                .first()
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()
        if not shelter:
            raise UserNotFoundError(
                detail=f'shelter {filters.get("uuid", None) or filters.get("email", None) or ""} not found.',
            )

        return shelter
