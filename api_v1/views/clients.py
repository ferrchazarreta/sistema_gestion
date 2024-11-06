from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from api_v1.serializers.cliente_serializer import ClienteSerializer
from usuario.models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        user = serializer.validated_data.get('user')
        if Cliente.objects.filter(user=user).exists():
            raise ValidationError("Este usuario ya tiene un perfil de cliente.")
        serializer.save()
