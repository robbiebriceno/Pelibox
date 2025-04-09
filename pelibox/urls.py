from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar_pelicula, name='buscar_pelicula'),
    path('agregar/', views.agregar_reseña, name='agregar_reseña'),
]
