from django.urls import path
from apps.users.infrastructure.views import (
    ShelterAPIView,
    AuthenticationAPIView,
    AdminAPIView,
    PetAPIView,
    PetListAPIView,
)

urlpatterns = [
    path(
        route="shelter/",
        view=ShelterAPIView.as_view(),
        name="shelter",
    ),
    path(
        route="auth/",
        view=AuthenticationAPIView.as_view(),
        name="authentication",
    ),
    path(
        route="admin/",
        view=AdminAPIView.as_view(),
        name="admin",
    ),
    path(
        route="pet/",
        view=PetAPIView.as_view(),
        name="pet",
    ),
    path(
        route="pet/<str:shelter_uuid>/",
        view=PetListAPIView.as_view(),
        name="list_pets_shelter",
    ),
]
