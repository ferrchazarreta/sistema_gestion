from django.views import View
from django.shortcuts import render, redirect

from vehiculos.forms import CountryForm
from vehiculos.repositories.countriesRepository import CountriesRepository


class CountryView(View):
  def get(self, request):
    repo = CountriesRepository()
    countries = repo.get_all()

    return render(
      request,
      'country/list.html',
      {
        'countries': countries
      }
      )

class CountryCreate(View):
  def get(self, request):
    if request.user.is_staff:
      form = CountryForm()

      return render(
        request,
        'country/create.html',
        {
          'form': form,
        }
      )
    else:
      return redirect('country_list')

  def post(self, request):
    if request.user.is_staff:
      countryRepo = CountriesRepository()
      data = request.POST
      country = data.get('country_name')

      countryRepo.create(
        name = country
      )

      return redirect('country_list')
    else:
      return redirect('country_list')


class CountryDelete(View):
    def get(self, request, id):
        if request.user.is_staff:
            repo = CountriesRepository()
            country = repo.get_by_id(id=id)
            repo.delete(country=country)
        return redirect('country_list')

class CountryUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      countryRepo = CountriesRepository()
      country = countryRepo.get_by_id(id)

      return render(
        request,
        'country/update.html',
        {
          'country': country,

        }
      )
    else:
      return redirect('country_list')

  def post(self, request, id):
    if request.user.is_staff:
      countryRepo = CountriesRepository()
      country = countryRepo.get_by_id(id)
      data = request.POST



      countryRepo.update(
        country=country,
      )

      return redirect('country_list')