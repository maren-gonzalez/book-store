from django.shortcuts import render
from .models import Libro, Autor, Editorial
from .forms import ComentariosForm
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    primeros_libros = Libro.objects.all()
    listaisbn = [libro.isbn for libro in primeros_libros]
    return render(request, 'index.html', {'primeros_libros': primeros_libros[:3], 'listaisbn': listaisbn})

def contact(request):
    if request.method == 'POST':
        form = ComentariosForm(request.POST)
        if form.is_valid():
            return render(request, 'contact.html', {'success': True})
    else:
        form = ComentariosForm()
    return render(request, 'contact.html', {'form': form})

def gallery(request):
    return render(request, 'gallery.html')

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
    libros_de_la_editorial = Libro.objects.filter(editorial=editorial)
    context = {'editorial': editorial, 'libros_de_la_editorial': libros_de_la_editorial}
    return render(request, "baseEditorial.html", context)

def autorDetalle(request, autorId):
    autor = get_object_or_404(Autor, pk=autorId)
    libros_del_autor = Libro.objects.filter(autores=autor)
    context = {'autor': autor, 'libros_del_autor': libros_del_autor}
    return render(request, "baseAutor.html", context)