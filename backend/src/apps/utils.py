from rest_framework import serializers


class ErrorMessages(serializers.Serializer):
    """
    A serializer class that provides custom error messages for fields.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customized error messages
        msg = {
            "required": "Este campo es requerido.",
            "blank": "Este campo no puede estar en blanco.",
            "null": "Este campo no puede ser nulo.",
        }
        fields = list(self.fields.keys())
        for field_name in fields:
            self.fields[field_name].error_messages.update(msg)
