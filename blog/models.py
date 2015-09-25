# Create your models here.

from django.db import models
from django.utils import timezone

class Postear(models.Model):
    autor = models.ForeignKey('auth.User')# mando a crear una llave foranea con el nombre
    titulo = models.CharField(max_length=200)
    texto = models.TextField()#puedo crear todo lo que quiera
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
