from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('^i18n/', include('django.conf.urls.i18n')),   
    path('',include('home.urls')),
    path('admin/', admin.site.urls),
    path('vehiculos/', include('vehiculos.urls')),
    path('usuarios/', include('usuario.urls')),
    path('noticias/',include('noticias.urls')),
    path('api_v1/',include('api_v1.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
