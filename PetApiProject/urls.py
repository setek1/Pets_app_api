"""
URL configuration for PetApiProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#Importaciones para visualizar la documentacion con swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#Importar rutas de las otras aplicaciones
from pets_Owner.api.router import router_pets_owner
from pets.api.router import router_pets

#Configuracion 
schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion proyectoPets",
      default_version='v1',
      description="Documentacion para un pequeño proyecto llamado Pets",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #Rutas para la visualizacion de la documentacion de swagger y redoc sobre la aplicacion 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #Rutas de la aplicacion 
    path('api/',include(router_pets_owner.urls)),
    path('api/',include(router_pets.urls)),
]
