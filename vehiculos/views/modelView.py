from django.views import View
from django.shortcuts import render, redirect

from vehiculos.forms import ModelForm
from vehiculos.repositories.modelsRepository import ModelsRepository


class ModelView(View):
  def get(self, request):
    if request.user.is_staff:
      repo = ModelsRepository()
      models = repo.get_all()

      return render(
        request,
        'model/list.html',
        {
          'models': models
        }
        )
    else:
      return redirect('index')

class ModelCreate(View):
  def get(self, request):
    if request.user.is_staff:
      form = ModelForm()

      return render(
        request,
        'model/create.html',
        {
          'form': form,
        }
      )
    else:
      return redirect('model_list')

  def post(self, request):
    if request.user.is_staff:
      modelRepo = ModelsRepository()
      data = request.POST
      model = data.get('name')

      modelRepo.create(
        name = model
      )

      return redirect('model_list')
    else:
      return redirect('model_list')


class ModelDelete(View):
    def get(self, request, id):
        if request.user.is_staff:
            repo = ModelsRepository()
            model = repo.get_by_id(id=id)
            repo.delete(model=model)
        return redirect('model_list')

class ModelUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      modelRepo = ModelsRepository()
      model = modelRepo.get_by_id(id)

      return render(
        request,
        'model/update.html',
        {
          'model': model,

        }
      )
    else:
      return redirect('model_list')

  def post(self, request, id):
    if request.user.is_staff:
      modelRepo = ModelsRepository()
      model = modelRepo.get_by_id(id)
      modelo = request.POST.get('name')

      modelRepo.update(
        model=model,
        nombre=modelo,
      )

      return redirect('model_list')