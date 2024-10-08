from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from vehiculos.views.brandView import (
  BrandView,
  BrandDelete,
  BrandCreate,
  BrandUpdate,
)

from vehiculos.views.fuelView import (
  FuelView,
  FuelCreate,
  FuelDelete,
  FuelUpdate,
)

from vehiculos.views.carView import (
  CarView,
  CarUpdate,
  CarDelete,
  CarCreate,
  CarDetail,
  
  #Filtros
  CarByBrand,
  CarByBodyWork,
  CarByCondition,
  CarByFuel,
  CarByGama,
  CarByTransmission,
) 
from vehiculos.views.countryView import (
  CountryView,
  CountryUpdate,
  CountryCreate,
  CountryDelete,
)
from vehiculos.views.modelView import (
  ModelView,
  ModelUpdate,
  ModelCreate,
  ModelDelete,
)
from vehiculos.views.transmissionView import (
  TransmissionView,
  TransmissionUpdate,
  TransmissionDelete,
  TransmissionCreate
)
from vehiculos.views.conditionView import (
  ConditionView,
  ConditionUpdate,
  ConditionDelete,
  ConditionCreate
)
from vehiculos.views.gamaView import (
  GamaView,
  GamaUpdate,
  GamaDelete,
  GamaCreate
)
from vehiculos.views.bodyWorkView import(
  BodyWorkView,
  BodyWorkUpdate,
  BodyWorkCreate,
  BodyWorkDelete
)

from vehiculos.views.vehiculoReviewView import (
  VehiculoReviewView,
  VehiculoReviewCreate,
  VehiculoReviewDelete,
  VehiculoReviewDetail,
  VehiculoReviewUpdate,
)

urlpatterns = [
#COMBUSTIBLES
  path(route='fuel/', view=FuelView.as_view(), name='fuel_list'),
  path(route='fuel/create/', view=FuelCreate.as_view(), name='fuel_create'),
  path(route='fuel/<int:id>/delete/', view=FuelDelete.as_view(), name='fuel_delete'),
  path(route='fuel/<int:id>/update/', view=FuelUpdate.as_view(), name='fuel_update'),
#MARCAS
  path(route='brand/', view=BrandView.as_view(), name='brand_list'),
  path(route='brand/create/', view=BrandCreate.as_view(), name='brand_create'),
  path(route='brand/<int:id>/delete/', view=BrandDelete.as_view(), name='brand_delete'),
  path(route='brand/<int:id>/update/', view=BrandUpdate.as_view(), name='brand_update'),
#VEHICULOS
  path(route='', view=CarView.as_view(), name='vehiculo_list'),
  path(route='create/', view=CarCreate.as_view(), name='vehiculo_create'),
  path(route='<int:id>/delete/', view=CarDelete.as_view(), name='vehiculo_delete'),
  path(route='<int:id>/update/', view=CarUpdate.as_view(), name='vehiculo_update'),
  path(route='<int:id>/detail/', view=CarDetail.as_view(), name='vehiculo_detail'),
#PAISES
  path(route='country/', view=CountryView.as_view(), name='country_list'),
  path(route='country/create/', view=CountryCreate.as_view(), name='country_create'),
  path(route='country/<int:id>/delete/', view=CountryDelete.as_view(), name='country_delete'),
  path(route='country/<int:id>/update/', view=CountryUpdate.as_view(), name='country_update'),
#MODELOS
  path(route='model/', view=ModelView.as_view(), name='model_list'),
  path(route='model/create/', view=ModelCreate.as_view(), name='model_create'),
  path(route='model/<int:id>/delete/', view=ModelDelete.as_view(), name='model_delete'),
  path(route='model/<int:id>/update/', view=ModelUpdate.as_view(), name='model_update'),
  
#TESTIMONIOS
  path(route='testimonios/', view=VehiculoReviewView.as_view(), name='review_list'),
  path(route='testimonios/create/', view=VehiculoReviewCreate.as_view(), name='review_create'),
  path(route='testimonios/<int:id>/delete/', view=VehiculoReviewDelete.as_view(), name='review_delete'),
  path(route='testimonios/<int:id>/update/', view=VehiculoReviewUpdate.as_view(), name='review_update'),
  path(route='testimonios/<int:id>/detail/', view=VehiculoReviewDetail.as_view(), name='review_detail'),

#TRANSMISIONES
  path(route='transmission/', view=TransmissionView.as_view(), name='transmission_list'),
  path(route='transmission/create/', view=TransmissionCreate.as_view(), name='transmission_create'),
  path(route='transmission/<int:id>/delete/', view=TransmissionDelete.as_view(), name='transmission_delete'),
  path(route='transmission/<int:id>/update/', view=TransmissionUpdate.as_view(), name='transmission_update'),
  
#CODICIONES AUTOS
  path(route='condition/', view=ConditionView.as_view(), name='condition_list'),
  path(route='condition/create/', view=ConditionCreate.as_view(), name='condition_create'),
  path(route='condition/<int:id>/delete/', view=ConditionDelete.as_view(), name='condition_delete'),
  path(route='condition/<int:id>/update/', view=ConditionUpdate.as_view(), name='condition_update'),
  
#GAMAS
  path(route='gama/', view=GamaView.as_view(), name='gama_list'),
  path(route='gama/create/', view=GamaCreate.as_view(), name='gama_create'),
  path(route='gama/<int:id>/delete/', view=GamaDelete.as_view(), name='gama_delete'),
  path(route='gama/<int:id>/update/', view=GamaUpdate.as_view(), name='gama_update'),
  
#CARROCERIAS
  path(route='bodywork/', view=BodyWorkView.as_view(), name='bodyWork_list'),
  path(route='bodywork/create/', view=BodyWorkCreate.as_view(), name='bodyWork_create'),
  path(route='bodywork/<int:id>/delete/', view=BodyWorkDelete.as_view(), name='bodyWork_delete'),
  path(route='bodywork/<int:id>/update/', view=BodyWorkUpdate.as_view(), name='bodyWork_update'),
  
  path(route='filter/brand/<int:id>/', view=CarByBrand.as_view(), name='filter_brand'),
  path(route='filter/bodywork/<int:id>/', view=CarByBodyWork.as_view(), name='filter_bodywork'),
  path(route='filter/condition/<int:id>/', view=CarByCondition.as_view(), name='filter_condition'),
  path(route='filter/fuel/<int:id>/', view=CarByFuel.as_view(), name='filter_fuel'),
  path(route='filter/gama/<int:id>/', view=CarByGama.as_view(), name='filter_gama'),
  path(route='filter/transmission/<int:id>/', view=CarByTransmission.as_view(), name='filter_transmission'),
 
  
] 