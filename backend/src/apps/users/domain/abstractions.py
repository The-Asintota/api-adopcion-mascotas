from abc import ABC, abstractmethod
from typing import Dict, Any
from apps.users.domain.typing import JWTPayload, JWToken
from apps.users.models import User, Shelter, JWT, JWTBlacklisted


class IUserRepository(ABC):
    """
    IUserRepository is an abstract base class that represents a user repository.
    Subclasses should implement the `insert` and `get_user` methods.
    """

    model_user = User
    model_shelter = Shelter

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
    def add_to_checklist(
        cls, payload: JWTPayload, token: JWToken, user: User
    ) -> None:
        """
        Add a token to the checklist.

        Parameters:
        - payload: A JWTPayload instance that represents the payload of a JWT.
        - token: A JWTType instance representing a JWT.
        - user: A User instance representing the user.
        """

        pass

    @classmethod
    @abstractmethod
    def add_to_blacklist(cls, token: JWT) -> None:
        """
        Add a token to the blacklist.

        Parameters:
        - token: A JWTType instance representing a JWT.
        """

        pass
