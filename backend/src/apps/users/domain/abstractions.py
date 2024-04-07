from abc import ABC, abstractmethod
from typing import Dict, Any
from apps.users.models import User, Shelter


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
