from django.urls import path
from .views import (
    RegisterShelterAPIView,
    AuthenticationAPIView,
    RegisterAdminAPIView,
    RegisterPetAPIView,
)

urlpatterns = [
    path(
        route="shelter/",
        view=RegisterShelterAPIView.as_view(),
        name="register_shelter",
    ),
    path(
        route="auth/",
        view=AuthenticationAPIView.as_view(),
        name="authentication",
    ),
    path(
        route="admin/",
        view=RegisterAdminAPIView.as_view(),
        name="register_admin",
    ),
    path(
        route="pet/",
        view=RegisterPetAPIView.as_view(),
        name="register_pet",
    )
]
