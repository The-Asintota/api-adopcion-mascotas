from rest_framework import serializers
from apps.emails.models import EmailsSent
from apps.emails.endpoint_schemas.get_all_emails import (
    EmailsListSerializerSchema,
)


@EmailsListSerializerSchema
class EmailsListReadOnlySerializer(serializers.ModelSerializer):
    """
    Defines the serialization of an email object for read-only purposes.
    """

    class Meta:
        model = EmailsSent
        fields = [
            "uuid",
            "subject",
            "message",
            "addressee",
            "additional_info",
        ]
        read_only_fields = fields
