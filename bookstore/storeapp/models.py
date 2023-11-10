from django.db import models
from django.forms import ModelForm

# Create your models here.
class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.ManyToManyField('Autor', default = '')
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE, default = '')

class Autor(models.Model):
    autorId = models.IntegerField(primary_key=True, default=0)
    nombre = models.CharField(max_length=50)
    fechanac = models.DateField(default='1999-01-01')

class Editorial(models.Model):
    editorialId = models.IntegerField(primary_key=True, default=0)
    editorial = models.CharField(max_length=30, default = '')