from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from vehiculos.forms import BodyWorkForm
from vehiculos.repositories.bodyWorkRepository import BodyWorkRepository

class BodyWorkView(View):
  def get(self, request):
    repo = BodyWorkRepository()
    bodyWork = repo.get_all()
    if request.user.is_staff:
      return render(
        request,
        'bodyWork/list.html',
        {
          'bodyWorks': bodyWork
        }
      )
    else:
      return redirect('index')

class BodyWorkCreate(View):
    def get(self, request):
        if request.user.is_staff:
            form = BodyWorkForm()
            return render(
                request,
                'bodyWork/create.html',
                {
                  'form':form,
                }
            )
        else:
            return redirect('bodyWork_list')
    
    def post(self, request):
        repo = BodyWorkRepository()
        nombre = request.POST.get('name')
        newBodyWork = repo.create(name=nombre)
        return redirect('bodyWork_list')

class BodyWorkDelete(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = BodyWorkRepository()
      bodyWork = repo.get_by_id(id=id)
      repo.delete(bodyWork=bodyWork)
    return redirect('bodyWork_list')

class BodyWorkUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = BodyWorkRepository()
      bodyWork = repo.get_by_id(id=id)

      return render(
          request,
          'bodyWork/update.html',
          {
            'bodyWork': bodyWork,
          }
      )
    else:
      return redirect('bodyWork_list')
    
  def post(self, request, id):
    if request.user.is_staff:
      repo = BodyWorkRepository()

      bodyWork = repo.get_by_id(id)
      name = request.POST.get('name')
      repo.update(bodyWork=bodyWork,
                  nombre=name)

      return redirect('bodyWork_list')
    else:
      return redirect('bodyWork_list')