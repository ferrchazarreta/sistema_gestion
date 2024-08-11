from django import forms

from noticias.models import (
  News,
  Category
)

class NewsForm(forms.ModelForm):
  class Meta:
    model = News
    fields = [
      'title',
      'short_description',
      'long_description',
      'category',
      'image',
    ]
      
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Título de la noticia',}),
      'short_description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Descripción'}),
      'long_description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Descrición'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
      'image': forms.FileInput(attrs={'class': 'form-control','required':'required'}),
    }


class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = [
      'name',
    ]
     
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control'})
    }
    