from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from vehiculos.forms import FuelForm
from vehiculos.repositories.fuelRepository import FuelRepository

class FuelView(View):
  def get(self, request):
    if request.user.is_staff:
      repo = FuelRepository()
      combustibles = repo.get_all()

      return render(
        request,
        'fuels/list.html',
        {
          'fuels': combustibles
        }
      )
    else:
      return redirect('index')

class FuelCreate(View):
    def get(self, request):
        if request.user.is_staff:
            form = FuelForm()
            return render(
                request,
                'fuels/create.html',
                {
                  'form':form,
                }
            )
        else:
            return redirect('fuel_list')
    
    def post(self, request):
        repo = FuelRepository()
        nombre = request.POST.get('name')
        newBrand = repo.create(name=nombre)
        return redirect('fuel_list')

class FuelDelete(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = FuelRepository()
      combustible = repo.get_by_id(id=id)
      repo.delete(fuel=combustible)
    return redirect('fuel_list')

class FuelUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = FuelRepository()
      combustible = repo.get_by_id(id=id)

      return render(
          request,
          'fuels/update.html',
          {
            'fuel': combustible,
          }
      )
    else:
      return redirect('fuel_list')
    
  def post(self, request, id):
    if request.user.is_staff:
      repo = FuelRepository()

      combustible = repo.get_by_id(id)
      name = request.POST.get('name')
      repo.update(fuel=combustible,
                  nombre=name)

      return redirect('fuel_list')
    else:
      return redirect('fuel_list')