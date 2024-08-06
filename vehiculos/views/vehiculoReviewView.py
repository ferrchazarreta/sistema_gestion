from django.views import View
from django.shortcuts import render, redirect

from vehiculos.repositories.reviewRepository import ReviewRepository
from vehiculos.repositories.vehiculosRepository import CarRepository

class VehiculoReviewView(View):
    def get(self, request):
        repo = ReviewRepository()
        reviews = repo.get_all()

        return render(
            request,
            'vehiculo_review/list.html',
            {'reviews': reviews}
        )
    
class VehiculoReviewCreate(View):
    def get(self, request):
        if request.user.is_cliente:
            repo = CarRepository()
            vehiculos = repo.get_all()
            return render(
                request,
                'vehiculo_review/create.html',
                {'vehiculos': vehiculos},
            )
        else:
            return redirect('review_list')
    
    def post(self, request):
        if request.user.is_cliente:
            repo = ReviewRepository()
            id_vehiculo = request.POST.get('id_vehiculo')
            opinion = request.POST.get('opinion')
            rating =  request.POST.get('rating')
            user = request.user
            repo.create(id_vehiculo, user, opinion, rating)
            return redirect('review_list')
        else:
            return redirect('review_list')
        
class VehiculoReviewDetail(View):
    def get(self, request, id):
        repo = ReviewRepository()
        review = repo.get_by_id(id=id)
        return render(
            request,
            'vehiculo_review/detail.html',
            {'review': review},
        )

class VehiculoReviewUpdate(View):
    def get(self, request, id):
        if request.user.is_cliente:
            repo = ReviewRepository()
            review = repo.get_by_id(id=id)
            return render(
                request,
                'vehiculo_review/update.html',
                {'review': review},
            )
        else:
            return redirect('review_list')

    def post(self, request, id):
        if request.user.is_cliente:
            repo = ReviewRepository()
            review = repo.get_by_id(id)
            opinion = request.POST.get('opinion')
            rating =  request.POST.get('rating')
            review.text = opinion
            review.rating = rating
            review.save()
            return redirect('review_list')
        else:
            return redirect('review_list')

class VehiculoReviewDelete(View):
    def get(self, request, id):
        if request.user.is_cliente:
            repo = ReviewRepository()
            review = repo.get_by_id(id=id)
            repo.delete(review=review)
            return redirect('review_list')
        else:
            return redirect('review_list')
            
