from django.db.models import QuerySet
from apps.emails.domain.abstractions import IEmailsSentRepository
from apps.emails.models import EmailsSent


class GetAllEmailsUseCase:
    """
    Use case that is responsible for getting all the emails sent.

    This class interacts with instances of classes implementing the
    `IEmailsSentRepository` interface, which are injected at the point of use.
    """

    def __init__(self, email_repository: IEmailsSentRepository) -> None:
        self._email_repository = email_repository

    def get_all(self) -> QuerySet[EmailsSent]:
        """
        Get all the emails sent.
        """

        return self._email_repository.get_all()
