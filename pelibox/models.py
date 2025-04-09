from django.db import models

class Reseña(models.Model):
    titulo = models.CharField(max_length=200)
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    puntuacion = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.usuario}"
