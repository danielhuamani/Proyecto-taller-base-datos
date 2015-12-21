from django import forms
from .models import Profesor, Alumno


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombres', 'apellidos', 'sexo', 'telefono', 'direccion', 'codigo_profesor', 'estado', 'email', 'estado')


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombres', 'apellidos', 'tipo_alumno', 'constancia_tipo_alumno', 'sexo', 'telefono', 'direccion', 'email', 'contrasena')


class AlumnoDetalleForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombres', 'apellidos', 'tipo_alumno', 'constancia_tipo_alumno', 'sexo', 'telefono', 'direccion', 'email', 'is_active')
