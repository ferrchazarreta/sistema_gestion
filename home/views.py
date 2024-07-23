from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.

## @login_required(login_url='login')
def index_view(request):
    return render(
        request,
        'home/index.html'
    )