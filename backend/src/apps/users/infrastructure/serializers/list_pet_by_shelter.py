from rest_framework import serializers


class ListPetByShelterSerializer(serializers.Serializer):

    pet_name = serializers.CharField(read_only=True)
    pet_type = serializers.ChoiceField(read_only=True)
    pet_sex = serializers.ChoiceField(read_only=True)
    shelter = serializers.UUIDField(read_only=True)
    race = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)
    observations = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    image = serializers.URLField(read_only=True)
