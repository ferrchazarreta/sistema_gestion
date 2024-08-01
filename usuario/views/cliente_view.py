from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from usuario.repositories.cliente_repository import Cliente_Repository

repository = Cliente_Repository()

class Cliente_View(View):
    def get(self, request):
        clientes = repository.get_all()
        return render(request, 'cliente/list.html', 
                      {'clientes': clientes}
                      )
    
class Cliente_Create(View):
    def get(self, request):
        if request.user.is_staff:
            users = User.objects.all()
            return render(request, 'cliente/create.html',{'users': users})
        else:
            return redirect('cliente_list')
    
    def post(self,request):
        if request.user.is_staff:
            user_id = request.POST.get('user')
            user = get_object_or_404(User, id=user_id)
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            nuevo_cliente = repository.create(
                user=user, 
                address=address, 
                phone=phone
            )
            return redirect('cliente_list')
        else:
            return redirect('cliente_list')

class Cliente_Delete(View):
    def get(self, request, id):
        if request.user.is_staff:
            cliente = repository.get_by_id(id=id)
            repository.delete(cliente)
            return redirect('cliente_list')
        else:
            return redirect('cliente_list')

class Cliente_Update(View):
    def get(self, request, id):
        if request.user.is_staff:
            cliente = repository.get_by_id(id=id)
            return render(request, 'cliente/update.html',
                          {'cliente': cliente}
                          )
        else:
            return redirect('cliente_list')
    
    def post(self,request,id):
        if request.user.is_staff:
            cliente = repository.get_by_id(id)
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            repository.update(
                cliente=cliente,
                address=address,
                phone=phone
            )
            return redirect('cliente_list')
        else:
            return redirect('cliente_list')
            