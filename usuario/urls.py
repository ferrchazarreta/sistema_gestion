from django.urls import path
from django.contrib.auth.decorators import login_required

from usuario.views.usuario_view import (
    Usuario_View,
    Usuario_Create,
    Usuario_Detail,
    Usuario_Update,
    Usuario_Delete,
)
from usuario.views.cliente_view import (
    Cliente_View,
    Cliente_Create,
    Cliente_Update,
    Cliente_Delete,
)

urlpatterns =[
    #USUARIOS
    path (route='', view=login_required(Usuario_View.as_view(),login_url='login'), name='usuario_list'),
    path(route='create/',view=(Usuario_Create.as_view()), name='usuario_create'),
    path(route='<int:id>/detail',view=(Usuario_Detail.as_view()), name='usuario_detail'),
    path(route='<int:id>/update', view=(Usuario_Update.as_view()),name='usuario_update'),
    path(route='<int:id>/delete', view=(Usuario_Delete.as_view()), name='usuario_delete'),
    
    #CLIENTES
    path (route='cliente/', view=login_required(Cliente_View.as_view(),login_url='login'), name='cliente_list'),
    path(route='cliente/create',view=(Cliente_Create.as_view()), name='cliente_create'),
    path(route='cliente/<int:id>/update', view=(Cliente_Update.as_view()),name='cliente_update'),
    path(route='cliente/<int:id>/delete', view=(Cliente_Delete.as_view()), name = 'cliente_delete'),
]