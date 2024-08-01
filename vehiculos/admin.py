from django.contrib import admin
from vehiculos.models import Car,Modelo,Brand,Fuel,Country
from django.utils.html import format_html

# Register your models here.

@admin.register(Car)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('brand', 'model_car', 'year_production','country_production')
    list_filter = ('brand', 'cilindrada','fuel_type','door_quatity')
    list_editable = ('price','image')
    #exclude = ('price',)
    empty_value_display = "No hay datos para este campo"

    list_display = (
        'brand',
        'model_car',
        'year_production',
        'door_quatity',
        'cilindrada',
        'fuel_type',
        'country_production',
        'image',
        'price',
    )

    fieldsets = [
    ]

@admin.register(Modelo)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = (
        'name',
    )
    fieldsets = []

@admin.register(Brand)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = (
        'name',
    )
    fieldsets = []

@admin.register(Fuel)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = (
        'name',
    )
    fieldsets = []

@admin.register(Country)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = (
        'name',
    )
    fieldsets = []