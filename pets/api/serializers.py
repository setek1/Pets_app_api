from rest_framework.serializers import ModelSerializer
from pets.models import Owner

class OwnerSerializer(ModelSerializer):
    class Meta:
        model=Owner
        fields='__all__'