from django.urls import path
from django.contrib.auth.decorators import login_required

from usuario.views.cliente_view import (
    Cliente_View,
    Cliente_Create,
    Cliente_Detail,
    Cliente_Update,
    Cliente_Delete,
)

urlpatterns =[
    #CLIENTES
    path (route='cliente/', view=login_required(Cliente_View.as_view(),login_url='login'), name='cliente_view'),
    path(route='cliente/create',view=(Cliente_Create.as_view()), name='cliente_create'),
    path(route='cliente/detail/<int:pk>', view=(Cliente_Detail.as_view()),name='cliente_detail'),
    path(route='cliente/update/<int:pk>', view=(Cliente_Update.as_view()),name='cliente_update'),
    path(route='cliente/delete/<int:pk>', view=(Cliente_Delete.as_view()), name = 'cliente_delete'),
]