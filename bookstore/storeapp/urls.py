from django.urls import path
from . import views
urlpatterns = [
 path('', views.loginform, name='index'),
 # ej: /miApp/empresas/
 path('libro/', views.libro, name='libro'),
 path('autor/', views.autor, name='autor'),
 
]
