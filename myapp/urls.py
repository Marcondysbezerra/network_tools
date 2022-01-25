from django.urls import path
from . import views


urlpatterns = [
    path('', views.teste_de_portas, name='teste-portas'),

]
