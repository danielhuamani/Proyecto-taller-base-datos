from django import forms
from .models import Idioma


class IdiomaForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = ('nombre',)
