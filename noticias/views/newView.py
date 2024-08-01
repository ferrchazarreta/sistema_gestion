from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from noticias.forms import NewsForm
from noticias.repositories.newsRepository import NewRepository
from noticias.repositories.categoryRepository import CategoryRepository
# from vehiculos.repositories.fuelRepository import FuelRepository
# from vehiculos.repositories.countriesRepository import CountriesRepository
# from vehiculos.repositories.modelsRepository import ModelsRepository

class NewsView(View):
  def get(self, request):
    repo = NewRepository()
    noticias = repo.get_all()

    return render(
      request,
      'noticias/list.html',
      {
        'news': noticias
      }
      )

class NewsCreate(View):
  def get(self, request):
    if request.user.is_staff:
      form = NewsForm()
      
      return render(
        request,
        'noticias/create.html',
        {
          'form': form,
        }
      )
    else:
      return redirect('noticias_list')
    
  def post(self, request):
    if request.user.is_staff:
      newRepo = NewRepository()
      categoryRepo = CategoryRepository()
      data = request.POST

      # codigo para guardar las imagenes dentro de los archivos
      if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
          form.save()
          return redirect('noticias_list') #redirigue a donde deseas
      else:
        form = NewsForm()
        return render(request, 'noticias_list', {
      })

      categoryId = data.get('category')
      category = categoryRepo.get_by_id(id=categoryId)
        

      newRepo.create(
        title=data.get('title'),
        short_description=data.get('short_description'),
        long_description=data.get('long_description'),
        category=category,
        image=data.get('image'),
      )
      
      return redirect('noticias_list')
    else:
      return redirect('noticias_list')

class NewDetail(View):
  def get(self, request, id):
    repo = NewRepository()
    noticia = repo.get_by_id(id=id)
    return render(
      request,
      'noticias/detail.html',
      {
        'news': noticia,
      }
    )

class NewsDelete(View):
    def get(self, request, id):
        if request.user.is_staff:
            repo = NewRepository()
            vehiculo = repo.get_by_id(id=id)
            repo.delete(vehiculo=vehiculo)
        return redirect('noticias_list')

class NewsUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      newRepo = NewRepository()
      categoryRepo = CategoryRepository()

      noticia = newRepo.get_by_id(id)
      categorias = categoryRepo.get_all()

      return render(
        request,
        'noticias/update.html',
        {
          'new': noticia,
          'categories': categorias,
        }
      )
    else:
      return redirect('noticias_list')
  
  def post(self, request, id):
    if request.user.is_staff:
      newRepo = NewRepository()
      categoryRepo = CategoryRepository()

      noticia = newRepo.get_by_id(id)
      categoria = categoryRepo.get_by_id(request.POST.get('category'))
      data = request.POST
      
      # Verificar si se ha cargado una nueva imagen
      if 'image' in request.FILES:
        noticia.image = request.FILES['image']

      newRepo.update(
        noticia,
        title= data.get('title'),
        category = categoria,
        short_description=data.get('short_description'),
        long_description=data.get('long_description'),
        image=data.get('image'),
      )

      return redirect('noticias_list')
    else:
      return redirect('noticias_list')