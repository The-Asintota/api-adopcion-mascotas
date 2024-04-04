from django.urls import path
from .views import RegisterShelterAPIView

urlpatterns = [
    path(
        route="shelter/",
        view=RegisterShelterAPIView.as_view(),
        name="register_shelter",
    ),
]
