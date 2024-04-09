from rest_framework_simplejwt.tokens import Token
from abc import ABC, abstractmethod
from typing import Dict, Any, Protocol
from apps.users.domain.typing import JWToken
from apps.users.models import User, Shelter, Admin, JWT, JWTBlacklisted


class IUserRepository(ABC):
    """
    IUserRepository is an abstract base class that represents a user repository.
    Subclasses should implement the `insert` and `get_user` methods.
    """

    model_user = User
    model_shelter = Shelter
    model_admin = Admin

    @classmethod
    @abstractmethod
    def _create_user(cls, email: str, password: str) -> User:
        """
        Inserts a new user into the database.
        """

        pass

    @classmethod
    @abstractmethod
    def create_shelter(cls, data: Dict[str, Any]) -> None:
        """
        Insert a new shelter into the database.

        Parameters:
        - data: A dictionary containing the shelter data.
        """

        pass

    @classmethod
    @abstractmethod
    def get_shelter(cls, **filters) -> Shelter:
        """
        Retrieve a shelter from the database based on the provided filters.
        """

        pass

    @classmethod
    @abstractmethod
    def create_admin(cls, data: Dict[str, Any]) -> None:
        """
        Insert a new admin into the database.

        Parameters:
        - data: A dictionary containing the admin data.
        """

        pass


class IJWTRepository(ABC):
    """
    IJWTRepository is an abstract base class that represents a JWT repository.
    Subclasses should implement the `get_token`, `get_tokens_user`,
    `add_to_checklist` and `add_to_blacklist` methods.
    """

    model_token = JWT
    model_blacklist = JWTBlacklisted

    @classmethod
    @abstractmethod
    def get_token(cls, **filters) -> JWT:
        """
        Retrieve a token from the database based on the provided filters.

        Parameters:
        - filters: Keyword arguments that define the filters to apply.
        """

        pass

    @classmethod
    @abstractmethod
    def add_to_checklist(cls, token: JWToken, user: User) -> None:
        """
        Add a token to the checklist.

        Parameters:
        - token: A JWToken.
        - user: An instance of the User model.
        """

        pass

    @classmethod
    @abstractmethod
    def add_to_blacklist(cls, token: JWT) -> None:
        """
        Add a token to the blacklist.

        Parameters:
        - token: An instance of the JWT model.
        """

        pass


class ITokenClass(Protocol):
    """
    Interface that defines the methods that a class must implement to be used as a
    JWT class.
    """

    def get_token(self, user: User) -> Token:
        """
        This method should return a JWT token for the given user.

        Parameters:
        - user: An instance of the User model. The user for which to generate the
        token.
        """

        ...
