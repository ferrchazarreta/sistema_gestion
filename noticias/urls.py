from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from noticias.views.newView import (
  NewsView,
  NewsDelete,
  NewsCreate,
  NewsUpdate,
)

from noticias.views.categoryView import (
  CategoryView,
  CategoryCreate,
  CategoryUpdate,
  CategoryDelete,
)

urlpatterns = [
  path(route='category/', view=CategoryView.as_view(), name='category_list'),
  path(route='category/create/', view=CategoryCreate.as_view(), name='category_create'),
  path(route='category/<int:id>/delete/', view=CategoryDelete.as_view(), name='category_delete'),
  path(route='category/<int:id>/update/', view=CategoryUpdate.as_view(), name='category_update'),

  path(route='', view=NewsView.as_view(), name='noticias_list'),
  path(route='create/', view=NewsCreate.as_view(), name='noticias_create'),
  path(route='<int:id>/delete/', view=NewsDelete.as_view(), name='noticias_delete'),
  path(route='<int:id>/update/', view=NewsUpdate.as_view(), name='noticias_update'),

] 