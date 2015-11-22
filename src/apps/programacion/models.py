from django.db import models
from apps.idioma.models import Idioma, CicloIdioma
# # Create your models here.

# class Horario(models.Model):
#     turno = models.CharField("Turno")
#     dia = models.CharField("Día")
#     hora = models.C
#     class Meta:
#         verbose_name = "Horario"
#         verbose_name_plural = "Horarios"

#     def __str__(self):
#         pass


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


class Programacion(models.Model):
    idioma = models.ForeignKey(Idioma, related_name='idioma_programacion')
    aula = models.ForeignKey(Aula, related_name='aula_programacion')
    periodo = models.ForeignKey(Periodo, related_name='periodo_programacion')
    ciclo_idioma = models.ForeignKey(CicloIdioma, related_name='ciclo_idioma_programacion')

    class Meta:
        verbose_name = "Programacion"
        verbose_name_plural = "Programacions"

    def __str__(self):
        pass
