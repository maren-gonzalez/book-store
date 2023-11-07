from django import forms

class InicioSesion(forms.Form):
 email = forms.EmailField(label='Introduce tu email', max_length=100)
 contra = forms.CharField(label='Introduce tu contraseña',widget=forms.PasswordInput())