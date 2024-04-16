from rest_framework import serializers


class PetSerializer(serializers.Serializer):
    """
    Defines the data required to list a pet from a shelter.
    """

    pet_name = serializers.CharField(read_only=True)
    pet_type = serializers.CharField(read_only=True)
    pet_sex = serializers.CharField(read_only=True)
    shelter = serializers.UUIDField(read_only=True)
    pet_race = serializers.CharField(read_only=True)
    pet_age = serializers.IntegerField(read_only=True)
    pet_observations = serializers.CharField(read_only=True)
    pet_description = serializers.CharField(read_only=True)
    pet_image = serializers.URLField(read_only=True)
