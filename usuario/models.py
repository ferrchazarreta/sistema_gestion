from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='is_cliente')
    address = models.CharField(max_length=255, blank=True, null=False)
    phone = models.IntegerField(blank=True, null=False)
    
    def __str__(self):
        return self.user.username
    
    def is_cliente(self):
        return hasattr(self, 'cliente_profile')

    User.add_to_class('is_cliente', property(is_cliente))