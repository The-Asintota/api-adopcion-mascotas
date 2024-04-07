from django.urls import path
from .views import RegisterShelterAPIView, AuthenticationAPIView

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
]
