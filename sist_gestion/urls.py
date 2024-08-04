from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('home.urls')),
    path('admin/', admin.site.urls),
    path('vehiculos/', include('vehiculos.urls')),
    path('usuarios/', include('usuario.urls')),
    path('noticias/',include('noticias.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
