from django import forms

from vehiculos.models import (
  Car,
  Brand,
  Fuel,
  Country,
  Modelo,
  Transmission,
  Gama,
  BodyWork,
  Condition,
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
      'transmission',
      'gama',
      'condition',
      'bodyWork',
      'km',
    ]
      
    widgets = {
      'brand': forms.Select(attrs={'class': 'form-control','required':'required'}),
      'model_car': forms.Select(attrs={'class': 'form-control','required':'required'}),
      'year_production': forms.NumberInput(attrs={'class': 'form-control','required':'required','min':'1886'}),
      'door_quatity': forms.NumberInput(attrs={'class': 'form-control','required':'required','min':'2'}),
      'cilindrada': forms.NumberInput(attrs={'class': 'form-control','required':'required','min':'1000'}),
      'fuel_type': forms.Select(attrs={'class': 'form-control','required':'required'}),
      'country_production': forms.Select(attrs={'class': 'form-control','required':'required'}),
      'image': forms.FileInput(attrs={'class': 'form-control','required':'required'}),
      'price': forms.NumberInput(attrs={'class': 'form-control','required':'required','min':'1000'}),
      'transmission': forms.Select(attrs={'class': 'form-control','required':'required'}),
      'gama': forms.Select(attrs={'class': 'form-control','required':'required'}),
      'condition':forms.Select(attrs={'class': 'form-control','required':'required'}),
      'bodyWork': forms.Select(attrs={'class': 'form-control','required':'required'}),
      'km': forms.NumberInput(attrs={'class': 'form-control','min':'1','required':'required'}),
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

class TransmissionForm(forms.ModelForm):
  class Meta:
    model = Transmission
    fields = [
      'name',
    ]

    widgets = {
      'name':forms.TextInput(attrs={'class': 'form-control'}),
    }

class ConditionForm(forms.ModelForm):
  class Meta:
    model = Condition
    fields = [
      'name',
    ]

    widgets = {
      'name':forms.TextInput(attrs={'class': 'form-control'}),
    }

class BodyWorkForm(forms.ModelForm):
  class Meta:
    model = BodyWork
    fields = [
      'name',
    ]

    widgets = {
      'name':forms.TextInput(attrs={'class': 'form-control'}),
    }

class GamaForm(forms.ModelForm):
  class Meta:
    model = Gama
    fields = [
      'name',
    ]

    widgets = {
      'name':forms.TextInput(attrs={'class': 'form-control'}),
    }