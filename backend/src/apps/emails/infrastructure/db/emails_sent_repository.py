from django.db import OperationalError
from typing import Dict, Any
from apps.emails.models import EmailsSent
from apps.exceptions import DatabaseConnectionError


class EmailsSentRepository:
    """
    EmailsSentRepository is a class that provides an abstraction of the database
    operations for the `EmailsSent` model.
    """

    model = EmailsSent

    @classmethod
    def add_record(cls, data: Dict[str, Any]) -> None:
        """
        Adds the record to the sent email database.

        #### Parameters:
        - data: A dictionary containing the message data.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        """

        try:
            cls.model.objects.create(**data)
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()
