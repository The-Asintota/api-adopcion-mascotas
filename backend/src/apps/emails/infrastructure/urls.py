from django.urls import path
from .views import AdoptionPetAPIView

urlpatterns = [
    path(
        route="email/adoption/",
        view=AdoptionPetAPIView.as_view(),
        name="adoption_pet_email",
    ),
]
