from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from vehiculos.forms import ConditionForm
from vehiculos.repositories.conditionRepository import ConditionRepository

class ConditionView(View):
  def get(self, request):
    if request.user.is_staff:
      repo = ConditionRepository()
      condition = repo.get_all()
      return render(
          request,
          'condition/list.html',
          {
            'conditions': condition
          }
        )
    else:
      return redirect('index')

class ConditionCreate(View):
    def get(self, request):
        if request.user.is_staff:
            form = ConditionForm()
            return render(
                request,
                'condition/create.html',
                {
                  'form':form,
                }
            )
        else:
            return redirect('condition_list')
    
    def post(self, request):
        repo = ConditionRepository()
        nombre = request.POST.get('name')
        newCondition = repo.create(name=nombre)
        return redirect('condition_list')

class ConditionDelete(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = ConditionRepository()
      condition = repo.get_by_id(id=id)
      repo.delete(condition=condition)
    return redirect('condition_list')

class ConditionUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = ConditionRepository()
      condition = repo.get_by_id(id=id)

      return render(
          request,
          'condition/update.html',
          {
            'condition': condition,
          }
      )
    else:
      return redirect('condition_list')
    
  def post(self, request, id):
    if request.user.is_staff:
      repo = ConditionRepository()

      condition = repo.get_by_id(id)
      name = request.POST.get('name')
      repo.update(condition=condition,
                  nombre=name,
                  )

      return redirect('condition_list')
    else:
      return redirect('condition_list')