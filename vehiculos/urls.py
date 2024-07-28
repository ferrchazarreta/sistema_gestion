from django.urls import path
from django.contrib.auth.decorators import login_required
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

urlpatterns = [
  path(route='', view=BrandView.as_view(), name='brand_list'),
  path(route='create/', view=BrandCreate.as_view(), name='brand_create'),
  path(route='<int:id>/delete/', view=BrandDelete.as_view(), name='brand_delete'),
  path(route='<int:id>/update/', view=BrandUpdate.as_view(), name='brand_update'),

  path(route='fuel', view=FuelView.as_view(), name='fuel_list'),
  path(route='fuel/create/', view=FuelCreate.as_view(), name='fuel_create'),
  path(route='fuel/<int:id>/delete/', view=FuelDelete.as_view(), name='fuel_delete'),
  path(route='fuel/<int:id>/update/', view=FuelUpdate.as_view(), name='fuel_update'),
]