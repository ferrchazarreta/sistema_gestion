from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Cliente


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Email Requerido')
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-class'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control custom-class'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control custom-class', 'required':'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control custom-class','required':'required'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise ValidationError("El email ya se encuetra registrado")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_staff = False
        user.is_superuser = False
        user.is_cliente = False
        if commit:
            user.save()
        return user
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['address','phone']