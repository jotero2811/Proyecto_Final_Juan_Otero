from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Frutosecos(models.Model):

    def __str__(self):

        return f"{self.nombre}"
    
    nombre = models.CharField(max_length=40)
    presentacion = models.CharField(max_length=40)
    precio = models.FloatField()

class Semillas(models.Model):

    def __str__(self):

        return f"{self.nombre}"
    
    nombre = models.CharField(max_length=40)
    presentacion = models.CharField(max_length=40)
    precio = models.FloatField()

class Especias(models.Model):

    def __str__(self):

        return f"{self.nombre}"
    
    nombre = models.CharField(max_length=40)
    presentacion = models.CharField(max_length=40)
    precio = models.FloatField()


class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
    
        return f"{self.usuario} --- {self.imagen}"


