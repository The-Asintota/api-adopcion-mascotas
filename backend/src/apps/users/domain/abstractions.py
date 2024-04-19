from rest_framework_simplejwt.tokens import Token
from django.db.models import QuerySet, Model
from typing import Dict, Any, Protocol
from apps.users.domain.typing import JWToken, StrUUID
from apps.users.models import BaseUser, JWT, Pet, Shelter, AdminUser


class IUserRepository(Protocol):
    """
    IUserRepository is a protocol that defines the interface for a user repository.

    This interface represents a contract for the `Shelter` and `AdminUser`
    model repositories, ensuring that they provide the methods necessary to manage
    shelters, and admins in the database.
    """

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

        ...

    @classmethod
    def get_user(cls, uuid: StrUUID = None, **other_fields) -> Model:
        """
        Retrieve a user from the database according to the provided filters, the
        search is performed on the `UserDIrectory` table.

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

        ...

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

        ...

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

        ...


class IJWTRepository(Protocol):
    """
    IJWTRepository is a protocol that defines the interface for a JWT repository.

    This interface represents a contract for the `JWT` and `JWTBlacklisted` model
    repository, ensuring that they provide the methods necessary to manage JSON Web
    Tokens in the database.
    """

    @classmethod
    def get_token(cls, **filters) -> JWT:
        """
        Retrieve a token from the database based on the provided filters.

        Parameters:
        - filters: Keyword arguments that define the filters to apply.
        """

        ...

    @classmethod
    def add_to_checklist(cls, token: JWToken, user: BaseUser) -> None:
        """
        Associate a JSON Web Token with a user by adding it to the checklist.

        This way you can keep track of which tokens are associated with which
        users, and which tokens created are pending expiration or invalidation.

        Parameters:
        - token: A JWToken.
        - user: An instance of the BaseUser model.
        """

        ...

    @classmethod
    def add_to_blacklist(cls, token: JWT) -> None:
        """
        Invalidates a JSON Web Token by adding it to the blacklist.

        Once a token is blacklisted, it can no longer be used for authentication purposes until it is removed from the blacklist or has expired.

        Parameters:
        - token: An instance of the `JWT` model.
        """

        ...


class ITokenClass(Protocol):
    """
    Interface that defines the methods that a class must implement to be used as a
    JWT class.
    """

    def get_token(self, user: BaseUser) -> Token:
        """
        This method should return a JWT token for the given user.

        Parameters:
        - user: An instance of the BaseUser model. The user for which to generate
        the token.
        """

        ...


class IPetRepository(Protocol):
    """
    Interface that defines the methods that a class must implement to be used as a
    pet repository.
    """

    @classmethod
    def create(cls, data: Dict[str, Any]) -> None:
        """
        Insert a new pet into the database.

        #### Parameters:
        - data: A dictionary containing the pet data.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        """

        ...

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

        ...
