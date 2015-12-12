# -*- coding: utf-8 -*-
from django.db import models
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
    hora = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    def __unicode__(self):
        return '%s - %s' % (self.hora, self.hora_fin)


class Aula(models.Model):
    numero_aula = models.IntegerField("Numero de aula")
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

    def __unicode__(self):
        return "Fechas"


# class Programacion(models.Model):
#     idioma = models.ForeignKey(Idioma, related_name='idioma_programacion')
#     aula = models.ForeignKey(Aula, related_name='aula_programacion')
#     periodo = models.ForeignKey(Periodo, related_name='periodo_programacion')
#     ciclo_idioma = models.ForeignKey(CicloIdioma, related_name='ciclo_idioma_programacion')

#     class Meta:
#         verbose_name = "Programacion"
#         verbose_name_plural = "Programacions"

#     def __str__(self):
#         pass
