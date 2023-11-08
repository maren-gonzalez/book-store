from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Libro, Autor, Genero, modeloGuardar
from .forms import InicioSesion
# Create your views here.

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


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def single(request):
    return render(request, 'single.html')

def libros(request):
    return render(request, 'libros.html')

def autor(request):
    return render(request, 'autor.html')

def genero(request):
    return render(request, 'genero.html')

#CAPTURAR ERORRES
