from django.contrib import admin
from .models import Libro, Autor, Editorial
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# Registrar el modelo con las nuevas configuraciones
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'isbn', 'editorial', 'mostrar_autores')
    list_filter = ('editorial', 'autores')
    search_fields = ('titulo', 'autores__nombre')
    filter_horizontal = ('autores',)

    def mostrar_autores(self, obj):
        return ", ".join([autor.nombre for autor in obj.autores.all()])

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fechanac')
    search_fields = ('nombre',)

class EditorialAdmin(admin.ModelAdmin):
    list_display = ('editorial', 'creacion')
    search_fields = ('editorial',)

admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editorial, EditorialAdmin)

# Cambiar los permisos de cada usuario

class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_staff'].initial = False
        self.fields['is_superuser'].initial = False

class UsuarioAdmin(BaseUserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm

    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permisos', {'fields': ('is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )

admin.site.unregister(User)
admin.site.register(User, UsuarioAdmin)