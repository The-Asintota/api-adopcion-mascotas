from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status, permissions
from typing import Dict, Any, Callable
from apps.users.infrastructure.serializers import (
    PetReadOnlySerializer,
    PetSerializer,
)
from apps.users.infrastructure.db import PetRepository
from apps.users.use_case import PetUseCase
from apps.users.endpoint_schemas.register_pet import GetEndPointSchema


class PetAPIView(generics.GenericAPIView):
    """
    API View for registering a new pet. This view handles the "POST" request to
    create a new pet in the system.
    """

    authentication_classes = ()
    pet_use_case = PetUseCase(pet_repository=PetRepository)
    application_mapping = {
        "GET": pet_use_case.get_pet,
        "POST": pet_use_case.create_pet,
    }
    permission_mapping = {
        "GET": [],
        "POST": [],
    }
    serializer_mapping = {
        "GET": PetReadOnlySerializer,
        "POST": PetSerializer,
    }

    def get_permissions(self):
        """
        Get the permissions based on the request method.
        """

        try:
            permission_classes = self.permission_mapping[self.request.method]
        except KeyError:
            raise ValueError(f"Method {self.request.method} not allowed")

        return [permission() for permission in permission_classes]

    def get_serializer_class(self, **attributes) -> Serializer:
        """
        Get the serializer class based on the request method.
        """

        try:
            serializer = self.serializer_mapping[self.request.method]
        except KeyError:
            raise ValueError(f"Method {self.request.method} not allowed")

        return serializer(**attributes)

    def get_application_class(self) -> Callable:
        """
        Get the application class based on the request method.
        """

        try:
            application_class = self.application_mapping[self.request.method]
        except KeyError:
            raise ValueError(f"Method {self.request.method} not allowed")

        return application_class

    def _handle_valid_request(self, data: Dict[str, Any]) -> Response:

        self.get_application_class()(data=data)

        return Response(status=status.HTTP_201_CREATED)

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

    @GetEndPointSchema
    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        Handle POST requests for pet registration.

        This method allows the registration of a new pet. It waits for a POST
        request with a pet's data, validates the information, and then creates
        a new record if the data is valid or returns an error response if it is not.
        """

        serializer = self.get_serializer_class(data=request.data)
        if serializer.is_valid():
            return self._handle_valid_request(
                data=serializer.validated_data,
            )

        return self._handle_invalid_request(serializer=serializer)

    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Handle GET requests to retrieve all pets from the database.
        Returns a paginated response with the pet information.
        """

        application_class = self.get_application_class()

        if kwargs.get("shelter_uuid", None):
            pet_list = application_class(shelter=kwargs.get("shelter_uuid"))
        else:
            pet_list = application_class(all=True)
        page = self.paginate_queryset(pet_list)
        paginated_response = self.get_paginated_response(page)
        pagination_data = paginated_response.data
        serializer = self.get_serializer_class(instance=pet_list, many=True)

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
