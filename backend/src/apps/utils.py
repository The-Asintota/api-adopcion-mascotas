from rest_framework import serializers


ERROR_MESSAGES = {
    "max_length": "{field_name} no puede tener más de {max_length} caracteres.",
    "min_length": "{field_name} debe tener al menos {min_length} caracteres.",
    "invalid": "{field_name} es inválido.",
    "invalid_choice": "{input} no es una elección válida.",
    "password_mismatch": "Las contraseñas no coinciden.",
    "password_common": "Esta contraseña es demasiado común.",
    "password_no_upper_lower": "La contraseña debe contener al menos una mayuscula o una minuscula.",
    "email_in_use": "Este correo electrónico ya está en uso.",
    "name_in_use": "Este nombre ya está en uso.",
    "phone_in_use": "Este número de teléfono ya está en uso.",
    "address_in_use": "Esta dirección ya está en uso.",
}


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
