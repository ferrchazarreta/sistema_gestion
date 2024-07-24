from django import forms

from vehiculos.models import (
  Car,
  Brand,
  Fuel,
  Country,
  Modelo,
)

# class CarForm(forms.ModelForm):
#   class Meta:
#     model = Car
#     fields = [
#       'brand',
#       'model',
#       'year_production',
#       'door_quatity',
#       'cilindrada', 
#       'fuel_type',
#       'country_production',
#       'image',
#       'price',      
#     ]
      
#     widgets = {
#       'brand': forms.Select(attrs={'class': 'form-control'}),
#       'modelo': forms.Select(attrs={'class': 'form-control'}),
#       'year_production': forms.NumberInput(attrs={'class': 'form-control'}),
#       'door_quatity': forms.NumberInput(attrs={'class': 'form-control'}),
#       'cilindrada': forms.NumberInput(attrs={'class': 'form-control'}),
#       'fuel_type': forms.Select(attrs={'class': 'form-control'}),
#       'country_production': forms.Select(attrs={'class': 'form-control'}),
#       'image': forms.FileInput(attrs={'class': 'form-control'}),
#       'price': forms.NumberInput(attrs={'class': 'form-control'}),
#     }

class BrandForm(forms.ModelForm):
  class Meta:
    model = Brand
    fields = [
      'name',
    ]


