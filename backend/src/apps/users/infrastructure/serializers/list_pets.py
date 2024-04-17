from rest_framework import serializers


class ListPetsSerializer(serializers.Serializer):
    """
    Defines the data that the pet list will return
    """

    pet_uuid = serializers.UUIDField()
    pet_type = serializers.PrimaryKeyRelatedField(read_only=True)
    pet_sex = serializers.PrimaryKeyRelatedField(read_only=True)
    shelter = serializers.PrimaryKeyRelatedField(read_only=True)
    pet_name = serializers.CharField(read_only=True)
    pet_race = serializers.CharField(read_only=True)
    pet_age = serializers.IntegerField(read_only=True)
    pet_observations = serializers.CharField(read_only=True)
    pet_description = serializers.CharField(read_only=True)
    pet_image = serializers.URLField(read_only=True)

    def to_representation(self, instance):
        # Convertir el modelo en un diccionario para la representación
        return {
            "pet_uuid": str(instance.pet_uuid),
            "pet_type": instance.pet_type.id,
            "pet_sex": instance.pet_sex.id,
            "shelter": str(instance.shelter.shelter_uuid),
            "pet_name": instance.pet_name,
            "race": instance.pet_race,
            "age": instance.pet_age,
            "observations": instance.pet_observations,
            "description": instance.pet_description,
            "image": instance.pet_image,
        }
