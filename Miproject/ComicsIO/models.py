from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
# 3 Clases hacer sus respectivos formularios
class Comic(models.Model):
    comic = models.CharField(max_length=40)
    precio = models.IntegerField()
    FechaDePublicacion = models.CharField(max_length = 20)
    def __str__(self):
        return f"{self.comic}"
    class Meta:
        ordering = ["comic"]
        


class el_post(models.Model):
    Titulo = models.CharField(max_length=100)
    Texto = models.TextField()
    fechaCreacion = models.DateTimeField()
    default=timezone.now()
    def __str__(self):
        return f"{self.Titulo}, {self.Texto}, {self.fechaCreacion}"
    class Meta1:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["fechaCreacion"]


class OpinionDelComic(models.Model):
        nombreDelcomic = models.CharField(max_length = 50)
        autor = models.CharField(max_length = 50)
        La_opinion = models.TextField(max_length = 250)
        def __str__(self):
            return f"{self.nombreDelcomic} {self.autor} // {self.La_opinion}"
        

class BuscarComic(models.Model):
        nombreDelcomic = models.CharField(max_length = 50)
        precio = models.IntegerField()
        def __str__(self):
            return f"{self.nombreDelcomic} {self.precio} "
        

# CORRER EL SERVER EN LA RUTA STANDART python manage.py runserver, ahi anda el ADMIN