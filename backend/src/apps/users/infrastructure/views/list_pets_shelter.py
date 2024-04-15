from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from apps.users.infrastructure.serializers import ListPetByShelterSerializer
from apps.users.use_case import FindPetsByShelter
from apps.users.infrastructure.db import PetRepository


class PetListByShelterApiView(generics.GenericAPIView):

    authentication_classes = ()
    permission_classes = ()
    serializer_class = ListPetByShelterSerializer
    application_class = FindPetsByShelter

    def get(self, request: Request, *args, **kwargs) -> Response:
        pet_list = self.application_class(
            pet_repository=PetRepository
        ).get_pet(shelter_uuid=kwargs["shelter_uuid"])
        serializer = self.serializer_class(instance=pet_list, many=True)
        if serializer.is_valid():
            return Response(
                data=serializer.validated_data,
                status=status.HTTP_200_OK,
                content_type="application/json",
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
            content_type="application/json",
        )
