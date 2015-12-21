from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from apps.programacion.models import Periodo, Programacion
from apps.matricula.forms import MatriculaForm
from apps.alumno_profesor.forms import AlumnoForm, AlumnoDetalleForm
from apps.common.util import paginador_general
import datetime
from .models import Matricula, Recibo
from .forms import ReciboForm
from django.http import JsonResponse
import json
# Create your views here.


def inicio_matricula(request):
    periodos = Periodo.objects.all().order_by("-fecha_final")
    return render(request, "sistema/index.html", locals())


def matricular(request, pk=False):
    programacion = get_object_or_404(Programacion, pk=pk)
    alumno = request.user
    if request.method == "POST":
        matriculaform = MatriculaForm(request.POST, request.FILES)

        if matriculaform.is_valid():
            matricula_guardado = matriculaform.save(commit=False)
            matricula_guardado.alumno = alumno
            matricula_guardado.save()
            return redirect(reverse("matricula:matricula_gracias"))
    else:
        alumnoform = AlumnoForm()
        matriculaform = MatriculaForm()
    return render(request, "matricula/matricula.html", locals())


def matricula_gracias(request):
    return render(request, "matricula/matricula_gracias.html", locals())


def periodo_matricula_detalle(request, pk=False):
    programacion = get_object_or_404(Programacion, pk=pk)
    alumnos = Matricula.objects.filter(programacion=programacion).prefetch_related("alumno")
    pagina = request.GET.get("pag", 1)
    pagina_cantidad = request.GET.get('pcantidad', 25)
    alumnos = paginador_general(alumnos, pagina_cantidad, pagina)
    return render(request, "matricula/periodo_matricula_listado.html", locals())


def matricula_alumno_detalle(request, pk=False):
    matricula = get_object_or_404(Matricula, pk=pk)
    recibo = Recibo.objects.filter(matricula=matricula)
    alumno = request.user
    if recibo:
        recibo = recibo[0]
        existe_recibo = True
    else:
        recibo = Recibo()
        existe_recibo = False
    if request.method == "POST":
        form = ReciboForm(request.POST, instance=recibo)
        estado = request.POST.get("estado_alumno")
        if estado:
            alumno.is_active = True
        else:
            alumno.is_active = False
        alumno.save()
        print alumno.is_active
        if form.is_valid():
            form.save()
            matricula.estado = True
            matricula.save()
            return redirect(reverse("matricula:periodo_matricula_detalle", kwargs={"pk": matricula.programacion.pk}))
    else:
        form = ReciboForm(instance=recibo)

    return render(request, "matricula/periodo_matricula_detalle.html", locals())


def api_validar_matricula(request):
    if request.is_ajax():
        if request.method == "POST":
            numero_recibo = request.POST.get("numero_recibo")
            if numero_recibo:
                existe_recibo = Recibo.objects.filter(numero_recibo=numero_recibo)
                if existe_recibo:
                    data = {"status": existe_recibo[0].matricula.get_absolute_url()}
                else:
                    data = {"status": "valido"}
    else:
        data = {"status": "error"}
    return JsonResponse(data)


def mi_matricula_listado(request):
    alumno = request.user
    matriculas = Matricula.objects.filter(alumno=alumno).order_by("fecha_creacion")
    print matriculas
    return render(request, "matricula/mi_matricula_listado.html", locals())
