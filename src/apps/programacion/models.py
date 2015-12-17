# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from apps.alumno_profesor.models import Profesor
from apps.idioma.models import CicloIdioma
# # Create your models here.


class Turno(models.Model):
    nombre = models.CharField("Turno", max_length=60)

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

    def __unicode__(self):
        return self.nombre


class Horario(models.Model):
    turno = models.ForeignKey(Turno, related_name='turno_horario')
    hora = models.TimeField("Horario Inicio")
    hora_fin = models.TimeField("Horario FIn")

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    def __unicode__(self):
        return '%s: %s - %s' % (self.turno, self.hora, self.hora_fin)


class Aula(models.Model):
    numero_aula = models.IntegerField("Numero de aula", unique=True)
    capacidad = models.IntegerField("capacidad", blank=True)

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"

    def __unicode__(self):
        return "%s - %s" % (self.numero_aula, self.capacidad)


class Periodo(models.Model):
    fecha_inicio = models.DateField("Fecha inicio")
    fecha_final = models.DateField("Fecha final")

    class Meta:
        verbose_name = "Fecha"
        verbose_name_plural = "Fechas"

    def get_absolute_url(self):
        return reverse('programacion:programacion_listado', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "%s - %s" % (self.fecha_inicio, self.fecha_final)


class Programacion(models.Model):
    aula = models.ForeignKey(Aula, related_name='aula_programacion')
    periodo = models.ForeignKey(Periodo, related_name='periodo_programacion')
    ciclo_idioma = models.ForeignKey(CicloIdioma, related_name='ciclo_idioma_programacion')
    profesor = models.ForeignKey(Profesor, related_name='profesor_programacion')
    horario = models.ForeignKey(Horario, related_name='horario_programacion')

    class Meta:
        verbose_name = "Programacion"
        verbose_name_plural = "Programacions"

    def get_absolute_url(self):
        return reverse('matricula:matricular', kwargs={'pk': self.pk})

    def get_matricula_detalle_url(self):
        return reverse('matricula:periodo_matricula_detalle', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.ciclo_idioma)
