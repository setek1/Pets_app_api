from rest_framework.viewsets import ModelViewSet
from pets.models import Owner
from pets.api.serializers import OwnerSerializer


class OwnerApiViewSet(ModelViewSet):
    serializer_class=OwnerSerializer
    queryset=Owner.objects.all()