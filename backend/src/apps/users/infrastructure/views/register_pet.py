from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from typing import Dict, Any
from apps.users.infrastructure.serializers import (
    RegisterPetSerializer,
    ListPetsSerializer,
)
from apps.users.infrastructure.db import PetRepository
from apps.users.use_case import PetRegister, PetList
from apps.users.endpoint_schemas.register_pet import GetEndPointSchema


class PetAPIView(generics.GenericAPIView):
    """
    API View for registering a new pet. This view handles the "POST" request to
    create a new pet in the system.
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = ListPetsSerializer

    def get_serializer_class(self):
        """
        Determina qué clase de serializador utilizar según el método de la solicitud.
        """
        if self.request.method == "POST":
            return RegisterPetSerializer
        else:
            return self.serializer_class

    def _handle_valid_request(
        self, data: Dict[str, Any], application_class: PetRegister
    ) -> Response:
        application_class(pet_repository=PetRepository).pet_registration(
            data=data
        )

        return Response(status=status.HTTP_201_CREATED)

    def _handle_invalid_request(self, serializer: Serializer) -> Response:

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

        application_class = PetRegister

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return self._handle_valid_request(
                data=serializer.validated_data,
                application_class=application_class,
            )

        return self._handle_invalid_request(serializer=serializer)

    def get(self, request: Request) -> Response:
        """
        Handle GET requests to retrieve all pets from the database.
        Returns a paginated response with the pet information.
        """

        application_class = PetList

        pet_list = application_class(pet_repository=PetRepository).pets_list()
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
