from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE)

class Autor(models.Model):
    autorId = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechanac = models.DateField()


class Editorial(models.Model):
    editorialId = models.IntegerField(primary_key=True)
    editorial = models.CharField(max_length=30)


class modeloGuardar(models.Model):
    email = forms.EmailField(label='Introduce tu email', max_length=20)
    contra = forms.CharField(label='Introduce tu contraseña',widget=forms.PasswordInput())

#métodos