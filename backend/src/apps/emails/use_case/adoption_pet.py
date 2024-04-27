from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.db.models import Model
from apps.emails.domain.constants import SubjectsMail
from apps.emails.domain.abstractions import IEmailsSentRepository
from apps.emails.template_paths import ADOPTION_APPLICATION_EMAIL_BODY
from apps.users.domain.abstractions import IUserRepository
from apps.exceptions import ResourceNotFoundError
from typing import Any, Dict


class AdoptionPetUseCase:
    """
    Use case that is responsible for sending an email to the shelter when a user
    applies for adoption.

    This class interacts with instances of classes implementing the
    `IEmailsSentRepository` and `IUserRepository` interfaces, which are injected at
    the point of use.
    """

    def __init__(
        self,
        email_repository: IEmailsSentRepository,
        user_repository: IUserRepository,
        smtp_class=None,
    ) -> None:
        self._email_repository = email_repository
        self._user_repository = user_repository
        self._smtp_class = smtp_class or EmailMessage

    @staticmethod
    def _get_message(data: Dict[str, str]) -> Dict[str, Any]:
        """
        Construct the email body and subject.

        #### Parameters:
        - data: Data to compose the email.
        """

        return {
            "subject": SubjectsMail.ADOPTION_APPLICATION.value,
            "body": render_to_string(
                template_name=ADOPTION_APPLICATION_EMAIL_BODY,
                context={
                    "pet_name": data["pet_name"],
                    "user_name": data["user_name"],
                    "user_email": data["user_email"],
                    "user_phone": data["user_phone"],
                    "message": data["message"],
                },
            ),
        }

    def _compose_and_dispatch(
        self, message: Dict[str, Any], addressee: Model
    ) -> None:
        """
        Compose and send an email.

        #### Parameters:
        - data: Data to compose the email.
        - addressee: User to send the email.
        """

        email = self._smtp_class(to=[addressee], **message)
        email.content_subtype = "html"
        email.send()

    def send_email(self, data: Dict[str, Any]) -> None:
        """
        Send an email to the user with the activation link. The link contains a token
        that is used to activate the user's account.

        #### Parameters:
        - data: Data to compose the email.

        #### Raises:
        - ResourceNotFoundError: If no shelter is found with the provided UUID.
        """

        shelter = self._user_repository.get(
            uuid=data.pop("shelter_uuid")
        ).first()

        if not shelter:
            raise ResourceNotFoundError(
                code="shelter_not_found",
                detail="No shelter found with the provided UUID.",
            )

        message = self._get_message(data)
        self._compose_and_dispatch(message=message, addressee=shelter.email)
        self._email_repository.add_record(
            data={
                "subject": message["subject"],
                "message": data["message"],
                "addressee": shelter.email,
                "additional_info": {
                    "pet_name": data["pet_name"],
                    "user_name": data["user_name"],
                    "user_email": data["user_email"],
                    "user_phone": data["user_phone"].__str__(),
                },
            }
        )
