from django import forms
from .models import Profesor


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombres', 'apellidos', 'sexo', 'telefono', 'direccion', 'codigo_profesor', 'estado', 'email', 'estado')

