from django.db import OperationalError
from typing import Dict, Any
from apps.users.models import Pet
from apps.exceptions import DatabaseConnectionError


class PetRepository:
    """
    PetRepository is a class that provides an abstraction of the database
    operations for the `Pet` model.
    """

    model = Pet

    @classmethod
    def create(cls, data: Dict[str, Any]) -> None:
        """
        Insert a new pet into the database.

        Parameters:
        - data: A dictionary containing the pet data.
        """

        try:
            cls.model.objects.create(**data)
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()
