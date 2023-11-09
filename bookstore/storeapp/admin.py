from django.contrib import admin

# Register your models here.
from .models import Libro, Autor, Editorial
# Register your models here.
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Editorial)