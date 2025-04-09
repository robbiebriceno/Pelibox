import requests
from django.shortcuts import render, redirect
from .models import Reseña

API_KEY = '7a921c76'  # 🔁 Reemplaza por tu key de https://www.omdbapi.com/apikey.aspx

def buscar_pelicula(request):
    datos_pelicula = None
    reseñas = None
    peliculas_con_reseñas = []

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        url = f'http://www.omdbapi.com/?t={titulo}&apikey={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            datos_pelicula = response.json()
            reseñas = Reseña.objects.filter(titulo__iexact=titulo)

    # Obtener todos los títulos únicos con reseñas
    titulos_unicos = Reseña.objects.values_list('titulo', flat=True).distinct()

    for titulo in titulos_unicos:
        url = f'http://www.omdbapi.com/?t={titulo}&apikey={API_KEY}'
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            if data.get("Response") == "True":
                peliculas_con_reseñas.append({
                    "titulo": titulo,
                    "poster": data.get("Poster"),
                    "año": data.get("Year"),
                    "genero": data.get("Genre")
                })

    return render(request, 'peliculas.html', {
        'pelicula': datos_pelicula,
        'reseñas': reseñas,
        'galeria': peliculas_con_reseñas
    })


def agregar_reseña(request):
    if request.method == 'POST':
        Reseña.objects.create(
            titulo=request.POST['titulo'],
            usuario=request.POST['usuario'],
            comentario=request.POST['comentario'],
            puntuacion=request.POST['puntuacion']
        )
    return redirect('buscar_pelicula')
