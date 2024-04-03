from abc import abstractclassmethod, ABC
from typing import Dict, Any
from apps.users.models import User


class IUserRepository(ABC):
    """
    IUserRepository is an abstract base class that represents a user repository.
    Subclasses should implement the `insert` and `get_user` methods.
    """

    model: User

    @abstractclassmethod
    def insert(cls, data: Dict[str, Any]) -> None:
        """
        Insert a new user into the database.

        Parameters:
        - data: A dictionary containing the user data.
        """

        pass
