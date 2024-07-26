from django.urls import path
from django.contrib.auth.decorators import login_required
from vehiculos.views.brandView import (
  BrandView,
  BrandDelete,
  BrandCreate,
  BrandUpdate,
)

from vehiculos.views.carView import (
  CarView,
  CarUpdate,
  CarDelete,
  CarCreate,
)

urlpatterns = [
  path(route='brand', view=BrandView.as_view(), name='brand_list'),
  path(route='brand/create/', view=BrandCreate.as_view(), name='brand_create'),
  path(route='brand/<int:id>/delete/', view=BrandDelete.as_view(), name='brand_delete'),
  path(route='brand/<int:id>/update/', view=BrandUpdate.as_view(), name='brand_update'),

  path(route='', view=CarView.as_view(), name='vehiculo_list'),
  path(route='create/', view=CarCreate.as_view(), name='vehiculo_create'),
  path(route='<int:id>/delete/', view=CarDelete.as_view(), name='vehiculo_delete'),
  path(route='<int:id>/update/', view=CarUpdate.as_view(), name='vehiculo_update'),
]