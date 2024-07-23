from django.contrib import admin
from vehiculos.models import Car,Model,Brand,Fuel,Country
from django.utils.html import format_html

# Register your models here.

@admin.register(Car)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('brand', 'model_car', 'year_production','country_production')
    list_filter = ('brand', 'cilindrada','fuel_type','door_quatity')
    #list_editable = ('price',)
    #exclude = ('price',)
    empty_value_display = "No hay datos para este campo"
    # readonly_fields =  ("name",)
    #list_display_links = ("price","name",)

    list_display = (
        'brand',
        'model_car',
        'year_production',
        'door_quatity',
        'cilindrada',
        'fuel_type',
        'country_production',
        'price',
    )

    fieldsets = [
        (
            "Info del Producto",
            {
                "fields" : ["brand", "price"],
            }
        ),
        (
            "Info Extra",
            {
                "classes":["collapse"],
                "fields" : ["stock", "description"]
            }
        )
    ]