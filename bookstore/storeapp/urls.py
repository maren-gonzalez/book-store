from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('gallery', views.gallery, name='gallery'),
 path('contact', views.contact, name='contact'),
 path('libros', views.libros, name='libros'),
 path('libro/<str:isbn>', views.libroDetalle, name='libroDetalle'),
 path('autor', views.autor, name='autor'),
 path('autor/<int:autorId>', views.autorDetalle, name='autorDetalle'),
 path('editorial', views.editorial, name='editorial'),
 path('editorial/<int:editorialId>', views.editorialDetalle, name='editorialDetalle'),
]
