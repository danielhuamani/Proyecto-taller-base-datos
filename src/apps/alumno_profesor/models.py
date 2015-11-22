# -*- coding: utf-8 -*-
from django.db import models
from apps.common.constants import SEXO
# Create your models here.


class Profesor(models.Model):
    nombres = models.CharField("Nombres", max_length=120)
    apellidos = models.CharField("Apellidos", max_length=120)
    sexo = models.CharField("Sexo", max_length=120, choices=SEXO)
    telefono = models.CharField("Teléfono", max_length=12, blank=True)
    direccion = models.CharField("Dirección", max_length=120)
    codigo_profesor = models.CharField("Codigo Profesor", max_length=12, blank=True)
    estado = models.BooleanField("Estado", default=True)
    email = models.EmailField("Email")
    fecha_agregado = models.DateTimeField("Fecha Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesors"

    def __unicode__(self):
        return "%s, %s" % (self.nombres, self.appellidos)


class TipoAlumno(models.Model):
    nombre = models.CharField("TIpo Alumno", max_length=120)

    class Meta:
        verbose_name = "TipoAlumno"
        verbose_name_plural = "TipoAlumnos"

    def __unicode__(self):
        return self.nombre


class Alumno(models.Model):
    tipo_alumno = models.ForeignKey(TipoAlumno, related_name='tipo_alumno_alumno')
    nombres = models.CharField("Nombres", max_length=120)
    apellidos = models.CharField("Apellidos", max_length=120)
    sexo = models.CharField("Sexo", max_length=120, choices=SEXO)
    telefono = models.CharField("Teléfono", max_length=12, blank=True)
    direccion = models.CharField("Dirección", max_length=120, blank=True)
    codigo_alumno = models.CharField("Codigo CIUNAC", max_length=12, blank=True)
    estado = models.BooleanField("Estado", default=True)
    fecha_agregado = models.DateTimeField("Fecha Registrado", auto_now_add=True)
    email = models.EmailField("Email")
    constancia_tipo_alumno = models.ImageField("Constancia de tipo alumno", upload_to="constancia/")

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __unicode__(self):
        return "%s, %s" % (self.nombres, self.appellidos)
