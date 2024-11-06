from rest_framework import routers
from .views.vehicles import (
    CountryViewSet, ModeloViewSet, BrandViewSet, FuelViewSet, TransmissionViewSet,
    GamaViewSet, ConditionViewSet, BodyWorkViewSet, CarViewSet, VehiculoReviewViewSet
)
from .views.clients import ClienteViewSet
from .views.users import UserViewSet
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'modelos', ModeloViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'fuels', FuelViewSet)
router.register(r'transmissions', TransmissionViewSet)
router.register(r'gamas', GamaViewSet)
router.register(r'conditions', ConditionViewSet)
router.register(r'bodyworks', BodyWorkViewSet)
router.register(r'cars', CarViewSet)
router.register(r'cars/(?P<vehiculo_id>[^/.]+)/reviews', VehiculoReviewViewSet) #acomodar esta ruta que no se muestra, ej: cars/4/reviews si se ve
router.register(r'usuarios', UserViewSet)
router.register(r'clientes', ClienteViewSet)

urlpatterns = router.urls + [
    path('login_api', obtain_auth_token, name='login_api'), #acomodar esta ruta porque no se muestra: api_v1/login_api
]
