from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status, exceptions, permissions
from typing import List, Dict, Any, Callable
from apps.users.infrastructure.serializers import (
    PetReadOnlySerializer,
    PetSerializer,
)
from apps.users.infrastructure.db import PetRepository
from apps.users.infrastructure.permissions import IsAuthenticatedShelter
from apps.users.infrastructure.exceptions import NotAuthenticated
from apps.users.use_case import PetUseCase
from apps.users.endpoint_schemas.pet.views import (
    CreateUpdatePetSchema,
    GetAllPetsSchema,
    GetPetByShelterSchema,
)
from apps.users.authentication import JWTAuthentication


class PetAPIView(generics.GenericAPIView):
    """
    API View for registering a new pet. This view handles the "POST" request to
    create a new pet in the system.
    """

    pet_use_case = PetUseCase(pet_repository=PetRepository)
    authentication_mapping = {
        "GET": [],
        "POST": [JWTAuthentication],
    }
    application_mapping = {
        "GET": pet_use_case.get_pet,
        "POST": pet_use_case.create_pet,
    }
    permission_mapping = {
        "GET": [],
        "POST": [IsAuthenticatedShelter],
    }
    serializer_mapping = {
        "GET": PetReadOnlySerializer,
        "POST": PetSerializer,
    }

    def get_authenticators(self):
        """
        Instantiates and returns the list of authenticators that this view can use.
        """

        try:
            authentication_classes = self.authentication_mapping[
                self.request.method
            ]
        except AttributeError:
            authentication_classes = []

        return [auth() for auth in authentication_classes]

    def get_permissions(self) -> List[permissions.BasePermission]:
        """
        Get the permissions based on the request method.
        """

        try:
            permission_classes = self.permission_mapping[self.request.method]
        except KeyError:
            raise ValueError(f"Method {self.request.method} not allowed")

        return [permission() for permission in permission_classes]

    def get_serializer_class(self) -> Serializer:
        """
        Get the serializer class based on the request method.
        """

        try:
            serializer = self.serializer_mapping[self.request.method]
        except KeyError:
            raise ValueError(f"Method {self.request.method} not allowed")

        return serializer

    def get_application_class(self) -> Callable:
        """
        Get the application class based on the request method.
        """

        try:
            application_class = self.application_mapping.get(
                self.request.method, PetSerializer
            )
        except KeyError:
            raise ValueError(f"Method {self.request.method} not allowed")

        return application_class

    def permission_denied(self, request: Request, message=None, code=None):
        """
        If request is not permitted, determine what kind of exception to raise.
        """

        if request.authenticators and not request.successful_authenticator:
            raise NotAuthenticated(code=code, detail=message)
        raise exceptions.PermissionDenied(code=code, detail=message)

    def _handle_valid_request(self, data: Dict[str, Any]) -> Response:

        application = self.get_application_class()
        application(data=data)

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

    @CreateUpdatePetSchema
    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        Handle POST requests for pet registration.

        This method allows the registration of a new pet. It waits for a POST
        request with a pet's data, validates the information, and then creates
        a new record if the data is valid or returns an error response if it is not.
        """

        serializer_class = self.get_serializer_class()
        serializer: Serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            shelter_uuid = request.decoded_token_access["payload"]["user"]
            data = serializer.validated_data
            data.update({"shelter": shelter_uuid})

            return self._handle_valid_request(data=data)

        return self._handle_invalid_request(serializer=serializer)

    @GetAllPetsSchema
    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Handles GET requests to retrieve all pets from the database.

        This method allows retrieving all pets from the database. It paginates the
        response with a total of 10 items and returns a list of pets along with the
        pagination data.
        """

        application_class = self.get_application_class()
        pet_list = application_class(all=True)

        # Paginate the response
        page = self.paginate_queryset(pet_list)
        paginated_response = self.get_paginated_response(page)
        pagination_data = paginated_response.data

        serializer_class = self.get_serializer_class()
        serializer: Serializer = serializer_class(instance=pet_list, many=True)

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


class PetListAPIView(generics.GenericAPIView):
    """
    API View for retrieving all pets from a specific shelter. This view handles the
    "GET" request to retrieve all pets from a specific shelter.
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = PetReadOnlySerializer
    application_class = PetUseCase

    @GetPetByShelterSchema
    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Handles GET requests to retrieve all pets from a specific shelter.

        This method allows retrieving all pets from a specific shelter. It paginates
        the response with a total of 10 items and returns a list of pets along with the
        pagination data.
        """

        pet_list = self.application_class(
            pet_repository=PetRepository
        ).get_pet(shelter=kwargs["shelter_uuid"])

        # Paginate the response
        page = self.paginate_queryset(pet_list)
        paginated_response = self.get_paginated_response(page)
        pagination_data = paginated_response.data

        serializer = self.serializer_class(instance=pet_list, many=True)

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
