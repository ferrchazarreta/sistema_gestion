from rest_framework import serializers
from django.contrib.auth.models import User
from usuario.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

    class Meta:
        model = Cliente
        fields = ['id', 'user', 'address', 'phone']
