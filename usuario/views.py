from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ClienteForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if user_form.is_valid() and cliente_form.is_valid():
            user = user_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.user = user
            cliente.save()
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        cliente_form = ClienteForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'cliente_form': cliente_form
    })