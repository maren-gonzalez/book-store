from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('gallery.html/', views.gallery, name='gallery'),
 path('contact.html/', views.contact, name='contact'),
 path('about.html/', views.about, name='about'),
 path('libros.html/', views.libros, name='libros'),
 path('autor.html/', views.autor, name='autor'),
  path('genero.html/', views.genero, name='genero'),
]
