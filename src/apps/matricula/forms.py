from django import forms
from .models import Matricula, Recibo


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ('programacion', 'alumno', 'recibo', 'observacion')


class ReciboForm(forms.ModelForm):
    class Meta:
        model = Recibo
        fields = ('matricula', 'numero_recibo')
