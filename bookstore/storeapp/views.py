from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Libro, Autor, Editorial
from .forms import InicioSesion
# Create your views here.

def loginform(request):
 form = InicioSesion()
 return render(
 request, 'forms.html', {'form':form}
 )

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

def editorial(request):
    return render(request, 'editorial.html')