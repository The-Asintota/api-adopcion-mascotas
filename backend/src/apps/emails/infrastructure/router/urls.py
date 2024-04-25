from django.urls import path
from apps.emails.infrastructure.views import (
    AdoptionPetAPIView,
    EmailsSentListAPIView,
)

urlpatterns = [
    path(
        route="email/adoption/",
        view=AdoptionPetAPIView.as_view(),
        name="adoption_pet_email",
    ),
    path(
        route="email/",
        view=EmailsSentListAPIView.as_view(),
        name="emails_sent_list",
    ),
]
