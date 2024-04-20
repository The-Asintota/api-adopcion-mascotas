from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from typing import Dict, Any
from apps.emails.infrastructure.serializers import AdoptionPetSerializer
from apps.emails.infrastructure.db import EmailsSentRepository
from apps.emails.use_case import AdoptionPetUseCase
from apps.emails.endpoint_schemas.adoption_pet import PostSchema
from apps.users.infrastructure.db import UserRepository


class AdoptionPetAPIView(generics.GenericAPIView):
    """
    API View for sending an email to the shelter when a user applies for adoption.
    """

    authentication_classes = []
    permission_classes = []
    serializer_class = AdoptionPetSerializer
    application_class = AdoptionPetUseCase

    def _handle_valid_request(self, data: Dict[str, Any]) -> Response:

        self.application_class(
            email_repository=EmailsSentRepository,
            user_repository=UserRepository,
        ).send_email(data=data)

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def _handle_invalid_request(serializer: Serializer) -> Response:

        return Response(
            data={
                "code": "invalid_request_data",
                "detail": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
            content_type="application/json",
        )

    @PostSchema
    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        Handle POST requests for sending an email to the shelter when a user applies for adoption.

        This method allows the sending of an email to the shelter when a user applies
        for adoption. It waits for a POST request with the required data, validates
        the information, and then sends the email if the data is valid or returns an
        error response if it is not.
        """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return self._handle_valid_request(data=serializer.validated_data)

        return self._handle_invalid_request(serializer=serializer)
