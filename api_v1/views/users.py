from rest_framework import viewsets, permissions
from api_v1.serializers.usuario_serializer import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework import status
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
            # Extraemos los datos de la peticion
            data = request.data

            # Creamos el producto
            #Hasheamos la contraseña, igual al metodo de la clase User
            password = data.get('password')
            hashPassword = make_password(password)
            user = User.objects.create(
                username=data.get('username'),
                password=hashPassword,
                first_name=data.get('first_name', None),
                last_name=data.get('last_name'),
                email=data.get('email')
            )

            serializer = self.serializer_class(user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
