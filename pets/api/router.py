from rest_framework.routers import DefaultRouter
from pets.api.views import PetsApiViewSet

#Registrar rutas especificas de esta app
router_pets=DefaultRouter()

router_pets.register(
    prefix='Mascota',basename='Mascota', viewset=PetsApiViewSet
)