from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('gallery.html/', views.gallery, name='gallery'),
 path('gallery.html/<str:categoria>', views.gallery, name='gallery'),
 path('contact.html/', views.contact, name='contact'),
 path('about.html/', views.about, name='about'),
 path('libros.html/', views.libros, name='libros'),
 path('libros.html/<str:isbn>', views.libros, name='libros'),
 path('autor.html/', views.autor, name='autor'),
 path('autor.html/<str:id_autor>', views.autor, name='autor'),
 path('editorial.html/', views.editorial, name='editorial'),
 path('editorial.html/<str:editorial>', views.editorial, name='editorial')
]
