from rest_framework.viewsets import ModelViewSet
from pets_Owner.models import Owner
from pets_Owner.api.serializers import OwnerSerializer


class OwnerApiViewSet(ModelViewSet):
    serializer_class=OwnerSerializer
    queryset=Owner.objects.all()