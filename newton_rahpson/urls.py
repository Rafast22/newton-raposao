from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular, name='calcular'),
    path('calcular', views.calcular, name='calcular'),
]