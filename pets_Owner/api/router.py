from rest_framework.routers import DefaultRouter
from pets_Owner.api.views import OwnerApiViewSet

#Registrar rutas especificas de esta app
router_pets_owner=DefaultRouter()

router_pets_owner.register(
    prefix='Owner', basename='Owner', viewset=OwnerApiViewSet
)