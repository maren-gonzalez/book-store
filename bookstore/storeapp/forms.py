from django import forms

class ComentariosForm(forms.Form):
    name = forms.CharField(label='NOMBRE')
    email = forms.EmailField(label='EMAIL')
    comments = forms.CharField(label='COMENTARIOS', widget=forms.Textarea)
