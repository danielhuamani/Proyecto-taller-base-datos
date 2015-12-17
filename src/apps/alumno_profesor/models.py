# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from apps.common.constants import SEXO
# Create your models here.


class Profesor(models.Model):
    nombres = models.CharField("Nombres", max_length=120)
    apellidos = models.CharField("Apellidos", max_length=120)
    sexo = models.CharField("Sexo", max_length=120, choices=SEXO)
    telefono = models.CharField("Teléfono", max_length=12, blank=True)
    direccion = models.CharField("Dirección", max_length=120)
    codigo_profesor = models.CharField("Codigo Profesor", max_length=12, blank=True, unique=True)
    estado = models.BooleanField("Estado", default=True)
    email = models.EmailField("Email", unique=True)
    fecha_agregado = models.DateTimeField("Fecha Registrado", auto_now_add=True)
    estado = models.BooleanField("Estado", default=True)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesors"

    def get_absolute_url(self):
        return reverse('alumno_profesor:profesor_modificar', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "%s, %s" % (self.nombres, self.apellidos)


class TipoAlumno(models.Model):
    nombre = models.CharField("TIpo Alumno", max_length=120)

    class Meta:
        verbose_name = "TipoAlumno"
        verbose_name_plural = "TipoAlumnos"

    def __unicode__(self):
        return self.nombre


class Alumno(models.Model):
    tipo_alumno = models.ForeignKey(TipoAlumno, related_name='tipo_alumno_alumno')
    nombres = models.CharField("Nombres y Apellidos", max_length=120)
    apellidos = models.CharField("Apellidos", max_length=120)
    sexo = models.CharField("Sexo", max_length=120, choices=SEXO)
    telefono = models.CharField("Teléfono", max_length=12, blank=True)
    direccion = models.CharField("Dirección", max_length=120, blank=True)
    codigo_alumno = models.CharField("Codigo CIUNAC", max_length=12, blank=True)
    estado = models.BooleanField("Estado", default=True)
    fecha_agregado = models.DateTimeField("Fecha Registrado", auto_now_add=True)
    email = models.EmailField("Email")
    constancia_tipo_alumno = models.ImageField("Constancia de tipo alumno", upload_to="constancia/")
    contrasena = models.CharField("Contraseña", max_length=60)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __unicode__(self):
        return "%s, %s" % (self.nombres, self.apellidos)
