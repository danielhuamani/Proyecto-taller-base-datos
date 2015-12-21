from django.db import models
from django.core.urlresolvers import reverse
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

    def get_absolute_url(self):
        return reverse('matricula:matricula_alumno_detalle', kwargs={'pk': self.pk})

    def get_valida_url(self):
        return reverse('matricula:matricula_valida', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s - %s' % (self.alumno, self.programacion)


class Recibo(models.Model):
    fecha_creacion = models.DateTimeField("Fecha creacion", auto_now_add=True)
    numero_recibo = models.IntegerField("Numero de Recibo", unique=True)
    matricula = models.OneToOneField(Matricula, related_name='matricula_recibo')

    class Meta:
        verbose_name = "Recibo"
        verbose_name_plural = "Recibos"

    def __str__(self):
        return str(self.numero_recibo)
