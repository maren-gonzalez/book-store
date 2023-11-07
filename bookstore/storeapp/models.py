from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class Libro(models.Model):
    isbn = models.CharField(max_length=13)
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)

    #def __str__(self):
        #return self.name

#class LibroForm(ModelForm):
 #class Meta:
    #model = Libro
    #fields = '__all__'

class Autor(models.Model):
    autorId = models.AutoField(primary_key=True, default=0)
    nombre = models.CharField(max_length=50)

    #def __str__(self):
        #return self.name

#class AutorForm(ModelForm):
 #class Meta2:
    #model = Autor
    #fields = '__all__'

class Genero(models.Model):
    generoId = models.AutoField(primary_key=True, default=0)
    genero = models.CharField(max_length=30)

    #def __str__(self):
        #return self.name

#class GeneroForm(ModelForm):
 #class Meta3:
    #model = Genero
    #fields = '__all__'

class modeloGuardar(models.Model):
    email = forms.EmailField(label='Introduce tu email', max_length=20)
    contra = forms.CharField(label='Introduce tu contraseña',widget=forms.PasswordInput())

#métodos