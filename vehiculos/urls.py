from django.urls import path
from django.contrib.auth.decorators import login_required
from vehiculos.views.brandView import (
  BrandView,
  BrandDelete,
  BrandCreate,
  BrandUpdate,
)

urlpatterns = [
  path(route='', view=BrandView.as_view(), name='brand_list'),
  path(route='create/', view=BrandCreate.as_view(), name='brand_create'),
  path(route='<int:id>/delete/', view=BrandDelete.as_view(), name='brand_delete'),
  path(route='<int:id>/update/', view=BrandUpdate.as_view(), name='brand_update'),
]