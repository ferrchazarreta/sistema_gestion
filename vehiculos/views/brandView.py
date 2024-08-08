from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from vehiculos.forms import BrandForm
from vehiculos.repositories.brandsRepository import BrandsRepository

class BrandView(View):
  def get(self, request):
    if request.user.is_staff:
      repo = BrandsRepository()
      marcas = repo.get_all()

      return render(
        request,
        'brands/list.html',
        {
          'brands': marcas
        }
      )
    else:
       return redirect('index')
class BrandCreate(View):
    def get(self, request):
        if request.user.is_staff:
            form = BrandForm()
            return render(
                request,
                'brands/create.html',
                {
                  'form': form,
                }
            )
        else:
            return redirect('brand_list')
    
    def post(self, request):
        repo = BrandsRepository()
        nombre = request.POST.get('name')
        newBrand = repo.create(name=nombre)
        return redirect('brand_list')

class BrandDelete(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = BrandsRepository()
      brand = repo.get_by_id(id=id)
      repo.delete(brand=brand)
    return redirect('brand_list')

class BrandUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = BrandsRepository()
      marca = repo.get_by_id(id)

      return render(
          request,
          'brands/update.html',
          {
              'brand': marca,
          }
      )
    else:
      return redirect('brand_list')
    
  def post(self, request, id):
    if request.user.is_staff:
      repo = BrandsRepository()

      marca = repo.get_by_id(id)
      name = request.POST.get('name')
      repo.update(brand=marca,
                  nombre=name)

      return redirect('brand_list')
    else:
      return redirect('brand_list')