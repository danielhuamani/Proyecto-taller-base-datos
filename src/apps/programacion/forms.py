from django import forms
from .models import Periodo, Programacion


class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ('fecha_inicio', 'fecha_final',)


class ProgramacionForm(forms.ModelForm):
    class Meta:
        model = Programacion
        fields = ('aula', 'periodo', 'ciclo_idioma', 'profesor', 'horario')
