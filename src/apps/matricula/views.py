from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from apps.programacion.models import Periodo, Programacion
from apps.matricula.forms import MatriculaForm
from apps.alumno_profesor.forms import AlumnoForm
from apps.common.util import paginador_general
import datetime
from .models import Matricula
# Create your views here.


def inicio_matricula(request):
    periodos = Periodo.objects.all().order_by("-fecha_final")
    return render(request, "sistema/index.html", locals())


def matricular(request, pk=False):
    programacion = get_object_or_404(Programacion, pk=pk)
    if request.method == "POST":
        matriculaform = MatriculaForm(request.POST, request.FILES)
        alumnoform = AlumnoForm(request.POST, request.FILES)
        if alumnoform.is_valid() and matriculaform.is_valid():
            alumno_guardado = alumnoform.save()
            matricula_guardado = matriculaform.save(commit=False)

            matricula_guardado.alumno = alumno_guardado
            matricula_guardado.save()
            return redirect(reverse("matricula:matricula_gracias"))
    else:
        alumnoform = AlumnoForm()
        matriculaform = MatriculaForm()
    return render(request, "matricula/matricula.html", locals())


def matricula_gracias(request):
    return render(request, "matricula/matricula_gracias.html", locals())


def periodo_matricula(request):
    periodos = Periodo.objects.all().order_by("-fecha_final")
    pagina = request.GET.get("pag", 1)
    pagina_cantidad = request.GET.get('pcantidad', 50)
    query_fecha_inicio = request.GET.get("fecha_inicio", "")
    query_fecha_final = request.GET.get("fecha_final", "")
    if query_fecha_inicio:
        query_fecha_inicio = datetime.datetime.strptime(query_fecha_inicio, "%d-%m-%Y").date()
        periodos = periodos.filter(fecha_inicio__gte=query_fecha_inicio)
    if query_fecha_final:
        query_fecha_final = datetime.datetime.strptime(query_fecha_final, "%d-%m-%Y").date()
        periodos = periodos.filter(fecha_inicio__lte=query_fecha_final)
    periodos = paginador_general(periodos, pagina_cantidad, pagina)
    return render(request, "matricula/periodo_matricula_listado.html", locals())


def periodo_matricula_detalle(request, pk=False):
    programacion = get_object_or_404(Programacion, pk=pk)
    alumnos = Matricula.objects.filter(programacion=programacion).prefetch_related("alumno")
    return render(request, "matricula/periodo_matricula_detalle.html", locals())
