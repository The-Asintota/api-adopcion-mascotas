from rest_framework import serializers
from apps.emails.models import EmailsSent


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
