from rest_framework import viewsets, permissions
from api_v1.serializers.usuario_serializer import UserSerializer
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(is_staff=False, is_superuser=False)
