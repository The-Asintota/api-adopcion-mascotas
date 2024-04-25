from django.db.models import Model, QuerySet
from django.db import OperationalError
from typing import Dict
from apps.users.domain.constants import UserRoles
from apps.users.models import (
    ShelterProfile,
    AdminProfile,
    User,
    CustomUserManager,
)
from apps.exceptions import DatabaseConnectionError


class UserRepository:
    """
    UserRepository is a class that provides an abstraction of the database
    operations for the `User` model.
    """

    role_models = dict(
        [
            (UserRoles.SHELTER.value, ShelterProfile),
            (UserRoles.ADMIN_USER.value, AdminProfile),
        ]
    )
    user_model = User

    @classmethod
    def create(cls, data: Dict[str, str], role: str) -> None:
        """
        Insert a new user into the database.

        #### Parameters:
        - data: A dictionary containing the user data.
        - role: The role of the user to be created.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        """

        email = data.pop("email")
        password = data.pop("password")
        user_manager: CustomUserManager = cls.user_model.objects

        try:
            model = cls.role_models[role]
            profie = model.objects.create(**data)
            user_manager.create_user(
                email=email, password=password, content_object=profie
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

    @classmethod
    def get(cls, **filters) -> QuerySet[User]:
        """
        Retrieves a user from the database according to the provided filters.

        #### Parameters:
        - filters: Keyword arguments that define the filters to apply.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        """

        try:
            user_list = cls.user_model.objects.filter(**filters).defer(
                "password", "last_login", "is_superuser", "date_joined"
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        return user_list

    @classmethod
    def get_profile_data(cls, role: str, **filters) -> QuerySet[Model]:
        """
        Retrieves the related data of a user profile from the database according to the
        provided filters.

        #### Parameters:
        - role: The role of the user.
        - filters: Keyword arguments that define the filters to apply.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        """

        model = cls.role_models[role]

        try:
            related_data = model.objects.filter(**filters)
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        return related_data
