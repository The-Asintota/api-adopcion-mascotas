from django.contrib import admin
from .models import EmailsSent


class EmailsSentAdminPanel(admin.ModelAdmin):
    """
    Admin panel configuration for the `EmailsSent` model.
    """

    list_display = (
        "uuid",
        "subject",
        "message",
        "addressee",
        "additional_info",
        "date_joined",
    )
    search_fields = ("addressee",)


admin.site.register(EmailsSent, EmailsSentAdminPanel)
