from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from vehiculos.forms import TransmissionForm
from vehiculos.repositories.transmissionRepository import TransmissionRepository

class TransmissionView(View):
  def get(self, request):
    repo = TransmissionRepository()
    transmision = repo.get_all()
    if request.user.is_staff:
      return render(
        request,
        'transmission/list.html',
        {
          'transmissions': transmision
        }
      )
    else:
      return redirect('index')

class TransmissionCreate(View):
    def get(self, request):
        if request.user.is_staff:
            form = TransmissionForm()
            return render(
                request,
                'transmission/create.html',
                {
                  'form':form,
                }
            )
        else:
            return redirect('transmission_list')
    
    def post(self, request):
        repo = TransmissionRepository()
        nombre = request.POST.get('name')
        newTransmission = repo.create(name=nombre)
        return redirect('transmission_list')

class TransmissionDelete(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = TransmissionRepository()
      transmision = repo.get_by_id(id=id)
      repo.delete(transmission=transmision)
    return redirect('transmission_list')

class TransmissionUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = TransmissionRepository()
      transmission = repo.get_by_id(id=id)

      return render(
          request,
          'transmission/update.html',
          {
            'transmission': transmission,
          }
      )
    else:
      return redirect('transmission_list')
    
  def post(self, request, id):
    if request.user.is_staff:
      repo = TransmissionRepository()

      transmission = repo.get_by_id(id)
      name = request.POST.get('name')
      repo.update(transmission=transmission,
                  nombre=name)

      return redirect('transmission_list')
    else:
      return redirect('transmission_list')