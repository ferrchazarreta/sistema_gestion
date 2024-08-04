from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from usuario.repositories.usuario_repository import Usuario_Repository

repository = Usuario_Repository()

class Usuario_View(View):
    def get(self, request):
        usuarios = repository.get_all()
        return render(request, 'usuario/list.html', 
                      {'usuarios': usuarios}
                      )
    
class Usuario_Create(View):
    def get(self, request):
        if request.user.is_staff:
            users = User.objects.all()
            return render(request, 'usuario/create.html')
        else:
            return redirect('usuario_list')
    
    def post(self,request):
        if request.user.is_staff:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            nuevo_usuario = repository.create(
                username=username, 
                email=email, 
                password=password, 
                first_name=first_name, 
                last_name=last_name)
            return redirect('usuario_list')
        else:
            return redirect('usuario_list')

class Usuario_Detail(View):
    def get(self, request, id):
        if request.user.is_staff:
            usuario = repository.get_by_id(id=id)
            return render(request, 'usuario/detail.html', {'usuario': usuario})
        else:
            return redirect('usuario_list')
        
class Usuario_Delete(View):
    def get(self, request, id):
        if request.user.is_staff:
            usuario = repository.get_by_id(id=id)
            repository.delete(usuario)
            return redirect('usuario_list')
        else:
            return redirect('usuario_list')

class Usuario_Update(View):
    def get(self, request, id):
        if request.user.is_staff:
            usuario = repository.get_by_id(id=id)
            return render(request, 'usuario/update.html',
                          {'usuario': usuario}
                          )
        else:
            return redirect('usuario_list')
    
    def post(self,request,id):
        if request.user.is_staff:
            usuario = repository.get_by_id(id=id)
            username = request.POST.get('username')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            repository.update(
                usuario=usuario,
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            return redirect('usuario_detail', id=id)
        else:
            return redirect('usuario_list')
            