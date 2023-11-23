from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Libro, Autor, Editorial
from django.shortcuts import get_object_or_404, get_list_or_404
# Create your views here.



def index(request):
    return render(request, 'base.html')

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

def libroDetalle(request, isbn):
    libro = get_object_or_404(Libro, pk=isbn)
    context = { 'libro': libro}
    return render(request, 'baseLibro.html', context)

def editorialDetalle(request, editorialId):
    editorial = get_object_or_404(Editorial, pk=editorialId)
    context = {'editorial': editorial}
    return render(request, "baseEditorial.html", context)

def autorDetalle(request, autorId):
    autor = get_object_or_404(Autor, pk=autorId)
    context = {'autor': autor}
    return render(request, "baseAutor.html", context)

