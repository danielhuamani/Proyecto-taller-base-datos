from django.db import models
from apps.alumno_profesor.models import Alumno
from apps.programacion.models import Programacion
# Create your models here.


class Matricula(models.Model):
    fecha_creacion = models.DateTimeField("fecha_creacion", auto_now_add=True)
    programacion = models.ForeignKey(Programacion, related_name='programacion_matricula')
    alumno = models.ForeignKey(Alumno, related_name='alumno_matricula', null=True, blank=True)
    recibo = models.FileField("Recibo de la matricula", upload_to="recibo")
    observacion = models.TextField("Observacion", blank=True, null=True)
    estado = models.BooleanField("Estado", default=False)

    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

    def __str__(self):
        return '%s - %s' % (self.alumno, self.programacion)
