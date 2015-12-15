from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from apps.programacion.models import Periodo, Programacion
# Create your views here.


def inicio_matricula(request):
    periodos = Periodo.objects.all().order_by("-fecha_final")
    return render(request, "sistema/index.html", locals())


def matricular(request, pk=False):
    programacion = get_object_or_404(Programacion, pk=pk)
    print programacion
    return render(request, "matricula/matricula.html", locals())
