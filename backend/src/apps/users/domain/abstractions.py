from abc import ABC, abstractmethod
from typing import Dict, Any
from apps.users.models import User


class IUserRepository(ABC):
    """
    IUserRepository is an abstract base class that represents a user repository.
    Subclasses should implement the `insert` and `get_user` methods.
    """

    model: User

    @classmethod
    @abstractmethod
    def create_shelter(cls, data: Dict[str, Any]) -> None:
        """
        Insert a new shelter into the database.

        Parameters:
        - data: A dictionary containing the shelter data.
        """

        pass
