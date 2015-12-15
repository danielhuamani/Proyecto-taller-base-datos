from django.db import models
from apps.alumno_profesor.models import Alumno
from apps.programacion.models import Programacion
# Create your models here.


class Matricula(models.Model):
    programacion = models.ForeignKey(Programacion, related_name='programacion_matricula')
    alumno = models.ForeignKey(Alumno, related_name='alumno_matricula')
    recibo = models.FileField("Recibo", upload_to="recibo")

    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

    def __str__(self):
        return '%s - %s' % (self.alumno, self.programacion)
