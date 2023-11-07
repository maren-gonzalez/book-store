from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('products.html/', views.libros, name='productos'),
 path('contact.html/', views.contacto, name='contacto'),
 path('about.html/', views.login, name='login')
]
