from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.db.models import Model
from typing import Any, Dict
from apps.emails.domain.constants import SubjectsMail
from apps.emails.domain.abstractions import IEmailsSentRepository
from apps.users.domain.abstractions import IUserRepository
from apps.emails.template_paths import ADOPTION_APPLICATION_EMAIL_BODY


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
    def _get_email_context(data: Dict[str, str]) -> Dict[str, Any]:
        return {
            key: (
                value.capitalize()
                if key in ["pet_name", "user_name"]
                else value
            )
            for key, value in data.items()
        }

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
                    "pet_name": data["pet_name"].capitalize(),
                    "user_name": data["user_name"].capitalize(),
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
        Send an email to the user with the activation link. The link contains a token that
        is used to activate the user's account.

        #### Parameters:
        - data: Data to compose the email.
        """

        message = self._get_message(data)
        shelter_uuid = data.pop("shelter_uuid")
        shelter = self._user_repository.get_shelter(base_user=shelter_uuid)
        self._compose_and_dispatch(
            message=message, addressee=shelter.base_user.email
        )
        self._email_repository.add_record(
            data={
                "subject": message["subject"],
                "message": data["message"],
                "addressee": shelter.base_user.email,
                "additional_info": {
                    "pet_name": data["pet_name"],
                    "user_name": data["user_name"],
                    "user_email": data["user_email"],
                    "user_phone": data["user_phone"].__str__(),
                },
            }
        )
