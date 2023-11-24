from django.db import models
from django.forms import ModelForm
# Create your models here.
class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=50)
    autores = models.ManyToManyField('Autor', default = '')
    edicion = models.CharField(max_length=50, default='')
    pag = models.IntegerField(default=0)
    desc = models.TextField(default='')
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE, default = '')
    foto = models.ImageField(upload_to='img/libros',blank=True,null=True,verbose_name='Image')
    def __str__(self):
        return self.titulo

class Autor(models.Model):
    autorId = models.IntegerField(primary_key=True, default=0)
    nombre = models.CharField(max_length=50)
    fechanac = models.DateField(default='1999-01-01')
    desc = models.TextField(default='')
    foto = models.ImageField(upload_to='img/autores',blank=True,null=True,verbose_name='Image')
    def __str__(self):
        return self.nombre
    
class Editorial(models.Model):
    editorialId = models.IntegerField(primary_key=True, default=0)
    editorial = models.CharField(max_length=30, default = '')
    creacion = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='img/editoriales',blank=True,null=True,verbose_name='Image')
    def __str__(self):
        return self.editorial