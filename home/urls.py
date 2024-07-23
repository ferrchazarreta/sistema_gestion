from django.urls import path
from home.views import (
    index_view
)

urlpatterns = [
    path('', view=index_view, name='index'),
]