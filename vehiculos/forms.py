from django import forms

from vehiculos.models import (
  Car,
  Brand,
  Fuel,
  Country,
  Modelo,
)

class CarForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = [
      'brand',
      'model_car',
      'year_production',
      'door_quatity',
      'cilindrada', 
      'fuel_type',
      'country_production',
      'image',
      'price',      
    ]
      
    widgets = {
      'brand': forms.Select(attrs={'class': 'form-control'}),
      'model_car': forms.Select(attrs={'class': 'form-control'}),
      'year_production': forms.NumberInput(attrs={'class': 'form-control'}),
      'door_quatity': forms.NumberInput(attrs={'class': 'form-control'}),
      'cilindrada': forms.NumberInput(attrs={'class': 'form-control'}),
      'fuel_type': forms.Select(attrs={'class': 'form-control'}),
      'country_production': forms.Select(attrs={'class': 'form-control'}),
      'image': forms.FileInput(attrs={'class': 'form-control'}),
      'price': forms.NumberInput(attrs={'class': 'form-control'}),
    }


class BrandForm(forms.ModelForm):
  class Meta:
    model = Brand
    fields = [
      'name',
    ]
     
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control'})
    }
    
class FuelForm(forms.ModelForm):
  class Meta:
    model = Fuel
    fields = [
      'name',
    ]

    widgets = {
      'name':forms.TextInput(attrs={'class': 'form-control'}),
    }

class CountryForm(forms.ModelForm):
  class Meta:
    model = Country
    fields = [
      'name',
    ]

    widgets = {
      'name':forms.TextInput(attrs={'class': 'form-control'}),
    }

class ModelForm(forms.ModelForm):
  class Meta:
    model = Modelo
    fields = [
      'name',
    ]

    widgets = {
      'name':forms.TextInput(attrs={'class': 'form-control'}),
    }