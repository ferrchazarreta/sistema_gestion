from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from usuario.repositories.usuario_repository import Usuario_Repository
from usuario.forms import UserRegisterForm, UserUpdateForm

repository = Usuario_Repository()

class Usuario_View(View):
    def get(self, request):
        if request.user.is_staff:
            usuarios = repository.get_all()
            return render(request, 'usuario/list.html', 
                        {'usuarios': usuarios}
                        )
        else:
            return redirect('index')
    
class Usuario_Create(View):
    form_class = UserRegisterForm
    def get(self, request):
        if request.user.is_staff:
            form = self.form_class()
            return render(
                request, 
                'usuario/create.html',
                {'form': form}
                )
        else:
            return redirect('index')
    
    def post(self,request):
        if request.user.is_staff:
            form = self.form_class(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('usuario_list')
            else:
                return render(
                    request, 
                    'usuario/create.html', 
                    {'form': form}
                    )
        else:
            return redirect('index')

class Usuario_Detail(View):
    def get(self, request, id):
        if request.user.is_staff:
            usuario = repository.get_by_id(id=id)
            return render(request, 'usuario/detail.html', {'usuario': usuario})
        else:
            return redirect('index')
        
class Usuario_Delete(View):
    def get(self, request, id):
        if request.user.is_staff:
            usuario = repository.get_by_id(id=id)
            repository.delete(usuario)
            return redirect('usuario_list')
        else:
            return redirect('index')

class Usuario_Update(View):
    def get(self, request, id):
        if request.user.is_staff:
            usuario = repository.get_by_id(id=id)
            user_form = UserUpdateForm(instance=usuario)
            return render(
                request, 
                'usuario/update.html', 
                {'user_form': user_form}
            )
        else:
            return redirect('index')
    
    def post(self,request,id):
        if request.user.is_staff:
            usuario = repository.get_by_id(id=id)
            user_form = UserUpdateForm(request.POST, instance=usuario)
            if user_form.is_valid():
                user_form.save()
                return redirect('usuario_detail', id=id)
            else:
                return render(
                request, 
                'usuario/update.html', 
                {'user_form': user_form},
                print('falla')
            )
        else:
            return redirect('index')
        