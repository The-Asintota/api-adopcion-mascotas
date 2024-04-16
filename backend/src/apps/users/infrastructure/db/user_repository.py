from django.db.models import Model, Q
from django.db import OperationalError
from typing import Dict
from apps.users.domain.typing import StrUUID
from apps.users.models import (
    BaseUser,
    Shelter,
    AdminUser,
    CustomUserManager,
    UserDirectory,
)
from apps.exceptions import DatabaseConnectionError, ResourceNotFoundError


class UserRepository:
    """
    UserRepository is a class that provides an abstraction of the database
    operations for the `Shelter` and `AdminUser` models.
    """

    role_models = {
        "shelter": Shelter,
        "admin": AdminUser,
    }
    related_fields = {
        field.name: "base_user" for field in BaseUser._meta.get_fields()
    }
    user_directory_model = UserDirectory
    base_user_model = BaseUser

    @classmethod
    def _get_model(cls, name: str) -> Model:
        """
        Method to get the model class based on the provided model name.
        """

        return cls.role_models[name]

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
    def create_user(cls, data: Dict[str, str], role: str) -> None:
        """
        Insert a new user into the database and add it to the directory.

        #### Parameters:
        - data: A dictionary containing the user data.
        - role: The role of the user to be created.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        """

        email = data.pop("email")
        password = data.pop("password")
        user_manager: CustomUserManager = cls.base_user_model.objects

        try:
            user = cls._get_model(name=role).objects.create(
                base_user=user_manager.create_base_user(
                    email=email,
                    password=password,
                ),
                **data,
            )
            cls.user_directory_model.objects.create(content_object=user)
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

    @classmethod
    def get_user(cls, uuid: StrUUID = None, **other_fields) -> Model:
        """
        Retrieves a user from the database according to the provided filters, the
        search is performed on the `UserDirectory` table. This method should be used
        if you do `not know the role` of the user you want to search for.

        #### Parameters:
        - uuid: The UUID of the user to retrieve.
        - filters: Keyword arguments that define the filters to apply.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        - ResourceNotFoundError: If no shelters matches the provided filters.
        - ValueError: If the `uuid` and `email` fields are not provided.

        #### Returns:
        - An instance of the `Shelter` or `AdminUser` model.
        """

        if (uuid is None and "email" not in other_fields) or (
            uuid is not None and "email" in other_fields
        ):
            raise ValueError("Either uuid or email must be provided.")

        try:
            if not uuid:
                base_user = cls.base_user_model.objects.filter(
                    **other_fields
                ).first()
                uuid = base_user.uuid if base_user else None
            generic_relationship = (
                cls.user_directory_model.objects.select_related("content_type")
                .filter(user_uuid=uuid)
                .first()
            )

            if generic_relationship:
                user = (
                    generic_relationship.content_type.model_class()
                    .objects.select_related("base_user")
                    .filter(base_user=uuid)
                    .first()
                )
            else:
                user = None
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        if not user:
            raise ResourceNotFoundError(
                code="user_not_found",
                detail=f"user with the {uuid or other_fields} was not found.",
            )

        return user

    @classmethod
    def get_shelter(cls, **filters) -> Shelter:
        """
        Retrieve a shelter from the database based on the provided filters.

        #### Parameters:
        - filters: Keyword arguments that define the filters to apply.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        - ResourceNotFoundError: If no JWT matches the provided filters.
        """

        try:
            shelter = (
                cls._get_model(name="shelter")
                .objects.select_related("base_user")
                .filter(cls._create_query_params(**filters))
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

        #### Parameters:
        - filters: Keyword arguments that define the filters to apply.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        - ResourceNotFoundError: If no JWT matches the provided filters.
        """

        try:
            admin = (
                cls._get_model(name="admin")
                .objects.select_related("base_user")
                .filter(cls._create_query_params(**filters))
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
