from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro, Autor, Genero
# Create your views here.

#def index(request):
#    return HttpResponse('yey')

def libro(request):
 libro = Libro.objects.order_by('isbn')
 output = ', '.join([l.isbn for l in libro]) +  ', '.join([l.titulo for l in libro])
 return HttpResponse(output)

def autor(request):
    autor = Autor.objects.order_by('autorId')
    output = ', '.join([a.autorId for a in autor])
    return HttpResponse(output)

def index(request):
    nombre = 'Maren'
    context = {
        'login': True,
        'nombre': nombre
    }
    return render(request, 'index.html',context)



#CAPTURAR ERORRES
