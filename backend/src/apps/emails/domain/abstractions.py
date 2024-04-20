from django.db.models import QuerySet
from typing import Dict, Any, Protocol
from apps.emails.models import EmailsSent


class IEmailsSentRepository(Protocol):
    """
    Interface that defines the methods that a class must implement to be used as a
    email sent repository.

    This interface defines a contract that must be followed by the repository
    that will be responsible for storing the sent emails.
    """

    @classmethod
    def add_record(cls, data: Dict[str, Any]) -> None:
        """
        Adds the record to the sent email database.

        #### Parameters:
        - data: A dictionary containing the message data.

        #### Raises:
        - DatabaseConnectionError: If there is an operational error with the database.
        """

        ...

    @classmethod
    def get_all(cls) -> QuerySet[EmailsSent]:
        """
        Get all the records from the sent email database.
        """

        ...
