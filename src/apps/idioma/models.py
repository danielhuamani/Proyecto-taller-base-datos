# -*- coding: utf-8 -*-
from django.db import models
from .constants import CHOICES_NIVEL


# Create your models here. #
class Idioma(models.Model):
    nombre = models.CharField("Nombre del idioma", max_length=120)

    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"

    def __unicode__(self):
        return self.nombre


class NivelIdioma(models.Model):
    nombre = models.CharField("Nombre del Nivel idioma", max_length=120, choices=CHOICES_NIVEL)

    class Meta:
        verbose_name = "Nivel Idioma"
        verbose_name_plural = "Nivel Idiomas"

    def __unicode__(self):
        return self.nombre


class CicloIdioma(models.Model):
    nivel_idioma = models.ForeignKey(NivelIdioma, related_name='nivel_idioma_ciclo')
    nombre = models.CharField("Nombre", max_length=2)

    class Meta:
        verbose_name = "CicloIdioma"
        verbose_name_plural = "CicloIdiomas"

    def __unicode__(self):
        return self.nombre
