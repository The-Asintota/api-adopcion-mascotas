from django.db import OperationalError
from typing import Dict
from apps.users.domain.abstractions import IUserRepository
from apps.users.models import User, Shelter
from apps.exceptions import DatabaseConnectionError


class UserRepository(IUserRepository):
    """
    UserRepository is a class that provides an abstraction of the database
    operations for the `User` and `Shelter` models.
    """

    model_user = User
    model_shelter = Shelter

    @classmethod
    def _create_user(cls, data: Dict[str, str]) -> User:
        """
        Inserts a new user into the database.
        """

        try:
            user = cls.model_user.objects.create_user(
                email=data["email"],
                password=data["password"],
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

        user = cls._create_user(data=data)
        try:
            cls.model_shelter.objects.create(
                user=user,
                **data,
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()
