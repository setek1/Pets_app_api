from rest_framework.serializers import ModelSerializer
from pets.models import Pets


class PetsSerializer(ModelSerializer):
    class Meta:
        model=Pets
        fields='__all__'