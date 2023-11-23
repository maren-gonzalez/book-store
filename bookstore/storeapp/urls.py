from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('gallery.html/', views.gallery, name='gallery'),
 path('gallery.html/<str:categoria>', views.gallery, name='gallery'),
 path('contact.html/', views.contact, name='contact'),
 path('about.html/', views.about, name='about'),
 path('libros.html/', views.libros, name='libros'),
 path('libro/<str:isbn>', views.libroDetalle, name='libroDetalle'),
 path('autor.html/', views.autor, name='autor'),
 path('autor.html/<int:autorId>', views.autor, name='autor'),
 path('autor/<int:autorId>', views.autorDetalle, name='autorDetalle'),
 path('editorial.html/', views.editorial, name='editorial'),
 path('editorial.html/<str:editorialId>', views.editorial, name='editorial'),
 path('editorial/<int:editorialId>', views.editorialDetalle, name='editorialDetalle'),
]
