from django.urls import path
from .views import inscricoes_abertas



urlpatterns = [
    path('inscricoes/', inscricoes_abertas, name='inscricoes_abertas'),
]