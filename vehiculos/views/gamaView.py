from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from vehiculos.forms import GamaForm
from vehiculos.repositories.gamaRepository import GamaRepository

class GamaView(View):
  def get(self, request):
    repo = GamaRepository()
    gama = repo.get_all()
    if request.user.is_staff:
      return render(
        request,
        'gama/list.html',
        {
          'gamas': gama
        }
      )
    else:
      return redirect('index')

class GamaCreate(View):
    def get(self, request):
        if request.user.is_staff:
            form = GamaForm()
            return render(
                request,
                'gama/create.html',
                {
                  'form':form,
                }
            )
        else:
            return redirect('gama_list')
    
    def post(self, request):
        repo = GamaRepository()
        nombre = request.POST.get('name')
        newGama = repo.create(name=nombre)
        return redirect('gama_list')

class GamaDelete(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = GamaRepository()
      gama = repo.get_by_id(id=id)
      repo.delete(gama=gama)
    return redirect('gama_list')

class GamaUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = GamaRepository()
      gama = repo.get_by_id(id=id)

      return render(
          request,
          'gama/update.html',
          {
            'gama': gama,
          }
      )
    else:
      return redirect('gama_list')
    
  def post(self, request, id):
    if request.user.is_staff:
      repo = GamaRepository()

      gama = repo.get_by_id(id)
      name = request.POST.get('name')
      repo.update(gama=gama,
                  nombre=name)

      return redirect('gama_list')
    else:
      return redirect('gama_list')