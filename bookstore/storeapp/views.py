from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Libro, Autor, Genero, modeloGuardar
from .forms import InicioSesion
# Create your views here.

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

def loginform(request):
 form = InicioSesion()
 return render(
 request, 'forms.html', {'form':form}
 )

def get_datos(request):
 if request.method == 'POST':
 # Crear una instancia del formulario y asociar los datos recibidos:
    form = InicioSesion(request.POST)
    # Validar los datos:
    if form.is_valid():
        mail = form.cleaned_data['email']
        cont = form.cleaned_data['contra']
        guardar = modeloGuardar(email=mail, contra=cont)
        guardar.save()
        return HttpResponseRedirect('/index/')
 # Si el metodo es GET (o cualquier otro) crear un formulario vacío
 else:
    form = InicioSesion()
 # Renderizar la plantilla con el formulario (con los datos anteriores o vacío)
 return render(request, 'forms.html', {'form': form})


#CAPTURAR ERORRES
