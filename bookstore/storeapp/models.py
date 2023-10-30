from django.db import models

# Create your models here.
class Libro(models.Model):
    isbn = models.CharField(max_length=13)
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)

class Autor(models.Model):
    autorId = models.AutoField
    nombre = models.CharField(max_length=50)

class Genero(models.Model):
    generoId = models.AutoField
    genero = models.CharField(max_length=30)

#métodos
