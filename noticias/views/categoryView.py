from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from noticias.forms import CategoryForm
from noticias.repositories.categoryRepository import CategoryRepository

class CategoryView(View):
  def get(self, request):
    repo = CategoryRepository()
    categorias = repo.get_all()

    return render(
      request,
      'category/list.html',
      {
        'categories': categorias
      }
    )

class CategoryCreate(View):
    def get(self, request):
        if request.user.is_staff:
            form = CategoryForm()
            return render(
                request,
                'category/create.html',
                {
                  'form': form,
                }
            )
        else:
            return redirect('category_list')
    
    def post(self, request):
        repo = CategoryRepository()
        nombre = request.POST.get('name')
        newBrand = repo.create(name=nombre)
        return redirect('category_list')

class CategoryDelete(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = CategoryRepository()
      category = repo.get_by_id(id=id)
      repo.delete(category=category)
    return redirect('category_list')

class CategoryUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      repo = CategoryRepository()
      categoria = repo.get_by_id(id)

      return render(
          request,
          'category/update.html',
          {
            'category': categoria,
          }
      )
    else:
      return redirect('category_list')
    
  def post(self, request, id):
    if request.user.is_staff:
      repo = CategoryRepository()

      categoria = repo.get_by_id(id)
      name = request.POST.get('name')
      repo.update(category=categoria,
                  nombre=name)

      return redirect('category_list')
    else:
      return redirect('category_list')