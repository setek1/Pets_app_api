from rest_framework.viewsets import ModelViewSet
from pets.models import Pets
from pets.api.serializers import PetsSerializer

class PetsApiViewSet(ModelViewSet):
    serializer_class=PetsSerializer
    queryset=Pets.objects.all()
