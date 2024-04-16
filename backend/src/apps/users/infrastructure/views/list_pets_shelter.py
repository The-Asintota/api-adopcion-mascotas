from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from apps.users.infrastructure.serializers import PetSerializer
from apps.users.infrastructure.db import PetRepository
from apps.users.use_case import FindPetsByShelter
from apps.users.endpoint_schemas.list_pet_shelter import GetEndPointSchema


class PetListByShelterApiView(generics.GenericAPIView):
    """
    API View for retrieving pets from a specific shelter. This view handles the "GET"
    request to retrieve pets from a specific shelter in the system.
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = PetSerializer
    application_class = FindPetsByShelter

    @GetEndPointSchema
    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Handle GET requests for retrieving pets from a specific shelter.

        This method allows the retrieval of pets from a specific shelter. It waits
        for a GET request with a shelter's UUID, retrieves the pets from the database,
        and returns a paginated response with the pets' information.
        """

        pet_list = self.application_class(
            pet_repository=PetRepository
        ).get_pet(shelter=kwargs["shelter_uuid"])
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
