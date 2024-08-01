from django.contrib import admin
from usuario.models import Cliente

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('address','phone')
    list_filter = ('address','phone')
    list_display = (
        'user',
        'address',
        'phone',
    )