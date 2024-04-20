from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from typing import Dict, Any
from apps.emails.infrastructure.serializers import AdoptionPetSerializer
from apps.emails.infrastructure.db import EmailsSentRepository
from apps.emails.use_case import AdoptionPetUseCase
from apps.users.infrastructure.db import UserRepository


class AdoptionPetAPIView(generics.GenericAPIView):

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

    def post(self, request: Request, *args, **kwargs) -> Response:

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return self._handle_valid_request(data=serializer.validated_data)

        return self._handle_invalid_request(serializer=serializer)
