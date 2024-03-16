from rest_framework.routers import DefaultRouter
from pets.api.views import OwnerApiViewSet

#Registrar rutas especificas de esta app
router_pets=DefaultRouter()

router_pets.register(
    prefix='Owner', basename='Owner', viewset=OwnerApiViewSet
)