from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from apps.emails.infrastructure.serializers import EmailsListReadOnlySerializer
from apps.emails.infrastructure.db import EmailsSentRepository
from apps.emails.use_case import GetAllEmailsUseCase
from apps.emails.endpoint_schemas.get_all_emails import GetAllEmailsSentSchema
from apps.users.infrastructure.permissions import IsAuthenticatedAdmin
from apps.authentication import JWTAuthentication


class EmailsSentListAPIView(generics.GenericAPIView):
    """
    API View for retrieving all the emails sent.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAdmin]
    serializer_class = EmailsListReadOnlySerializer
    application_class = GetAllEmailsUseCase

    @GetAllEmailsSentSchema
    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Handles the GET request to retrieve all the emails sent.

        This method returns a paginated response with the list of emails sent.
        """

        email_list = self.application_class(
            email_repository=EmailsSentRepository
        ).get_all()

        # Paginate the response
        page = self.paginate_queryset(email_list)
        paginated_response = self.get_paginated_response(page)
        pagination_data = paginated_response.data

        serializer = self.serializer_class(instance=email_list, many=True)

        return Response(
            data={
                "count": pagination_data.get("count"),
                "next": pagination_data.get("next"),
                "previous": pagination_data.get("previous"),
                "results": serializer.data,
            },
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
